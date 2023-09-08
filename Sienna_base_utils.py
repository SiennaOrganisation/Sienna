import discord
from discord.ext import commands
import random
import peewee
from peewee import *
from Sienna import Language, Notifications
from Sienna_mod import SMODSETBACKEN, SMODSETBACKDE

class SBASEUTIL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban", description="ban specified user")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason):
        await user.ban(reason=reason)
        getnotif = Notifications.get_or_none(guild_id=ctx.guild.id)
        if getnotif is None:
            NSTATS = 'on'
        else:
            NSTATS = 'none'
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            ban = discord.Embed(title='User banned', colour=0xf1c40f)
            ban.add_field(name=f'**User {user.name} has been banned by {ctx.author.name}**',
                          value='**__________________**',
                          inline=False)
            if NSTATS == 'on':
                ban.add_field(
                    name='If you want to set separate channel for notifications type click **Dashboard** below',
                    value='**__________________**', inline=False)
                await ctx.respond(embed=ban, view=SMODSETBACKEN())
            else:
                await ctx.respond(embed=ban)
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    ban = discord.Embed(title='User banned', colour=0xf1c40f)
                    ban.add_field(name=f'**User {user.name} has been banned by {ctx.author.name}**',
                                  value='**__________________**', inline=False)
                    if NSTATS == 'on':
                        ban.add_field(
                            name='If you want to set separate channel for notifications type click **Dashboard** below',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=ban, view=SMODSETBACKEN())
                    else:
                        await ctx.respond(embed=ban)
                else:
                    ban = discord.Embed(title='Пользователь забанен', colour=0xf1c40f)
                    ban.add_field(name=f'**Пользователь {user.name} был забанен по команде {ctx.author.name}**',
                                  value='**__________________**', inline=False)
                    if NSTATS == 'on':
                        ban.add_field(
                            name='Если вы хотите установить отдельный канал для уведомлений, нажмите **Панель управления** ниже',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=ban, view=SMODSETBACKDE())
                    else:
                        await ctx.respond(embed=ban)

    @commands.slash_command(name="kick", description="kicks specified user")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, reason):
        await user.kick(reason=reason)
        getnotif = Notifications.get_or_none(guild_id=ctx.guild.id)
        if getnotif is None:
            NSTATS = 'on'
        else:
            NSTATS = 'none'
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            kick = discord.Embed(title='User kicked', colour=0xf1c40f)
            kick.add_field(name=f'**User {user.name} has been kicked by {ctx.author.name}**',
                          value='**__________________**',
                          inline=False)
            if NSTATS == 'on':
                kick.add_field(
                    name='If you want to set separate channel for notifications type click **Dashboard** below',
                    value='**__________________**', inline=False)
                await ctx.respond(embed=kick, view=SMODSETBACKEN())
            else:
                await ctx.respond(embed=kick)
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    kick = discord.Embed(title='User kicked', colour=0xf1c40f)
                    kick.add_field(name=f'**User {user.name} has been kicked by {ctx.author.name}**',
                                  value='**__________________**', inline=False)
                    if NSTATS == 'on':
                        kick.add_field(
                            name='If you want to set separate channel for notifications type click **Dashboard** below',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=kick, view=SMODSETBACKEN())
                    else:
                        await ctx.respond(embed=kick)
                else:
                    kick = discord.Embed(title='Пользователь кикнут', colour=0xf1c40f)
                    kick.add_field(name=f'**Пользователь {user.name} кикнут по команде {ctx.author.name}**',
                                  value='**__________________**', inline=False)
                    if NSTATS == 'on':
                        kick.add_field(
                            name='Если вы хотите установить отдельный канал для уведомлений, нажмите **Панель управления** ниже',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=kick, view=SMODSETBACKDE())
                    else:
                        await ctx.respond(embed=kick)

    @commands.slash_command(name="clear", description="clear the channel")
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx, amount: int):
        if amount < 0:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                error = discord.Embed(title='Error!', colour=0xf1c40f)
                error.add_field(name=f'**Only positive amounts can be specified! You entered:** ```{amount}```',
                               value='**__________________**',
                               inline=False)
                await ctx.respond(embed=error, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        error = discord.Embed(title='Error!', colour=0xf1c40f)
                        error.add_field(name=f'**Only positive amounts can be specified! You entered:** ```{amount}```',
                                       value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
                    else:
                        error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                        error.add_field(name=f'**Можно указывать только положительную сумму! Вы указали:** ```{amount}```',
                                       value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
        else:
            if amount > 300:
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is None:
                    error = discord.Embed(title='Error!', colour=0xf1c40f)
                    error.add_field(name=f'**You can not delete more than 300 messages at once! You entered:** ```{amount}```',
                                    value='**__________________**',
                                    inline=False)
                    await ctx.respond(embed=error, ephemeral=True)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == 'en':
                            error = discord.Embed(title='Error!', colour=0xf1c40f)
                            error.add_field(
                                name=f'**You can not delete more than 300 messages at once! You entered:** ```{amount}```',
                                value='**__________________**', inline=False)
                            await ctx.respond(embed=error, ephemeral=True)
                        else:
                            error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                            error.add_field(
                                name=f'**Вы не можете удалять белее чем 300 сообщений за раз! Вы указали:** ```{amount}```',
                                value='**__________________**', inline=False)
                            await ctx.respond(embed=error, ephemeral=True)
            else:
                await ctx.channel.purge(limit=amount)
                getnotif = Notifications.get_or_none(guild_id=ctx.guild.id)
                if getnotif is None:
                    NSTATS = 'on'
                else:
                    NSTATS = 'none'
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is None:
                    clear = discord.Embed(title='Messages deleted', colour=0xf1c40f)
                    clear.add_field(name=f'**User {ctx.author.name} has deleted {amount} messages in channel {ctx.channel}**',
                                   value='**__________________**',
                                   inline=False)
                    if NSTATS == 'on':
                        clear.add_field(
                            name='If you want to set separate channel for notifications type click **Dashboard** below',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=clear, view=SMODSETBACKEN())
                    else:
                        await ctx.respond(embed=clear)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == 'en':
                            clear = discord.Embed(title='Messages deleted', colour=0xf1c40f)
                            clear.add_field(name=f'**User {ctx.author.name} has deleted {amount} messages in channel {ctx.channel}**',
                                           value='**__________________**', inline=False)
                            if NSTATS == 'on':
                                clear.add_field(
                                    name='If you want to set separate channel for notifications type click **Dashboard** below',
                                    value='**__________________**', inline=False)
                                await ctx.respond(embed=clear, view=SMODSETBACKEN())
                            else:
                                await ctx.respond(embed=clear)
                        else:
                            clear = discord.Embed(title='Сообщения удалены', colour=0xf1c40f)
                            clear.add_field(name=f'**Пользователь {ctx.author.name} удалил {amount} сообщений в канале {ctx.channel}**',
                                           value='**__________________**', inline=False)
                            if NSTATS == 'on':
                                clear.add_field(
                                    name='Если вы хотите установить отдельный канал для уведомлений, нажмите **Панель управления** ниже',
                                    value='**__________________**', inline=False)
                                await ctx.respond(embed=clear, view=SMODSETBACKDE())
                            else:
                                await ctx.respond(embed=clear)

def setup(bot):
    bot.add_cog(SBASEUTIL(bot))