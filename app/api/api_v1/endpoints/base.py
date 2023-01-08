import validators
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Path, Response
from sqlalchemy.ext.asyncio import AsyncSession


from app.api.dependencies import get_db_session
from app.schemas import OriginUrl, ShortUrl
from app.configs.base import settings
from app.api.services import generate_unique_code
from app.dal import UrlDal

router = APIRouter()


@router.post("/url/create/", response_model=ShortUrl)
async def create_url(origin_url: OriginUrl, db_session: AsyncSession = Depends(get_db_session)) -> Optional[ShortUrl]:
    if not validators.url(origin_url.origin_url):
        raise HTTPException(status_code=400, detail=f"{origin_url.origin_url} is not a valid URL address")

    unique_code_length = settings.UNIQUE_CODE_LENGTH
    unique_code = generate_unique_code(unique_code_length)

    while await UrlDal.get_by_pk(db_session, unique_code):
        unique_code_length += 1
        unique_code = generate_unique_code(unique_code_length)

    url_data = {
        "unique_code": unique_code,
        "origin_url": origin_url.origin_url,
        "created_at": datetime.utcnow(),
    }
    await UrlDal.create(db_session, url_data)

    return ShortUrl(short_url=settings.URL_DOMAIN + unique_code)


@router.post("/url/get/", response_model=OriginUrl)
async def get_url(short_url: ShortUrl, db_session: AsyncSession = Depends(get_db_session)) -> Optional[OriginUrl]:
    if not short_url.short_url.startswith(settings.URL_DOMAIN):
        raise HTTPException(status_code=400, detail=f"{short_url.short_url} has an invalid domain")

    unique_code = short_url.short_url.split("/")[-1]
    if url := await UrlDal.get_by_pk(db_session, unique_code):
        return OriginUrl(origin_url=url.origin_url)
    raise HTTPException(status_code=404, detail=f"Short url - {short_url.short_url} doesn't exist.")


@router.post(
    "/url/delete/",
    responses={204: {"description": "Url is deleted successfully"}, 404: {"description": "Unique code doesn't exist"}},
)
async def delete_url(short_url: ShortUrl, db_session: AsyncSession = Depends(get_db_session)) -> Optional[OriginUrl]:
    if not short_url.short_url.startswith(settings.URL_DOMAIN):
        raise HTTPException(status_code=400, detail=f"{short_url.short_url} has an invalid domain")

    unique_code = short_url.short_url.split("/")[-1]
    if await UrlDal.delete(db_session, unique_code):
        return Response(status_code=204)
    raise HTTPException(status_code=404, detail=f"Short url - {short_url.short_url} doesn't exist.")
