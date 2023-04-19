from aiogram import Dispatcher

from .group_admin import IsAdmin
from .groups_chat import IsGroup
from .private_chat import IsPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsAdmin)
