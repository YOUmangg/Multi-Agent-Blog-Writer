# from langchain_community.tools import DuckDuckGoSearchRun
# from crewai.tools import BaseTool
# from pydantic import BaseModel, Field

# class DuckDuckGoSearchToolSchema(BaseModel):
#     query: str = Field(..., description="The search query to look up on DuckDuckGo.")

# class DuckDuckGoSearchTool(BaseTool):
#     name = "DuckDuckGo Search"
#     description = "Searches DuckDuckGo for relevant information."
#     args_schema = DuckDuckGoSearchToolSchema

#     def _run(self, query: str):
#         search = DuckDuckGoSearchRun()
#         return search.run(query)

from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import ClassVar, Type  # Added for type annotations

class DuckDuckGoSearchToolSchema(BaseModel):
    query: str = Field(..., description="The search query to look up on DuckDuckGo.")

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"  # Added type annotation
    description: str = "Searches DuckDuckGo for relevant information."  # Added type annotation
    args_schema: Type[BaseModel] = DuckDuckGoSearchToolSchema  # Added type annotation

    def _run(self, query: str):
        search = DuckDuckGoSearchRun()
        return search.run(query)
