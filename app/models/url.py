import sqlalchemy as sa

from app.db.base import Base


class Url(Base):
    __tablename__ = "url"

    unique_code = sa.Column(sa.String, primary_key=True)
    origin_url = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime)
