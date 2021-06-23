"""Pesquisa simplificada do Google - @applled"""

import asyncio
import os
import time
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint
from re import sub
from datetime import datetime

import requests
import wget
from cowpy import cow

from userge import Message, userge
@userge.on_cmd(
    "goo",
    about={
        "header": "Muito fácil usar o Google",
        "usar": "{tr}goo [pesquisar | responder]",
    },
)
async def goo_(message: Message):
    """goo_"""
    query = message.input_or_reply_str
    if not query:
        await message.edit("`Vou pesquisar o vento?!`")
        return
    query_encoded = query.replace(" ", "+")
#   query_encoded = query2.replace(" ", "+")
    goo_url = f"https://www.google.com/search?q={query_encoded}"
#   twt_url = f"https://twitter.com/search?q={query2_encoded}"
    payload = {"format": "json", "url": goo_url}
    r = requests.get("http://is.gd/create.php", params=payload)
    await message.edit(
        f"""
✅ **Este é o resultado da Sua Pesquisa no Google:**
🔗 [{query}]({r.json()['shorturl']})

  ➖➖➖➖
Dev: @applled
"""
    )

