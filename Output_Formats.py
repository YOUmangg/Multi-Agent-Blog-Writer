from pydantic import BaseModel, Field
from typing import List

class SingleImageOutput(BaseModel):
    """
    Represents a single image output with its associated metadata.
    """
    sub_heading: str = Field(..., description="The sub-heading for which the image is generated.")
    image: str = Field(..., description="The URL or path to the generated image.")
    description: str = Field(..., description="A brief description of the image content.")
    tags: List[str] = Field(..., description="Tags associated with the image for better categorization and searchability.")

class Image_output(BaseModel):
    """
    Represents the output format for images generated by the Images Generator agent.
    """
    images: List[SingleImageOutput] = Field(..., description="List of generated images with metadata.")



