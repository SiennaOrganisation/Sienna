import discord
from discord.ext import commands
import random
import peewee
from peewee import *
from Sienna import Language, Notifications, Warns
from Sienna_mod import SMODSETBACKEN, SMODSETBACKRU

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

    @commands.slash_command(name="warn", description="warn user")
    @commands.has_permissions(administrator=True)
    async def warn(self, ctx, user: discord.Member, *, warn: str, index: int = None):
        if user.id == ctx.author.id:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                error = discord.Embed(title='Error!', colour=0xf1c40f)
                error.add_field(name='**You cant give a warn to yourself!**',
                                value='**__________________**',
                                inline=False)
                await ctx.respond(embed=error, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        error = discord.Embed(title='Error!', colour=0xf1c40f)
                        error.add_field(name='**You cant give a warn to yourself!**',
                                        value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
                    else:
                        error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                        error.add_field(
                            name='**Вы не можете выдать предупреждение себе же!**',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
        else:
            if user.bot:
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is None:
                    error = discord.Embed(title='Error!', colour=0xf1c40f)
                    error.add_field(name='**You cant give a warn to a bot!**',
                                    value='**__________________**',
                                    inline=False)
                    await ctx.respond(embed=error, ephemeral=True)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == 'en':
                            error = discord.Embed(title='Error!', colour=0xf1c40f)
                            error.add_field(name='**You cant give a warn to a bot!**',
                                            value='**__________________**', inline=False)
                            await ctx.respond(embed=error, ephemeral=True)
                        else:
                            error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                            error.add_field(
                                name='**Вы не можете выдать предупреждение боту!**',
                                value='**__________________**', inline=False)
                            await ctx.respond(embed=error, ephemeral=True)
            else:
                new_warn = Warns.create(guild_id=ctx.guild.id, user_id=user.id, warn=warn, index=index)
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is None:
                    warn_emb = discord.Embed(title='User warned', colour=0xf1c40f)
                    warn_emb.add_field(name=f'**User** {user.name}, got warned.',
                                    value=f'**Reason:** {warn}',
                                    inline=False)
                    await ctx.respond(embed=warn_emb, ephemeral=True)
                    channel = await user.create_dm()
                    warn_emb = discord.Embed(title='You got warned', colour=0xf1c40f)
                    warn_emb.add_field(name=f'**Server** {user.guild.name}',
                                       value=f'**Reason:** {warn}', inline=False)
                    await channel.send(embed=warn_emb)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == 'en':
                            warn_emb = discord.Embed(title='User warned', colour=0xf1c40f)
                            warn_emb.add_field(name=f'**User** {user.name}, got warned.',
                                            value=f'**Reason:** {warn}', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
                            channel = await user.create_dm()
                            warn_emb = discord.Embed(title='You got warned', colour=0xf1c40f)
                            warn_emb.add_field(name=f'**Server** {user.guild.name}',
                                               value=f'**Reason:** {warn}', inline=False)
                            await channel.send(embed=warn_emb)
                        else:
                            warn_emb = discord.Embed(title='Пользователь предупрежден', colour=0xf1c40f)
                            warn_emb.add_field(
                                name=f'**Пользователь** {user.name}, был предупрежден.',
                                value=f'**Причина:** {warn}', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
                            channel = await user.create_dm()
                            warn_emb = discord.Embed(title='Вы получили предупреждение', colour=0xf1c40f)
                            warn_emb.add_field(name=f'**Сервер** {user.guild.name}',
                                               value=f'**Причина:** {warn}', inline=False)
                            await channel.send(embed=warn_emb)

    @commands.slash_command(name="warn_list", description="list of all warns")
    @commands.has_permissions(administrator=True)
    async def warn_list(self, ctx, user: discord.Member):
        warns_get = Warns.get_or_none(guild_id=ctx.guild.id, user_id=user.id)
        if warns_get is not None:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                warn_emb = discord.Embed(title=f'**Warns of** {user.name}', colour=0xf1c40f)
                for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                    warn_emb.add_field(name=f'**Warn:** {warns.warn}',
                                       value=f'**Index:** {warns.index}', inline=False)
                    await ctx.respond(embed=warn_emb, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        warn_emb = discord.Embed(title=f'**Warns of** {user.name}', colour=0xf1c40f)
                        for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                            warn_emb.add_field(name=f'**Warn:** {warns.warn}',
                                               value=f'**Index:** {warns.index}', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
                    else:
                        warn_emb = discord.Embed(title=f'**Предупреждения пользователя** {user.name}', colour=0xf1c40f)
                        for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                            warn_emb.add_field(
                                name=f'**Предупреждение:** {warns.warn}',
                                value=f'**Индекс:** {warns.index}', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
        else:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                error = discord.Embed(title='Error!', colour=0xf1c40f)
                error.add_field(name=f'**User {user.name} has no warns**',
                                value='**__________________**',
                                inline=False)
                await ctx.respond(embed=error, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        error = discord.Embed(title='Error!', colour=0xf1c40f)
                        error.add_field(name=f'**User {user.name} has no warns**',
                                        value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
                    else:
                        error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                        error.add_field(
                            name=f'**У пользователя {user.name} нету предупреждений**',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)

    @commands.slash_command(name="pardon", description="Specify warn index to remove one.")
    @commands.has_permissions(administrator=True)
    async def pardon(self, ctx, user: discord.Member, index: int = None):
        warns_get = Warns.get_or_none(guild_id=ctx.guild.id, user_id=user.id)
        if warns_get is not None:
            if index is None:
                for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id):
                    delete = Warns.get(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id)
                    delete.delete_instance()
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is None:
                    warn_emb = discord.Embed(title='Warns removal', colour=0xf1c40f)
                    warn_emb.add_field(name=f'**All warns for {user.name} have been removed**',
                                       value='**__________________**', inline=False)
                    await ctx.respond(embed=warn_emb, ephemeral=True)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == 'en':
                            warn_emb = discord.Embed(title='Warns removal', colour=0xf1c40f)
                            warn_emb.add_field(name=f'**All warns for {user.name} have been removed**',
                                               value='**__________________**', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
                        else:
                            warn_emb = discord.Embed(title='Удаление предупреждений', colour=0xf1c40f)
                            warn_emb.add_field(
                                name=f'**Все предупреждения для {user.name} удалены**',
                                value='**__________________**', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
            else:
                for warns in Warns.select().where(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id,
                                                  Warns.index == index):
                    delete = Warns.get(Warns.guild_id == ctx.guild.id, Warns.user_id == user.id, Warns.index == index)
                    delete.delete_instance()
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is None:
                    warn_emb = discord.Embed(title='Warns removal', colour=0xf1c40f)
                    warn_emb.add_field(name=f'**All warns with index {index} for {user.name} have been removed**',
                                       value='**__________________**', inline=False)
                    await ctx.respond(embed=warn_emb, ephemeral=True)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == 'en':
                            warn_emb = discord.Embed(title='Warns removal', colour=0xf1c40f)
                            warn_emb.add_field(name=f'**All warns with index {index} for {user.name} have been removed**',
                                               value='**__________________**', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
                        else:
                            warn_emb = discord.Embed(title='Удаление предупреждений', colour=0xf1c40f)
                            warn_emb.add_field(
                                name=f'**Все предупреждения с индексом {index} для {user.name} удалены**',
                                value='**__________________**', inline=False)
                            await ctx.respond(embed=warn_emb, ephemeral=True)
        else:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                error = discord.Embed(title='Error!', colour=0xf1c40f)
                error.add_field(name=f'**User {user.name} has no warns**',
                                value='**__________________**',
                                inline=False)
                await ctx.respond(embed=error, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        error = discord.Embed(title='Error!', colour=0xf1c40f)
                        error.add_field(name=f'**User {user.name} has no warns**',
                                        value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
                    else:
                        error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                        error.add_field(
                            name=f'**У пользователя {user.name} нету предупреждений**',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)

def setup(bot):
    bot.add_cog(SBASEUTIL(bot))
