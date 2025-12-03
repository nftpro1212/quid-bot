# Telegram Bot - Har Kunlik Xabar

Bu bot har kuni bir xil vaqtda belgilangan guruhga xabar yuboradi.

## O'rnatish

1. Kerakli kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

2. `.env` faylini yaratish:
```bash
cp .env.example .env
```

3. `.env` faylini tahrirlash va quyidagi ma'lumotlarni kiritish:
   - `BOT_TOKEN`: @BotFather dan olingan bot tokeni
   - `CHAT_ID`: Guruh ID raqami (manfiy son)
   - `SEND_TIME`: Xabar yuborish vaqti (masalan: 09:00)
   - `MESSAGE`: (ixtiyoriy) to'liq matn. Bo'sh bo'lsa INTRO/ITEMS/OUTRO dan xabar tuziladi
   - `MESSAGE_INTRO`: (ixtiyoriy) xabar bosh qismi
   - `MESSAGE_ITEMS`: (ixtiyoriy) ro'yxat bandlari; elementlarni `;` yoki `|` bilan ajrating
   - `MESSAGE_OUTRO`: (ixtiyoriy) yakuniy jumla
   - `MENTION_ALL`: `true` bo'lsa xabar oxirida `@all` qo'shiladi

## Xabar formatlash

- `MESSAGE` to'ldirilsa, u to'liq matn sifatida yuboriladi.
- `MESSAGE` bo'sh bo'lsa, bot quyidagicha xabar tuzadi:
  1. `MESSAGE_INTRO` (agar bo'lsa)
  2. `MESSAGE_ITEMS` dan tartibli ro'yxat
  3. `MESSAGE_OUTRO` (agar bo'lsa)
  4. `@all` (agar `MENTION_ALL=true` bo'lsa)
- `@all` mention barcha guruh a'zolarini xabardor qilish uchun tavsiya etiladi. Bot admin ekanligiga ishonch hosil qiling.

## Bot yaratish

1. Telegram'da @BotFather ga murojaat qiling
2. `/newbot` komandasini yuboring
3. Bot uchun nom va username tanlang
4. Olingan tokenni `.env` fayliga kiriting

## Guruh ID olish

1. Botni guruhga admin sifatida qo'shing
2. @userinfobot ni guruhga qo'shing
3. Guruh ID sini oling (masalan: -1001234567890)
4. ID ni `.env` fayliga kiriting

## Ishga tushirish

```bash
python bot.py
```

Bot doimiy ishlab turadi va har kuni belgilangan vaqtda xabar yuboradi.

## Serverde ishlatish

Botni doimiy ishlatish uchun `screen` yoki `systemd` dan foydalaning:

### Screen bilan:
```bash
screen -S telegram_bot
python bot.py
# Ctrl+A+D ni bosing (detach uchun)
```

### Systemd bilan:
`/etc/systemd/system/telegram-bot.service` faylini yarating va sozlang.

## Xatoliklarni tekshirish

Bot log fayllarini yaratadi. Agar xabar yuborilmasa:
- Bot tokenini tekshiring
- Guruh ID to'g'riligini tekshiring
- Bot guruhda admin ekanligini tekshiring
- Internet ulanishini tekshiring
