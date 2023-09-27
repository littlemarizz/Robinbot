import nextcord as discord
import asyncio
import json
import sqlite3
import datetime
import chat_exporter
import io
import requests
from nextcord.ext import commands
from nextcord import File, ButtonStyle, Embed, Color, SelectOption
from nextcord.ui import Button, View, Select
from cogs.ticket_system import Ticket_System
from cogs.ticket_commands import Ticket_Command
from cogs.application import ApplicationView
from cogs.applications_commands import Application_Command
from nextcord import File, ButtonStyle, Embed, Color, SelectOption
from nextcord.ui import Button, View, Select

#This will get everything from the config.json file
with open("config.json", mode="r") as config_file:
    config = json.load(config_file)

BOT_TOKEN = config["token"]  #Your Bot Token from https://discord.dev
GUILD_ID = config["guild_id"] #Your Server ID aka Guild ID
CATEGORY_ID1 = config["category_id_1"] #Category 1 where the Bot should open the Ticket for the Ticket option 1
CATEGORY_ID2 = config["category_id_2"] #Category 2 where the Bot should open the Ticket for the Ticket option 2

#intents
intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())

bot = commands.Bot(intents=intents.all())

bot = commands.Bot(command_prefix='.',
                   intents=discord.Intents.all(),
                   status=discord.Status.online,
                   activity=discord.Activity(type=discord.ActivityType.watching, name="over the moon")
                   )

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1155578794418126868)
    star = "{ ✧ }"
    embed=discord.Embed(
        title="· ・{ {<:Moon_insignia:1156343361356189716> Welcome to Robin Mains!",
        description=f'> ***"This is the Dreamscape, I am an agent of Watchmaker."***\n\n · · · · · · · · · · · · · · · · ꒰ა { star } ໒꒱ · · · · · · · · · · · · · · · · \n\n > <:Star:1156343147954192546> First off, please take a look at our <#1155578876005728256> channel so you can be familiar with our server expectations. \n > <:Star:1156343147954192546> Next, head over to <1155578913364377660> for some roles to personalize your server profile. \n > <:Star:1156343147954192546> If there are any issues or problems, please feel free to <#1155986648597803049> when needed. \n > <:Star:1156343147954192546> Feel free to head over to the <#1155578893735047188> when getting lost.',
        color=0x9ba2f0,
        )
    embed.set_author(name=member.name, icon_url=member.avatar.url)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1155577204571373658/1156081127086379048/IMG_4101.png?ex=6515a633&is=651454b3&hm=39ad004cfa5165ac11250d1befd29dd04d1b83d91535b0e09ce58ebb5a2fbb2e&')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1155577204571373658/1156334776664461484/IMG_4105.png?ex=651540ee&is=6513ef6e&hm=351b326f1d1323fb51b6501914278745670c62f04c608073acd5b5592c59628a&')
    embed.set_footer(text=f"You are our {member.guild.member_count}th visitor of Penacony!")
    embed.timestamp = datetime.datetime.now()
    await channel.send(content=f"Welcome {member.mention}!", embed=embed)

@bot.event
async def on_ready():
    print(f'Bot Logged | {bot.user.name}')
    print("chicken chicken")

bot.add_cog(Ticket_System(bot))
bot.add_cog(Ticket_Command(bot))
bot.add_cog(Application_Command(bot))
bot.run(BOT_TOKEN)