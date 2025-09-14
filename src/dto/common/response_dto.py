from pydantic import BaseModel
from typing import Any


class ResponseDTO(BaseModel):
    success: bool
    data: Any = None
    msg: str | None = None
    code: int | None = None

    @staticmethod
    def success_response(data: Any) -> "ResponseDTO":
        return ResponseDTO(success=True, data=data, msg=None, code=None)

    @staticmethod
    def error_response(msg: str, code: int = 500) -> "ResponseDTO":
        return ResponseDTO(success=False, data=None, msg=msg, code=code)