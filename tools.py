from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from datetime import datetime

search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:

    """Search the web for information using DuckDuckGo"""
    return search.run(query)

api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=100
)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)


@tool
def wiki_tool(query: str) -> str:
    """Fetch a short summary from Wikipedia"""
    return wiki.run(query)

@tool
def save_tool(data: str, filename: str = "researched_files/research_output.txt") -> str:
    """Save structured research data to a text file inside researched_files folder"""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    formatted_text = (
        f"Research Output\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"
