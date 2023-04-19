from sqlalchemy import Column, sql, VARCHAR, TEXT, INTEGER

from utils.db_api.db_gino import TimedBaseModel


class Card(TimedBaseModel):
    __tablename__ = 'card'
    id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(255))
    text = Column(TEXT)
    url = Column(VARCHAR(255))
    top = Column(INTEGER, nullable=False, default=0)
    image = Column(VARCHAR(255), )
    active = Column(INTEGER, default=1)

    query: sql.select
