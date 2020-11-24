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
    class Config:
        schema_extra = {
            "example": {
                "acousticness": 0.344719513,
                "danceability": 0.758067547,
                "energy": 0.323318405,
                "instrumentalness": 0.0166768347,
                "liveness": 0.0856723112,
                "speechiness": 0.0306624283,
                "tempo": 101.993,
                "valence": 0.443876228 ,
            }
        }
