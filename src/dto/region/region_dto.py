from pydantic import BaseModel

class RegionResponse(BaseModel):
    id: str
    name: str
    deep: int
    ext_path: str | None

    class Config:
        from_attributes  = True