#!usr/bin/env python3
# logger.py
# Author: s0v13tl3mon
# Github: https://github.com/s0v13tl3m0n

import os
from datetime import datetime
import discord
from dotenv import load_dotenv
import io

# grabs server data along with the token required for bot functionality
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# set bot prefix and the intents of the bot, ie- using user messages to generate responses
intents = discord.Intents.all()
bot = discord.Client()


######################################################################################

# runs the startup, lets user know when bot is ready
@bot.event
async def on_ready():
    print('Bot Ready \n')


# message logging (terminal and logs)
@bot.event
async def on_message(message):
    clock = datetime.now()
    clock_format = clock.strftime("%d/%m/%Y %H:%M:%S")

    if message.author == bot.user or message.author.bot or len(message.content) == 0:
        return

    print(f'User Event: Message \n'
          f'Username: {message.author} \n'
          f'Message Content: {message.content} \n'
          f'Message ID: {message.id} \n'
          f'Time: {clock_format} \n')

    with io.open("logs/messages.txt", "a", encoding="utf-8") as f:
        f.write(f'User Event: Message | '
                f'Username: {message.author} | '
                f'Message Content: {message.content} | '
                f'Message ID: {message.id} | '
                f'Time: {clock_format} \n'
                )
        f.close()


# for joins (terminal and logs)
@bot.event
async def on_member_join(member):
    clock = datetime.now()
    clock_format = clock.strftime("%d/%m/%Y %H:%M:%S")

    print(f'User Event: Join \n'
          f'Username: {member} \n'
          f'User ID: {member.id} \n'
          f'Time: {clock_format} \n'
          )
    with io.open("logs/joins.txt", "a", encoding="utf-8") as f:
        f.write(f'User Event: Join | '
                f'Username: {member} | '
                f'User ID: {member.id} | '
                f'Time: {clock_format} \n'
                )
        f.close()


# for leaves (terminal and logs)
@bot.event
async def on_member_remove(member):
    clock = datetime.now()
    clock_format = clock.strftime("%d/%m/%Y %H:%M:%S")

    print(f'User Event: Leave \n'
          f'Username: {member} \n'
          f'User ID: {member.id} \n'
          f'Time: {clock_format} \n'
          )
    with io.open("logs/leaves.txt", "a", encoding="utf-8") as f:
        f.write(f'User Event: Leave | '
                f'Username: {member} | '
                f'User ID: {member.id} | '
                f'Time: {clock_format} \n'
                )
        f.close()


# for deletes (terminal and logs)
@bot.event
async def on_message_delete(message):
    clock = datetime.now()
    clock_format = clock.strftime("%d/%m/%Y %H:%M:%S")

    if message.author == bot.user or message.author.bot or len(message.content) == 0:
        return

    print(f'User Event: Message Delete \n'
          f'Username: {message.author} \n'
          f'Message Content: {message.content} \n'
          f'Message ID: {message.id} \n'
          f'Time: {clock_format} \n')

    with io.open("logs/deletes.txt", "a", encoding="utf-8") as f:
        f.write(f'User Event: Message Delete | '
                f'Username: {message.author} | '
                f'Message Content: {message.content} | '
                f'Message ID: {message.id} | '
                f'Time: {clock_format} \n')
        f.close()


# for edits (terminal and logs)
@bot.event
async def on_message_edit(message_before, message_after):
    clock = datetime.now()
    clock_format = clock.strftime("%d/%m/%Y %H:%M:%S")

    if message_before.author == bot.user or message_before.author.bot or len(message_after.content) == 0 or \
            message_before.content == message_after.content:
        return

    if message_before.author != bot.user or message_before.author.bot or message_before.content == \
            message_after.content:
        print(f'User Event: Message Edit \n'
              f'Username: {message_before.author} \n'
              f'Message Before: {message_before.content} \n'
              f'Message After: {message_after.content} \n'
              f'Message ID: {message_before.id} \n'
              f'Time: {clock_format} \n')

        with io.open("logs/edits.txt", "a", encoding="utf-8") as f:
            f.write(f'User Event: Message Edit | '
                    f'Username: {message_before.author} | '
                    f'Message Before: {message_before.content} | '
                    f'Message After: {message_after.content} | '
                    f'Message ID: {message_before.id} | '
                    f'Time: {clock_format} \n')
            f.close()

bot.run(TOKEN)
