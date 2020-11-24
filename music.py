from pydantic import BaseModel, Field


class Music(BaseModel):
    acousticness: float = Field(..., description="Here is the description of the input to be sent")
    danceability: float = Field(..., description="Here is the description of the input to be sent")
    energy: float = Field(..., description="Here is the description of the input to be sent")
    instrumentalness: float = Field(..., description="Here is the description of the input to be sent")
    liveness: float = Field(..., description="Here is the description of the input to be sent")
    speechiness: float = Field(..., description="Here is the description of the input to be sent")
    tempo: float = Field(..., description="Here is the description of the input to be sent")
    valence: float = Field(..., description="Here is the description of the input to be sent")
