import asyncio
import logging
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError
import schedule
import time
import config

# Logging sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot obyekti
bot = Bot(token=config.BOT_TOKEN)


def compose_message() -> str:
    """Xabar matnini sozlamalardan tuzish."""
    lines: list[str] = []

    if config.MESSAGE:
        lines.append(config.MESSAGE.strip())
    else:
        if config.MESSAGE_INTRO:
            lines.append(config.MESSAGE_INTRO.strip())

        for index, item in enumerate(config.MESSAGE_ITEMS, start=1):
            lines.append(f"{index}. {item}")

        if config.MESSAGE_OUTRO:
            lines.append(config.MESSAGE_OUTRO.strip())

    if config.MENTION_ALL:
        lines.append('@all')

    message = '\n'.join(line for line in lines if line)

    if not message:
        raise ValueError('Yuboriladigan xabar matni topilmadi. Sozlamalarni tekshiring.')

    return message


async def send_daily_message():
    """Guruhga kunlik xabar yuborish"""
    try:
        await bot.send_message(
            chat_id=config.CHAT_ID,
            text=compose_message()
        )
        logger.info(f"Xabar muvaffaqiyatli yuborildi: {datetime.now()}")
    except TelegramError as e:
        logger.error(f"Xabar yuborishda xatolik: {e}")
    except Exception as e:
        logger.error(f"Kutilmagan xatolik: {e}")


def schedule_job():
    """Xabar yuborish vazifasini asinxron rejimda bajarish"""
    asyncio.run(send_daily_message())


def main():
    """Asosiy funksiya - botni ishga tushirish"""
    logger.info(f"Bot ishga tushdi. Har kuni soat {config.SEND_TIME} da xabar yuboriladi.")
    logger.info(f"Guruh ID: {config.CHAT_ID}")
    
    # Har kuni belgilangan vaqtda vazifani bajarish
    schedule.every().day.at(config.SEND_TIME).do(schedule_job)
    
    # Birinchi xabarni darhol yuborish (test uchun ixtiyoriy)
    # asyncio.run(send_daily_message())
    
    # Doimiy ishlab turish
    while True:
        schedule.run_pending()
        time.sleep(60)  # Har daqiqada tekshirish


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Bot to'xtatildi.")
    except Exception as e:
        logger.error(f"Dasturda xatolik: {e}")
