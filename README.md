# Research Agent

This is a Research Agent, which is built using LangChain, gemini-2.5-flask, to perform a deep research on the topic provided by the user. Agent refers to [search_tool, wiki_tool] for research and then save the generated research content inside the reseached_files folder in .txt format.

## Features:

### main.py
1. @tool 'def search_tool()': To take reference from: https://duckduckgo.com/
2. @tool 'def wiki_tool()': To take reference from: https://www.wikipedia.org/
3. @tool 'def save_tool(): To save the generated research content in text format.
    * It is saved in researched_files folder with a relevant name with the timestamp.

### tools.py

4. class ResearchResponse(): To generated the research in a structered format: 
    * topic: Topic provided by the user.
    * summary: Body of the generated reseacrh.
    * conclusion: Conclusion of the research.
    * related_topics_to_research: Topics related to the input.
    * sources: Sources from where AI Agent extracted the content.
    * tools_used: What @tools are used by the Agent.

5. llm: To generate the reponse after calling the @tools.
    * temperature = 0 {To maitain the accuracy of the research}
    * model= To intialise gemini-2.5.-flash model from Google.
    * convert_system_message_to_human: To handle the system message.
    * google_api_key= To load the GEMINI_API_KEY from .env folder.
6. system_prompt: To guide gemini in research and response.
7. query: To take user input. (Topic to research on)
8. agent: To create_agent using llm and tools.

### researched_files/

* To save researched content in .txt format


## Technologies used:

1. Python
2. LangChain
3. Pydantic
4. gemini-2.5-flash


