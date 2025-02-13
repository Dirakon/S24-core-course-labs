from datetime import datetime

from fastapi import APIRouter, Depends
from services.time import get_time_in_msk
from pydantic import BaseModel

router = APIRouter(
    prefix="/time",
    tags=["time"])


class CurrentTimeResponse(BaseModel):
    current_time: datetime


@router.get(
    path="/msk",
    responses={200: {"description": "Success"}})
def get_current_time_in_msk_timezone(current_time_in_msk: datetime = Depends(get_time_in_msk)) -> CurrentTimeResponse:
    return CurrentTimeResponse(current_time=current_time_in_msk)
