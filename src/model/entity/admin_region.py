from sqlmodel import SQLModel, Field, Column
from geoalchemy2 import Geometry

class AdminRegion(SQLModel, table=True):
    __tablename__ = "admin_regions"

    id: str = Field(primary_key=True)
    name: str
    deep: int
    ext_path: str | None = None

    boundary: str = Field(sa_column=Geometry(geometry_type="POLYGON", srid=4326))
