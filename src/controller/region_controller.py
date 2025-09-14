from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.dependencies.auth import get_current_user
from src.dto.common.response_dto import ResponseDTO
from src.dto.region.region_request import RegionRequest
from src.service.region_service import get_region
from src.dto.region.region_dto import RegionResponse

router = APIRouter(prefix="/regions", tags=["Regions"])

@router.post("/search", response_model=ResponseDTO)
def search_region(region_request: RegionRequest, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    try:
        region = get_region(region_request.longitude, region_request.latitude, db)
        if region:
            return ResponseDTO.success_response(region)
        else:
            return ResponseDTO.error_response("지역을 찾을 수 없습니다", 404)
    except Exception as e:
        return ResponseDTO.error_response(str(e), 500)