import discord
from discord.ext import commands
import pymysql
import random
import peewee
from peewee import *
from playhouse.shortcuts import ReconnectMixin

class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass

SMOD_DB = ReconnectMySQLDatabase('railway', user='root', password='GBaE63cGcHD-Ea6CC-c-BeDbhF1HB5Fh',
                         host='monorail.proxy.rlwy.net', port=10983)
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
class Warns(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    warn = CharField(max_length=200)
    index = BigIntegerField()
    class Meta:
        database = SMOD_DB
SMOD_DB.connect()
SMOD_DB.create_tables([Language, Notifications, Warns])
SMOD_DB.close()

SECO_DB = ReconnectMySQLDatabase('railway', user='root', password='62bE-HDGB3-6-H-c2B41Ccefh-Ha4c6a',
                         host='monorail.proxy.rlwy.net', port=19068)
class Economy(Model):
    guild_id = BigIntegerField()
    user_id = BigIntegerField()
    amount = BigIntegerField()
    class Meta:
        database = SECO_DB
SECO_DB.connect()
SECO_DB.create_tables([Economy])
SECO_DB.close()

SAR_DB = ReconnectMySQLDatabase('railway', user='root', password='-24e4CHAFC2GEhc-GEDhgHAGb5E1aFf6',
                         host='viaduct.proxy.rlwy.nett', port=39236)
class Raiders(Model):
    user_id = BigIntegerField()
    user_class = CharField(max_length=1)
    class Meta:
        database = SAR_DB
class Actions(Model):
    guild_id = BigIntegerField()
    action = CharField(max_length=4)
    class Meta:
        database = SAR_DB
SAR_DB.connect()
SAR_DB.create_tables([Raiders, Actions])
SAR_DB.close()

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='S_', intents=intents)
bot.remove_command('help')

cogs_list = [
    'Sienna_mod',
    'Sienna_base_utils',
    'Sienna_fun',
    'Sienna_economy',
    'Sienna_shield',
]
for cog in cogs_list:
    bot.load_extension(f'{cog}')

Token = 'MTEzOTIzNDgyNzcyMDIwODQwNA.G0C9cp.PB38an6L5CpzIgqmHL--Cu2rLicK3mcyTDUs4g'

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
                        leave = discord.Embed(title='Пользователь покинул сервер', colour=0xf1c40f)
                        leave.set_thumbnail(url=member.avatar)
                        leave.add_field(name=f'**Пользователь {member.name} покинул сервер**',
                                      value='**__________________**', inline=False)
                        await channel.send(embed=leave)

@bot.event
async def on_member_join(member):
    getraid = Raiders.get_or_none(user_id=member.id)
    if getraid is None:
        israider = 'False'
    else:
        israider = 'True'
        getaction = Actions.get_or_none(guild_id=member.guild.id)
        if getaction is None:
            isspecified = 'None'
        else:
            for actions in Actions.select().where(Actions.guild_id == member.guild.id):
                if actions.action == 'ban':
                    await member.ban(reason='Raider')
                    isspecified = 'Ban'
                elif actions.action == 'kick':
                    await member.kick(reason='Raider')
                    isspecified = 'Kick'
                else:
                    isspecified = 'None'
    getnotif = Notifications.get_or_none(guild_id=member.guild.id)
    if getnotif is None:
        pass
    else:
        for notifications in Notifications.select().where(Notifications.guild_id == member.guild.id):
            channel = bot.get_channel(notifications.channel_id)
            getlang = Language.get_or_none(guild_id=member.guild.id)
            if getlang is None:
                join = discord.Embed(title='User joined server', colour=0xf1c40f)
                join.set_thumbnail(url=member.avatar)
                join.add_field(name=f'**User {member.name} has joined the server**',
                              value='**__________________**',
                              inline=False)
                if israider == "True":
                    join.add_field(name='**This user is a raider!**',
                                   value='**__________________**',
                                   inline=False)
                    join.add_field(name='**Specified action against raiders:**',
                                   value=f'```{isspecified}```',
                                   inline=False)
                else:
                    pass
                await channel.send(embed=join)
            else:
                for language in Language.select().where(Language.guild_id == member.guild.id):
                    if language.lang == 'en':
                        join = discord.Embed(title='User joined server', colour=0xf1c40f)
                        join.set_thumbnail(url=member.avatar)
                        join.add_field(name=f'**User {member.name} has joined the server**',
                                      value='**__________________**', inline=False)
                        if israider == "True":
                            join.add_field(name='**This user is a raider!**',
                                           value='**__________________**',
                                           inline=False)
                            join.add_field(name='**Specified action against raiders:**',
                                           value=f'```{isspecified}```',
                                           inline=False)
                        else:
                            pass
                        await channel.send(embed=join)
                    else:
                        join = discord.Embed(title='Новый пользователь присоединился', colour=0xf1c40f)
                        join.set_thumbnail(url=member.avatar)
                        join.add_field(name=f'**Пользователь {member.name} присоединился**',
                                      value='**__________________**', inline=False)
                        if israider == "True":
                            join.add_field(name='**Пользователь является рейдером!**',
                                           value='**__________________**',
                                           inline=False)
                            join.add_field(name='** Установленные действия против рейдеров:**',
                                           value=f'```{isspecified}```',
                                           inline=False)
                        else:
                            pass
                        await channel.send(embed=join)

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
                        name='У этой команды кулдаун! Попробуйте снова через 1 час',
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
                        name='У вас недостаточно разрешений! Если вы считаете, что это ошибка, свяжитесь с владельцем сервера.',
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
                        name='У бота недостаточно прав',
                        value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
    else:
        raise error

bot.run(Token)
