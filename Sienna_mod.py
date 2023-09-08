import discord
from discord.ext import commands
import random
import peewee
from peewee import *
from Sienna import Language, Notifications, Actions, bot

class SMODNOTIFEN(discord.ui.View):
    @discord.ui.select(
        placeholder="Channel selection",
        min_values=1,
        max_values=1,
        select_type=discord.ComponentType.channel_select
    )
    async def select_callback(self, select, interaction):
        getnotif = Notifications.get_or_none(guild_id=interaction.guild_id)
        if getnotif is None:
            pass
        else:
            delete = Notifications.get(Notifications.guild_id == interaction.guild_id)
            delete.delete_instance()
        Newnotification = Notifications.create(guild_id=interaction.guild_id, channel_id=select.values[0].id)
        settings = discord.Embed(title='Channel selection', colour=0xf1c40f)
        settings.add_field(name=f'**Channel for all notifications:** ```{select.values[0]}```', value='**__________________**',
                           inline=False)
        settings.add_field(name='Return to dashboard by clicking **Dashboard** below',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=SMODSETBACKEN())

class SMODNOTIFRU(discord.ui.View):
    @discord.ui.select(
        placeholder="Выбор канала",
        min_values=1,
        max_values=1,
        select_type=discord.ComponentType.channel_select
    )
    async def select_callback(self, select, interaction):
        getnotif = Notifications.get_or_none(guild_id=interaction.guild_id)
        if getnotif is None:
            pass
        else:
            delete = Notifications.get(Notifications.guild_id == interaction.guild_id)
            delete.delete_instance()
        Newnotification = Notifications.create(guild_id=interaction.guild_id, channel_id=select.values[0].id)
        settings = discord.Embed(title='Выбор канала', colour=0xf1c40f)
        settings.add_field(name=f'**Канал для уведомлений:** ```{select.values[0]}```',
                           value='**__________________**',
                           inline=False)
        settings.add_field(name='Вернитесь в панель управления, нажав **Панель управления** ниже',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=SMODSETBACKDE())

