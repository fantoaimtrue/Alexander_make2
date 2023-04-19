from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.card import Card
from utils.db_api.schemas.offer import Offer
from utils.db_api.schemas.user import User


# Add
async def add_user(user_id: int, username: str, last_name: str, first_name: str,
                   status: str):
    try:
        user = User(user_id=user_id, username=username, last_name=last_name,
                    first_name=first_name, status=status)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def add_info(ide: int, title: str, text: str, url: str,
                   top: str, image: str):
    try:
        db.Unicode()
        offer = Offer(id=ide, title=title, text=text, url=url, top=top,
                      image=image)
        await offer.create()
    except UniqueViolationError:
        print('Данные не добавлены')


async def add_card(ide: int, title: str, text: str, url: str,
                   top: str, image: str, active: int):
    try:
        card = Card(id=ide, title=title, text=text, url=url, top=top,
                    image=image, active=active)
        await card.create()
    except UniqueViolationError:
        print("Данные не добавлены")


# Count
async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


# SELECT
async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_users(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def select_table_all():
    table = await Offer.select("id", "title", "text", "url", "top", "image"). \
        gino.all()
    return table


async def select_table_9(offset):
    table = await Offer.select("id", "title", "text", "url", "top", "image"). \
        where(Offer.id > offset).limit(9).gino.all()
    return table


async def select_offer(offer_data):
    offer = await Offer.select("id", "title", "text", "url", "top", "image"). \
        where(Offer.id == offer_data).gino.one()
    return offer


async def select_card_all():
    card = await Card.select("id", "title", "text", "url", "top",
                             "image").gino.all()
    return card


async def select_count():
    count = await Offer.select('id').gino.all()
    return len(count)


async def count_card():
    count = await Card.select('id').gino.all()
    return len(count)


async def select_card_9(offset):
    card = await Offer.select("id", "title", "text", "url", "top", "image"). \
        where(Offer.id > offset).limit(9).gino.all()
    return card


async def select_top_5():
    top = await Offer.select("id", "title", "text", "url", "top", "image") \
        .where(Offer.top == 1).limit(5).gino.all()
    return top
