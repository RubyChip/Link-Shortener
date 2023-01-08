from typing import Any, Dict, Optional
from sqlalchemy import delete, select

from app.models.url import Url


class UrlDal:
    """Data Access Layer class for Url model"""

    @classmethod
    async def get_by_pk(cls, db_session, unique_code) -> Optional[Url]:
        query = select(Url).filter(Url.unique_code == unique_code)
        return (await db_session.execute(query)).scalar()

    @classmethod
    async def create(cls, db_session, data: Dict[str, Any]) -> Url:
        model = Url(
            unique_code=data.get("unique_code"),
            origin_url=data.get("origin_url"),
            created_at=data.get("created_at"),
        )
        db_session.add(model)
        await db_session.commit()
        await db_session.refresh(model)
        return model

    @classmethod
    async def delete(cls, db_session, unique_code) -> Optional[str]:
        query = delete(Url).filter(Url.unique_code == unique_code).returning(Url.unique_code)
        unique_code = (await db_session.execute(query)).scalar()
        await db_session.commit()
        return unique_code
