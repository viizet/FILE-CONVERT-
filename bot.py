import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6316830758:AAHcobXnj1F06usLBpNw7YqKnBTqwaUnBuU")

API_ID = int(os.environ.get("API_ID", "26176218"))

API_HASH = os.environ.get("API_HASH", "4a50bc8acb0169930f5914eb88091736")

STRING = os.environ.get("STRING", "BAGPatoAOj_nxBZo06MhTJMT0TrQAmN7_6shpq1nKbrf9iszrKTY6AXFwZ7Oy-47NEVMt2x93e7PXgHPCZKiI6Retmmi2VcHOSsmX5Z60lC3w3ZPtFYS10wKErbTy-rEiaiUIUhtvTg79xps0ZvGBEJk5rjgyu4hG3OPhQIwJCqKFJJRE7XFaZLzvoQ64oEgDNW-eN3nibsXAc7wItZEYRn1WmHwKn51TuaQ3ko6IJgvFtA0VAqeQGgWbtqB5zv6IT-gppOqF_S7S5OtaxyCT8_Zlg1OSF5pFECknYvW4BE2sARBR49EV9YndWLsKF9sX7UnWJl8mZSiyQEvDYm7abnCGhenCwAAAABBXjeKAA")


bot = Client(

           "Rename",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
