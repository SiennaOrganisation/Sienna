import discord
from discord.ext import commands
import pymysql
import random
import peewee
from peewee import *
import asyncio

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='S_', intents=intents)
bot.remove_command('help')

SMOD_DB = MySQLDatabase('railway', user='root', password='gjSYlt0AJJiLoEaJPMgr',
                         host='containers-us-west-120.railway.app', port=5989)
class Language(Model):
    guild_id = BigIntegerField()
    lang = CharField(max_length=2)
    class Meta:
        database = SMOD_DB
class Notifications(Model):
    guild_id = BigIntegerField()
    channel_id = BigIntegerField()
    class Meta:
        database = SMOD_DB
SMOD_DB.connect()
SMOD_DB.create_tables([Language, Notifications])

SECO_DB = MySQLDatabase('railway', user='root', password='xcoGDuHDzdLRZfOJx7wo',
                         host='containers-us-west-150.railway.app', port=7340)
class Economy(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    amount = BigIntegerField()
    class Meta:
        database = SECO_DB
SECO_DB.connect()
SECO_DB.create_tables([Economy])

cogs_list = [
    'Sienna_mod',
    'Sienna_base_utils',
    'Sienna_fun',
    'Sienna_economy'
]
for cog in cogs_list:
    bot.load_extension(f'{cog}')

bot.run("MTEzOTIzNDgyNzcyMDIwODQwNA.GDiTJW.1doTop_H3cYD8hmeJZ8IYGzO8awko_mG2xs24s")
