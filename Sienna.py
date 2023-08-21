import discord
from discord.ext import commands
import pymysql
import random
import peewee
from peewee import *
from playhouse.shortcuts import ReconnectMixin

class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass

SMOD_DB = ReconnectMySQLDatabase('railway', user='root', password='gjSYlt0AJJiLoEaJPMgr',
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
SMOD_DB.close()

SECO_DB = ReconnectMySQLDatabase('railway', user='root', password='xcoGDuHDzdLRZfOJx7wo',
                         host='containers-us-west-150.railway.app', port=7340)
class Economy(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    amount = BigIntegerField()
    class Meta:
        database = SECO_DB
SECO_DB.connect()
SECO_DB.create_tables([Economy])
SECO_DB.close()

SAR_DB = ReconnectMySQLDatabase('railway', user='root', password='cvoovYtMtOa3uSoGQjvG',
                         host='containers-us-west-196.railway.app', port=7536)
class Raiders(Model):
    user_id = BigIntegerField()
    user_class = CharField(max_length=1)
    class Meta:
        database = SAR_DB
SAR_DB.connect()
SAR_DB.create_tables([Raiders])
SAR_DB.close()

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='S_', intents=intents)
bot.remove_command('help')

cogs_list = [
    'Sienna_mod',
    'Sienna_base_utils',
    'Sienna_fun',
    'Sienna_economy',
    'Sienna_shield'
]
for cog in cogs_list:
    bot.load_extension(f'{cog}')

Token = 'MTEzOTIzNDgyNzcyMDIwODQwNA.GO4VhI.XWRBFPYqpou7aThe84SnsI0YE3dLHQhJpN3FuA'

@bot.before_invoke
async def command_executed(guild):
    if SMOD_DB.is_closed():
        SMOD_DB.connect()
    if SECO_DB.is_closed():
        SECO_DB.connect()

@bot.after_invoke
async def command_after_executed(guild):
    SMOD_DB.close()
    SECO_DB.close()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Im on {len(bot.guilds)} servers! Mrawr!'))

@bot.event
async def on_guild_join(guild):
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Im on {len(bot.guilds)} servers! Mrawr!'))
    user = guild.owner
    greet = discord.Embed(title='Hello there!', colour=0xf1c40f)
    greet.set_thumbnail(url='https://cdn.discordapp.com/avatars/1139234827720208404/b086c35d8039890dcdae4edf97faaba4.png?size=512')
    greet.add_field(name='**Thank you so much for adding me to your server! :3**',
                    value='Execute **/help** command on your server in order to explore all my features! ^w^',
                    inline=False)
    greet.add_field(name='____________________',
                    value='You can join my support server as well, there you will have all your questions answered! :p Have a nice day!',
                    inline=False)
    greet.add_field(name='____________________', value='https://discord.gg/bmmNuUBHVC', inline=False)
    await user.send(embed=greet)

@bot.event
async def on_guild_remove(guild):
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f'Im on {len(bot.guilds)} servers! Mrawr!'))

@bot.event
async def on_member_remove(member):
    getnotif = Notifications.get_or_none(guild_id=member.guild.id)
    if getnotif is None:
        pass
    else:
        for notifications in Notifications.select().where(Notifications.guild_id == member.guild.id):
            channel = bot.get_channel(notifications.channel_id)
            getlang = Language.get_or_none(guild_id=member.guild.id)
            if getlang is None:
                leave = discord.Embed(title='User left server', colour=0xf1c40f)
                leave.set_thumbnail(url=member.avatar)
                leave.add_field(name=f'**User {member.name} has left the server**',
                              value='**__________________**',
                              inline=False)
                await channel.send(embed=leave)
            else:
                for language in Language.select().where(Language.guild_id == member.guild.id):
                    if language.lang == 'en':
                        leave = discord.Embed(title='User left server', colour=0xf1c40f)
                        leave.set_thumbnail(url=member.avatar)
                        leave.add_field(name=f'**User {member.name} has left the server**',
                                      value='**__________________**', inline=False)
                        await channel.send(embed=leave)
                    else:
                        leave = discord.Embed(title='User verließ den Server', colour=0xf1c40f)
                        leave.set_thumbnail(url=member.avatar)
                        leave.add_field(name=f'**User {member.name} hat den Server verlassen**',
                                      value='**__________________**', inline=False)
                        await channel.send(embed=leave)

@bot.event
async def on_member_join(member):
    getnotif = Notifications.get_or_none(guild_id=member.guild.id)
    if getnotif is None:
        pass
    else:
        for notifications in Notifications.select().where(Notifications.guild_id == member.guild.id):
            channel = bot.get_channel(notifications.channel_id)
            getlang = Language.get_or_none(guild_id=member.guild.id)
            if getlang is None:
                leave = discord.Embed(title='User joined server', colour=0xf1c40f)
                leave.set_thumbnail(url=member.avatar)
                leave.add_field(name=f'**User {member.name} has joined the server**',
                              value='**__________________**',
                              inline=False)
                await channel.send(embed=leave)
            else:
                for language in Language.select().where(Language.guild_id == member.guild.id):
                    if language.lang == 'en':
                        leave = discord.Embed(title='User joined server', colour=0xf1c40f)
                        leave.set_thumbnail(url=member.avatar)
                        leave.add_field(name=f'**User {member.name} has joined the server**',
                                      value='**__________________**', inline=False)
                        await channel.send(embed=leave)
                    else:
                        leave = discord.Embed(title='User beitrat den Server', colour=0xf1c40f)
                        leave.set_thumbnail(url=member.avatar)
                        leave.add_field(name=f'**User {member.name} hat den Server beigetretet**',
                                      value='**__________________**', inline=False)
                        await channel.send(embed=leave)

@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            eco = discord.Embed(title='Error!', colour=0xf1c40f)
            eco.add_field(name='Command on cooldown! Retry in 1 hour',
                          value='**__________________**', inline=False)
            await ctx.respond(embed=eco, ephemeral=True)
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                    eco.add_field(name='Command on cooldown! Retry in 1 hour',
                                  value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
                else:
                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                    eco.add_field(
                        name='Befehl bei Abklingzeit! Versuchen Sie es in 1 Stunde noch einmal',
                        value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
    elif isinstance(error, commands.MissingPermissions):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            eco = discord.Embed(title='Error!', colour=0xf1c40f)
            eco.add_field(name='You do not have enough permissions! Contact server owner, if you think this is a mistake',
                          value='**__________________**', inline=False)
            await ctx.respond(embed=eco, ephemeral=True)
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                    eco.add_field(name='You do not have enough permissions! Contact server owner, if you think this is a mistake',
                                  value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
                else:
                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                    eco.add_field(
                        name='Sie haben nicht genügend Berechtigungen! Wenden Sie sich an den Serverbesitzer, wenn Sie glauben, dass dies ein Fehler ist',
                        value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
    elif isinstance(error, commands.BotMissingPermissions):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            eco = discord.Embed(title='Error!', colour=0xf1c40f)
            eco.add_field(name='Bot does not have enough permissions',
                          value='**__________________**', inline=False)
            await ctx.respond(embed=eco, ephemeral=True)
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                    eco.add_field(name='Bot does not have enough permissions',
                                  value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
                else:
                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                    eco.add_field(
                        name='Der Bot verfügt nicht über ausreichende Berechtigungen',
                        value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
    else:
        raise error

bot.run(Token)
