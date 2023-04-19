from sqlalchemy import Column, sql, VARCHAR, TEXT, INTEGER

from utils.db_api.db_gino import TimedBaseModel


class Offer(TimedBaseModel):
    __tablename__ = 'offer'
    id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(255))
    text = Column(TEXT)
    url = Column(VARCHAR(255))
    top = Column(INTEGER, nullable=False, default=0)
    image = Column(VARCHAR(255))

    query: sql.select
