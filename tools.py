from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import ClassVar, Type  # Added for type annotations
from together import Together


class DuckDuckGoSearchToolSchema(BaseModel):
    '''Schema for DuckDuckGo Search Tool arguments.'''
    query: str = Field(..., description="The search query to look up on DuckDuckGo.")

class DuckDuckGoSearchTool(BaseTool):
    name: str = "DuckDuckGo Search"  # Added type annotation
    description: str = "Searches DuckDuckGo for relevant information."  # Added type annotation
    args_schema: Type[BaseModel] = DuckDuckGoSearchToolSchema  # Added type annotation

    def _run(self, query: str):
        search = DuckDuckGoSearchRun()
        return search.run(query)
    
class ImageGenerationToolSchema(BaseModel):
    sub_heading: str = Field(..., description="The sub-heading for which the image is generated.")
    content: str = Field(..., description="The content based on which the image is generated.")

class ImageGenerationTool(BaseTool):
    name: str = "Image Generation Tool"  # Added type annotation
    description: str = "Generates images based on the provided sub-heading and content."  # Added type annotation
    args_schema: Type[BaseModel] = ImageGenerationToolSchema  # Added type annotation

    def _run(self, sub_heading: str, content: str):
        # black-forest-labs/FLUX.1-schnell-Free 
        client = Together()
        response = client.images.generate(
            prompt = "Generate an image for the sub-heading: " + sub_heading +
                     " with the following content: " + content,
            model = "black-forest-labs/FLUX.1-schnell-Free",  # Specify the model to use
            n = 1,
            steps = 2
        )
        return response.data[0].b64_json


        return f"Image generated for sub-heading '{sub_heading}' with content '{content}'."
