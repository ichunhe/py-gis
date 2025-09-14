from sqlalchemy import func
from sqlalchemy.orm import Session
from src.model.entity.admin_region import AdminRegion

def find_region_by_point(lon: float, lat: float, db: Session):
    point = func.ST_SetSRID(func.ST_MakePoint(lon, lat), 4326)

    return (
        db.query(AdminRegion)
        .filter(AdminRegion.boundary.isnot(None))
        .filter(AdminRegion.deep == 2)
        .filter(func.ST_Contains(AdminRegion.boundary, point))
        .order_by(AdminRegion.deep.desc())
        .limit(1)
        .first()
    )