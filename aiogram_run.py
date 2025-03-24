import asyncio

from bot_producer.create_bot import dp, bot
from bot_producer.handlers import get
from bot_producer.handlers.start import start_router


# from create_bot import bot, dp, scheduler
# from handlers import get
# from handlers.start import start_router

# from aiogram import InlineKeyboardButton, KeyboardButton, WebAppInfo

# from work_time.time_func import send_time_msg

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    dp.include_router(get)

    # ...
    # ikb = InlineKeyboardButton("Перейти", web_app=WebAppInfo('https://<your_domain>'))
    # kb = KeyboardButton("Перейти", web_app=WebAppInfo('https://<your_domain>'))


if __name__ == "__main__":
    asyncio.run(main())
