import random

from telegram import ParseMode
from telethon import Button

from Natsunagi import OWNER_ID, SUPPORT_CHAT
from Natsunagi import telethn as tbot

from ..events import register


@register(pattern="/feedback ?(.*)")
async def feedback(e):
    quew = e.pattern_match.group(1)
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    NATSUNAGI = (
        "https://telegra.ph/file/753bfe51f0e0314f1f3ff.jpg",
        "https://telegra.ph/file/20bab4a499d6dccd823f1.jpg",
        "https://telegra.ph/file/2ef1c255ac51d9febb3f4.jpg",
        "https://telegra.ph/file/bc3a10df7c66e6333bba6.jpg",
        "https://telegra.ph/file/bf283996f928a6ab5b625.jpg",
        "https://telegra.ph/file/bf283996f928a6ab5b625.jpg",
        "https://telegra.ph/file/43b4f5a5645ab1cd1dd7c.jpg",
        "https://telegra.ph/file/0f5240ad4d50d5dac57fe.jpg",
        "https://telegra.ph/file/f6128a7a197cf088ba5e0.jpg",
        "https://telegra.ph/file/53d0320dcaa0d21da19c0.jpg",
        "https://telegra.ph/file/fc988e9441acfb5fe71a7.jpg",
        "https://telegra.ph/file/731387573fd96e3cfc2f5.jpg",
        "https://telegra.ph/file/6c9951e14cece66f2fc3a.jpg",
    )
    BUTTON = [[Button.url("Go To Support Group", f"https://t.me/{SUPPORT_CHAT}")]]
    TEXT = "Thanks For Your Feedback, I Hope You Happy With Our Service"
    logger_text = f"""
**New Feedback**

**From User:** {mention}
**Username:** @{e.sender.username}
**User ID:** `{e.sender.id}`
**Feedback:** `{e.text}`
"""
    if e.sender_id != OWNER_ID and not quew:
        NATFEED = ("https://telegra.ph/file/2dd04f407b16bc2cfdf76.jpg",)
        GIVE = "Give Some Text For Feedback ✨"
        await e.reply(
            GIVE,
            parse_mode=ParseMode.MARKDOWN,
            buttons=BUTTON,
            file=random.choice(NATFEED),
        ),
        return

    await tbot.send_message(
        SUPPORT_CHAT,
        f"{logger_text}",
        file=random.choice(NATSUNAGI),
        link_preview=False,
    )
    await e.reply(TEXT, file=random.choice(NATSUNAGI), buttons=BUTTON)
