import discord
from discord.ext import commands
import random
import peewee
from peewee import *
from Sienna import Language, Notifications, Raiders

class SARADDEN(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Raider id", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Raider class", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        newraider = Raiders.create(user_id=int(self.children[0].value), user_class=self.children[1].value)
        ar_shield = discord.Embed(title='Raider added', colour=0xf1c40f)
        ar_shield.add_field(name=f'**User {int(self.children[0].value)}, will now be considered as a raider**',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=ar_shield, view=None)

class SARDElEN(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Raider id", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        getraider = Raiders.get_or_none(user_id=int(self.children[0].value))
        if getraider is None:
            error = discord.Embed(title='Error!', colour=0xf1c40f)
            error.add_field(
                name=f'**User {int(self.children[0].value)}, not found!**',
                value='**__________________**', inline=False)
            await interaction.response.send_message(embed=error, ephemeral=True)
        else:
            delete = Raiders.get(Raiders.user_id == int(self.children[0].value))
            delete.delete_instance()
            ar_shield = discord.Embed(title='Raider deleted', colour=0xf1c40f)
            ar_shield.add_field(name=f'**User {int(self.children[0].value)}, will not be considered as a raider anymore**',
                                value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=ar_shield, view=None)

class SARADDRU(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Айди рейдера", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Класс рейдера", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        newraider = Raiders.create(user_id=int(self.children[0].value), user_class=self.children[1].value)
        ar_shield = discord.Embed(title='Рейдер добавлен', colour=0xf1c40f)
        ar_shield.add_field(name=f'**Пользователь {int(self.children[0].value)}, теперь будет восприниматься как рейдер**',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=ar_shield, view=None)

class SARDElRU(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Айди рейдера", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        getraider = Raiders.get_or_none(user_id=int(self.children[0].value))
        if getraider is None:
            error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
            error.add_field(
                name=f'**Пользователь {int(self.children[0].value)}, не найден!**',
                value='**__________________**', inline=False)
            await interaction.response.send_message(embed=error, ephemeral=True)
        else:
            delete = Raiders.get(Raiders.user_id == int(self.children[0].value))
            delete.delete_instance()
            ar_shield = discord.Embed(title='Рейдер удален', colour=0xf1c40f)
            ar_shield.add_field(name=f'**Пользователь {int(self.children[0].value)}, больше не будет восприниматься как рейдер**',
                                value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=ar_shield, view=None)

class SARSELECTEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Add raider", custom_id="1", style=discord.ButtonStyle.blurple)
    async def add_button_callback(self, button, interaction):
        await interaction.response.send_modal(SARADDEN(title='Add raider'))

    @discord.ui.button(label="Remove raider", custom_id="2", style=discord.ButtonStyle.danger)
    async def remove_button_callback(self, button, interaction):
        await interaction.response.send_modal(SARDElEN(title='Remove raider'))

class SARSELECTRU(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Добавить рейдера", custom_id="1", style=discord.ButtonStyle.blurple)
    async def add_button_callback(self, button, interaction):
        await interaction.response.send_modal(SARADDRU(title='Добавить рейдера'))

    @discord.ui.button(label="Удалить рейдера", custom_id="2", style=discord.ButtonStyle.danger)
    async def remove_button_callback(self, button, interaction):
        await interaction.response.send_modal(SARDElRU(title='Удалить рейдера'))

class SAR(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ar_dashboard", description="Dev only")
    async def ar_dashboard(self, ctx):
        if ctx.author.id != 830486806478848040:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                error = discord.Embed(title='Error!', colour=0xf1c40f)
                error.add_field(
                    name='**Only developer team members can execute this command!**',
                    value='**__________________**',
                    inline=False)
                await ctx.respond(embed=error, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        error = discord.Embed(title='Error!', colour=0xf1c40f)
                        error.add_field(
                            name='**Only developer team members can execute this command!**',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
                    else:
                        error = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                        error.add_field(
                            name='**Только разработчикам доступна эта команда!**',
                            value='**__________________**', inline=False)
                        await ctx.respond(embed=error, ephemeral=True)
        else:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                ar_shield = discord.Embed(title='AR_Dashboard', colour=0xf1c40f)
                ar_shield.add_field(name='**Here you can modify all AR functions available**',
                                   value='**__________________**', inline=False)
                ar_shield.add_field(name='In order to select a function click needed button below',
                                   value='**__________________**', inline=False)
                await ctx.respond(embed=ar_shield, view=SARSELECTEN(), ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        ar_shield = discord.Embed(title='AR_Dashboard', colour=0xf1c40f)
                        ar_shield.add_field(name='**Here you can modify all AR functions available**',
                                           value='**__________________**', inline=False)
                        ar_shield.add_field(name='In order to do so, just click the needed button below!',
                                           value='**__________________**', inline=False)
                        await ctx.respond(embed=ar_shield, view=SARSELECTEN(), ephemeral=True)
                    else:
                        ar_shield = discord.Embed(title='Антирейд панель', colour=0xf1c40f)
                        ar_shield.add_field(name='**Здесь вы можете настраивать все функции антирейда**',
                                           value='**__________________**', inline=False)
                        ar_shield.add_field(name='Для этого просто нажмите на соответствующую кнопку ниже!',
                                           value='**__________________**', inline=False)
                        await ctx.respond(embed=ar_shield, view=SARSELECTRU(), ephemeral=True)

def setup(bot):
    bot.add_cog(SAR(bot))
