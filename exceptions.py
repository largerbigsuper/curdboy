from typing import Any, Dict, Optional
from fastapi import HTTPException


class ObjectNotFoundException(HTTPException):

    def __init__(self, status_code: int, detail: Any = None, headers: Dict[str, str] | None = None) -> None:
        super().__init__(status_code, detail, headers)