from pydantic import BaseModel

class RegionRequest(BaseModel):
    #경도
    longitude: float
    #위도
    latitude: float