class SMODLANGEN(discord.ui.View):
    @discord.ui.select(
        placeholder = "Language selection",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="English",
                description=""
            ),
            discord.SelectOption(
                label="German",
                description=""
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "English":
            getlang = Language.get_or_none(guild_id=interaction.guild_id)
            if getlang is None:
                pass
            else:
                delete = Language.get(Language.guild_id == interaction.guild_id)
                delete.delete_instance()
            Newlanguage = Language.create(guild_id=interaction.guild.id, lang='en')
            settings = discord.Embed(title='Language selection', colour=0xf1c40f)
            settings.add_field(name='**Your language is english now!**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Return to dashboard by clicking **Dashboard** below',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKEN())

        elif select.values[0] == "Russian":
            getlanguage = Language.get_or_none(guild_id=interaction.guild_id)
            if getlanguage is None:
                pass
            else:
                delete = Language.get(Language.guild_id == interaction.guild_id)
                delete.delete_instance()
            Newlanguage = Language.create(guild_id=interaction.guild.id, lang='ru')
            settings = discord.Embed(title='Выбор языка', colour=0xf1c40f)
            settings.add_field(name='**Новый язык, Русский!**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Вернитесь в панель управления, нажав **Панель управления** ниже',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKRU())

class SMODLANGRU(discord.ui.View):
    @discord.ui.select(
        placeholder = "Выбор языка",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Английский",
                description=""
            ),
            discord.SelectOption(
                label="Русский",
                description=""
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Английский":
            getlang = Language.get_or_none(guild_id=interaction.guild_id)
            if getlang is None:
                pass
            else:
                delete = Language.get(Language.guild_id == interaction.guild_id)
                delete.delete_instance()
            Newlanguage = Language.create(guild_id=interaction.guild_id, lang='en')
            settings = discord.Embed(title='Language selection', colour=0xf1c40f)
            settings.add_field(name='**Your language is english now!**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Return to dashboard by clicking **Dashboard** below',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKEN())

        elif select.values[0] == "Русский":
            getlanguage = Language.get_or_none(guild_id=interaction.guild_id)
            if getlanguage is None:
                pass
            else:
                delete = Language.get(Language.guild_id == interaction.guild_id)
                delete.delete_instance()
            Newlanguage = Language.create(guild_id=interaction.guild_id, lang='ru')
            settings = discord.Embed(title='Выбор языка', colour=0xf1c40f)
            settings.add_field(name='**Новый язык, Русский!**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Вернитесь в панель управления, нажав **Панель управления** ниже',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKRU())

class SMODPROTECTEN(discord.ui.View):
    @discord.ui.select(
        placeholder = "Available actions",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Ban",
                description=""
            ),
            discord.SelectOption(
                label="Kick",
                description=""
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Ban":
            getaction = Actions.get_or_none(guild_id=interaction.guild_id)
            if getaction is None:
                newaction = Actions.create(guild_id=interaction.guild_id, action='ban')
            else:
                delete = Actions.get(Actions.guild_id == interaction.guild_id)
                delete.delete_instance()
                newaction = Actions.create(guild_id=interaction.guild_id, action='ban')
            settings = discord.Embed(title='Action selection', colour=0xf1c40f)
            settings.add_field(name='**Action ban selected**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Return to dashboard by clicking **Dashboard** below',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKEN())

        elif select.values[0] == "Kick":
            getaction = Actions.get_or_none(guild_id=interaction.guild_id)
            if getaction is None:
                newaction = Actions.create(guild_id=interaction.guild_id, action='kick')
            else:
                delete = Actions.get(Actions.guild_id == interaction.guild_id)
                delete.delete_instance()
                newaction = Actions.create(guild_id=interaction.guild_id, action='kick')
            settings = discord.Embed(title='Action selection', colour=0xf1c40f)
            settings.add_field(name='**Action kick selected**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Return to dashboard by clicking **Dashboard** below',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKEN())

class SMODPROTECTRU(discord.ui.View):
    @discord.ui.select(
        placeholder = "Возможные действия",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Бан",
                description=""
            ),
            discord.SelectOption(
                label="Кик",
                description=""
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Бан":
            getaction = Actions.get_or_none(guild_id=interaction.guild_id)
            if getaction is None:
                newaction = Actions.create(guild_id=interaction.guild_id, action='ban')
            else:
                delete = Actions.get(Actions.guild_id == interaction.guild_id)
                delete.delete_instance()
                newaction = Actions.create(guild_id=interaction.guild_id, action='ban')
            settings = discord.Embed(title='Выбор действия', colour=0xf1c40f)
            settings.add_field(name='**Выбрано действие, бан**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Вернитесь в панель управления, нажав **Панель управления** ниже',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKRU())

        elif select.values[0] == "Кик":
            getaction = Actions.get_or_none(guild_id=interaction.guild_id)
            if getaction is None:
                newaction = Actions.create(guild_id=interaction.guild_id, action='kick')
            else:
                delete = Actions.get(Actions.guild_id == interaction.guild_id)
                delete.delete_instance()
                newaction = Actions.create(guild_id=interaction.guild_id, action='kick')
            settings = discord.Embed(title='Выбор действия', colour=0xf1c40f)
            settings.add_field(name='**Выбрано действие, кик**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Вернитесь в панель управления, нажав **Панель управления** ниже',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKRU())

class SMODSETEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Language", custom_id="1", style=discord.ButtonStyle.danger)
    async def language_button_callback(self, button, interaction):
        settings = discord.Embed(title='Choose your language!', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODLANGEN())

    @discord.ui.button(label="Notifications", custom_id="2", style=discord.ButtonStyle.blurple)
    async def notifications_button_callback(self, button, interaction):
        settings = discord.Embed(title='Select channel for notifications', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODNOTIFEN())

    @discord.ui.button(label="Protection", custom_id="3", style=discord.ButtonStyle.blurple)
    async def protection_button_callback(self, button, interaction):
        settings = discord.Embed(title='Select preferable action against raiders', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODPROTECTEN())

class SMODSETRU(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Язык", custom_id="1", style=discord.ButtonStyle.danger)
    async def language_button_callback(self, button, interaction):
        settings = discord.Embed(title='Выберите свой язык!', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODLANGRU())

    @discord.ui.button(label="Уведомления", custom_id="2", style=discord.ButtonStyle.blurple)
    async def notifications_button_callback(self, button, interaction):
        settings = discord.Embed(title='Установите канал для уведомлений', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODNOTIFRU())

    @discord.ui.button(label="Защита", custom_id="3", style=discord.ButtonStyle.blurple)
    async def protection_button_callback(self, button, interaction):
        settings = discord.Embed(title='Выберите действие против рейдеров', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODPROTECTRU())

class SMODSETBACKEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Dashboard", custom_id="1", style=discord.ButtonStyle.blurple)
    async def dashboard_button_callback(self, button, interaction):
        settings = discord.Embed(title='Dashboard', colour=0xf1c40f)
        settings.add_field(name='**Here you can modify all functions available**',
                           value='**__________________**', inline=False)
        settings.add_field(name='In order to do so, just click the needed button below!',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=SMODSETEN())

class SMODSETBACKRU(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Панель управления", custom_id="1", style=discord.ButtonStyle.blurple)
    async def dashboard_button_callback(self, button, interaction):
        settings = discord.Embed(title='Панель управления', colour=0xf1c40f)
        settings.add_field(name='**Здесь вы можете изменять настройки бота**',
                           value='**__________________**', inline=False)
        settings.add_field(name='Просто нажмите на нужную кнопку!',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=SMODSETRU())

class SMODREPORTEN(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot = bot

        self.add_item(discord.ui.InputText(label="Please describe the bug", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        channel = bot.get_channel(1141774982268076042)
        settings = discord.Embed(title='Bug report sent', colour=0xf1c40f)
        settings.add_field(name='**Developers will review your report soon**',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=None)
        report = discord.Embed(title='Bug report received', colour=0xf1c40f)
        report.add_field(name='**Please describe the bug**',
                           value=self.children[0].value, inline=False)
        await channel.send(embed=report)

class SMODREPORTRU(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot = bot

        self.add_item(discord.ui.InputText(label="Пожалуйста, опишите ошибку", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        channel = bot.get_channel(1141774982268076042)
        settings = discord.Embed(title='Репорт об ошибках отправлен', colour=0xf1c40f)
        settings.add_field(name='**Разработчики вскоре его рассмотрят**',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=None)
        report = discord.Embed(title='Репорт об ошибках получен', colour=0xf1c40f)
        report.add_field(name='**Пожалуйста, опишите ошибку**',
                           value=self.children[0].value, inline=False)
        await channel.send(embed=report)

class SMODHELPEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Credits", custom_id="1", style=discord.ButtonStyle.blurple)
    async def credit_button_callback(self, button, interaction):
        settings = discord.Embed(title='Dev team', colour=0xf1c40f)
        settings.add_field(name='**Main developer, project manager**',
                           value='```Mester Satellite```', inline=False)
        settings.add_field(name='Advisor',
                           value='```Kyle Kondos```', inline=False)
        await interaction.response.edit_message(embed=settings, view=None)

    @discord.ui.button(label="Bug report", custom_id="2", style=discord.ButtonStyle.danger)
    async def report_button_callback(self, button, interaction):
        await interaction.response.send_modal(SMODREPORTEN(title='Bug report'))

class SMODHELPRU(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Команда", custom_id="1", style=discord.ButtonStyle.blurple)
    async def credit_button_callback(self, button, interaction):
        settings = discord.Embed(title='Разработчики', colour=0xf1c40f)
        settings.add_field(name='**Главный создатель, руководитель проектом**',
                           value='```Mester Satellite```', inline=False)
        settings.add_field(name='Советник',
                           value='```Kyle Kondos```', inline=False)
        await interaction.response.edit_message(embed=settings, view=None)

    @discord.ui.button(label="Репорт ошибок", custom_id="2", style=discord.ButtonStyle.danger)
    async def report_button_callback(self, button, interaction):
        await interaction.response.send_modal(SMODREPORTRU(title='Репорт ошибок'))

class SMOD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="settings", description="change your settings!")
    @commands.has_permissions(administrator=True)
    async def settings(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            settings = discord.Embed(title='Dashboard', colour=0xf1c40f)
            settings.add_field(name='**Here you can modify all functions available**', value='**__________________**', inline=False)
            settings.add_field(name='In order to do so, just click the needed button below!', value='**__________________**', inline=False)
            await ctx.respond(embed=settings, view=SMODSETEN(), ephemeral=True)
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    settings = discord.Embed(title='Dashboard', colour=0xf1c40f)
                    settings.add_field(name='**Here you can modify all functions available**',
                                       value='**__________________**', inline=False)
                    settings.add_field(name='In order to do so, just click the needed button below!',
                                       value='**__________________**', inline=False)
                    await ctx.respond(embed=settings, view=SMODSETEN(), ephemeral=True)
                else:
                    settings = discord.Embed(title='Панель управления', colour=0xf1c40f)
                    settings.add_field(name='**Здесь вы можете изменять настройки бота**',
                                       value='**__________________**', inline=False)
                    settings.add_field(name='Просто нажмите на нужную кнопку!',
                                       value='**__________________**', inline=False)
                    await ctx.respond(embed=settings, view=SMODSETRU(), ephemeral=True)

    @commands.slash_command(name="help", description="help command")
    async def help(self, ctx):
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            settings = discord.Embed(title='Help', colour=0xf1c40f)
            settings.add_field(name='**Command**s', value='You can see all commands by typing **/**',
                               inline=False)
            settings.add_field(name='**Settings/Moderation**',
                               value='Type **/settings**, in order to modify all functions available', inline=False)
            settings.add_field(name='**Current Status**',
                               value=f'Servers: {len(self.bot.guilds)}', inline=False)
            settings.set_thumbnail(url='https://cdn.discordapp.com/avatars/1139234827720208404/b086c35d8039890dcdae4edf97faaba4.png?size=512')
            await ctx.respond(embed=settings, view=SMODHELPEN())
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    settings = discord.Embed(title='Help', colour=0xf1c40f)
                    settings.add_field(name='**Commands**',
                                       value='You can see all commands by typing **/**', inline=False)
                    settings.add_field(name='**Settings/Moderation**',
                                       value='Type **/settings**, in order to modify all functions available', inline=False)
                    settings.add_field(name='**Current Status**',
                                       value=f'Servers: {len(self.bot.guilds)}', inline=False)
                    settings.set_thumbnail(url='https://cdn.discordapp.com/avatars/1139234827720208404/b086c35d8039890dcdae4edf97faaba4.png?size=512')
                    await ctx.respond(embed=settings, view=SMODHELPEN())
                else:
                    settings = discord.Embed(title='Помощь', colour=0xf1c40f)
                    settings.add_field(name='**Команды**',
                                       value='Вы можете увидеть все команды бота, написав **/**', inline=False)
                    settings.add_field(name='**Настройки/Модерация**',
                                       value='Введите **/settings** что бы открыть панель управления со всеми функциями бота.', inline=False)
                    settings.add_field(name='**Статус**',
                                       value=f'Сервера: {len(self.bot.guilds)}', inline=False)
                    settings.set_thumbnail(url='https://cdn.discordapp.com/avatars/1139234827720208404/b086c35d8039890dcdae4edf97faaba4.png?size=512')
                    await ctx.respond(embed=settings, view=SMODHELPRU())

def setup(bot):
    bot.add_cog(SMOD(bot))
