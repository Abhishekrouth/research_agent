from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool
import os

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    conclusion: str
    related_topics_to_research: str
    sources: list[str]
    tools_used: list[str]

tools = [search_tool, wiki_tool, save_tool]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_output_tokens=870,
    convert_system_message_to_human=True,
    google_api_key=os.getenv("GEMINI_API_KEY")
).bind_tools(tools)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

path = 'researched_files/'

system_prompt = f"""

You are a research assistant. Research on topic input by user.

Rules for research:
- Keep changing lines after 12-16 words.
- Don't include JSON in the output.
- Follow the max_output_token limit.
- Call both [search_tool, wiki_tool] to search.
- Call [save_tool] to save the generted research and save it into {path} folder in text format, not in JSON(change lines after every 10 words)
- Return the final answer as plain text only.
- Do not include tool calls or structured message parts.
- State an interesting_facts related to the topic.
- Include 2 related_topics_to_research similar to the original topic.
- Do not include 'extras'.
- Verbose: Detailed.

{parser.get_format_instructions()}

"""
query = input("Hello, What do you want to research on?\n")
print("___"*30)
print(f"\nResarching on {query}...\n")

agent = create_agent(
    model=llm,
    tools=tools
)

result = agent.invoke(
    {
        "messages": [
            ("system", system_prompt),
            ("human", query)
            ]
    }
)

final_message = result["messages"][-1].content
if isinstance(final_message, list):
    final_text = "".join(
        part.get("text", "") for part in final_message if part.get("type") == "text"
    )
else:
    final_text = final_message

structured_response = parser.parse(final_text)
print(structured_response)