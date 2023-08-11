import discord
from discord.ext import commands
import pymysql
import random
import peewee
from peewee import *

Token = 'MTEzOTIzNDgyNzcyMDIwODQwNA.G9BkAS.c1jAB84NeJqVgjJuIEBSPkSwrDpaVmOCj9ug70'
Streaming = 'Mrawr!'

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='S_', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=Streaming))

SMOD_DB = MySQLDatabase('railway', user='root', password='gjSYlt0AJJiLoEaJPMgr',
                         host='containers-us-west-120.railway.app', port=5989)
class Language(Model):
    guild_id = BigIntegerField()
    lang = CharField(max_length=2)
    class Meta:
        database = SMOD_DB
SMOD_DB.connect()
SMOD_DB.create_tables([Language])
class Notifications(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()
    class Meta:
        database = SMOD_DB
SMOD_DB.connect()
SMOD_DB.create_tables([Language, Notifications])

cogs_list = [
    'Sienna_mod',
    'Sienna_base_utils'
]
for cog in cogs_list:
    bot.load_extension(f'{cog}')

bot.run(Token)
