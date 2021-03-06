from math import ceil
import asyncio
import json
import random
import re
from telethon.tl.custom import Button 
from telethon import events, errors, custom
from userbot import CMD_LIST
import io


if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back"))) #https://t.me/pldhsys/372
   
    async def backr(event):
            if event.query.user_id == bot.uid :
                current_page_number=0
                buttons = paginate_help(current_page_number, CMD_LIST, "helpme")
                await event.edit("📜Userbot Helper to reveal all the commands📜\n\n🔥This is main menu....🔥", buttons=buttons)
            else:
                reply_pop_up_alert = "Kya daba rha h bsdk... Jake apna khudka bot bna mera use naa kar....😏 @teamishere"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
   
    async def opner(event):
            if event.query.user_id == bot.uid :
                current_page_number=0
                buttons = paginate_help(current_page_number, CMD_LIST, "helpme")
                await event.edit("📜Userbot Helper to reveal all the commands📜\n\n🔥You opened the menu again🔥", buttons=buttons)
            else:
                reply_pop_up_alert = "Kya daba rha h bsdk... Jake apna khudka bot bna mera use naa kar....😏 NEXTRON!!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
               #https://t.me/pldhsys/372

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article("© Userbot Help",text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),buttons=buttons,link_preview=False)
            await event.answer([result] if result else None)
        else:
              reply_pop_up_alert = "Kya daba rha h bsdk... Jake apna khudka bot bna mera use naa kar....😏 NEXTRON!!"
              await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            buttons = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Kya daba rha h bsdk... Jake apna khudka bot bna mera use naa kar....😏 NEXTRON!!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            buttons = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Kya daba rha h bsdk... Jake apna khudka bot bna mera use naa kar....😏 NEXTRON!!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            hellbot = custom.Button.inline("🔹 Open Again 🔸", data="open")
            await event.edit("🚨 Closed Userbot Helper Main menu 🚨", buttons=hellbot)
            
  #https://t.me/pldhsys/372

    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_plugin_(.*)")
    ))
    async def on_plug_in_callback_query_handler(event):
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = ""
        try:
            for i in CMD_LIST[plugin_name]:
                help_string += i
                help_string += "\n"
        except:
            pass
        if help_string is "":
            reply_pop_up_alert = "{} is useless".format(plugin_name)
        else:
            reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
            © NEXTRON".format(plugin_name)
        try:
            #hellbot = [[Button.inline('Go back', 'back')]] 
            if event.query.user_id == bot.uid :
                hellbot = custom.Button.inline("⚜️ Back To Menu ⚜️", data="back")
                await event.edit(reply_pop_up_alert, buttons=hellbot)
            else:
                reply_pop_up_alert = "Kya daba rha h bsdk... Jake apna khudka bot bna mera use naa kar.... NEXTRON!!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        except: 
            kraken = "Do .help {} to get the list of commands.".format(plugin_name)
            await event.edit(kraken)

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    multi = Config.EMOJI_TO_DISPLAY_IN_HELP
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {}".format(random.choice(list(multi)), x, random.choice(list(multi))),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("• 👈 •", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("• 🙏 •", data="close"),
             custom.Button.inline("• 👉 •", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs
