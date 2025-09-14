from sqlalchemy.orm import Session
from src.repository.region_repository import find_region_by_point
from src.dto.region.region_dto import RegionResponse

def get_region(lon: float, lat: float, db: Session) -> RegionResponse | None:
    region = find_region_by_point(lon, lat, db)
    if region:
        return RegionResponse.from_orm(region)
    return None
