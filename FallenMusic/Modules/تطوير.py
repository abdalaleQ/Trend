import asyncio
import random
import os
import time
import requests
from random import  choice, randint
from pyrogram import Client, filters
from FallenMusic.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from FallenMusic import app


@app.on_message(
    command(["سورس","السورس","المطور"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ff4448ad2c768f94cb77c.jpg",
        caption=f"""-| مطور السورس \n-| قناة المطور""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور السورس .", url=f"https://t.me/T_5_G"),
                ],
                [
                   InlineKeyboardButton(
                        "- قناة المطور ", url=f"https://t.me/VVV5P"),
                ],       
            ]
        ),
    )

