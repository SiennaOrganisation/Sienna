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

class SMODNOTIFDE(discord.ui.View):
    @discord.ui.select(
        placeholder="Kanalauswahl",
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
        settings = discord.Embed(title='Kanalauswahl', colour=0xf1c40f)
        settings.add_field(name=f'**Kanal für alle Benachrichtigungen:** ```{select.values[0]}```',
                           value='**__________________**',
                           inline=False)
        settings.add_field(name='Kehren Sie zum Dashboard zurück, indem Sie unten auf **Dashboard** klicken',
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

        elif select.values[0] == "German":
            getlanguage = Language.get_or_none(guild_id=interaction.guild_id)
            if getlanguage is None:
                pass
            else:
                delete = Language.get(Language.guild_id == interaction.guild_id)
                delete.delete_instance()
            Newlanguage = Language.create(guild_id=interaction.guild.id, lang='de')
            settings = discord.Embed(title='Sprachauswahl', colour=0xf1c40f)
            settings.add_field(name='**Ihre Sprache ist jetzt Deutsch!**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Kehren Sie zum Dashboard zurück, indem Sie unten auf **Dashboard** klicken',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKDE())

class SMODLANGDE(discord.ui.View):
    @discord.ui.select(
        placeholder = "Sprachauswahl",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Englisch",
                description=""
            ),
            discord.SelectOption(
                label="Deutsch",
                description=""
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Englisch":
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

        elif select.values[0] == "Deutsch":
            getlanguage = Language.get_or_none(guild_id=interaction.guild_id)
            if getlanguage is None:
                pass
            else:
                delete = Language.get(Language.guild_id == interaction.guild_id)
                delete.delete_instance()
            Newlanguage = Language.create(guild_id=interaction.guild_id, lang='de')
            settings = discord.Embed(title='Sprachauswahl', colour=0xf1c40f)
            settings.add_field(name='**Ihre Sprache ist jetzt Deutsch!**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Kehren Sie zum Dashboard zurück, indem Sie unten auf **Dashboard** klicken',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKDE())

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
            Newlanguage = Language.create(guild_id=interaction.guild_id, lang='en')
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
            Newlanguage = Language.create(guild_id=interaction.guild_id, lang='de')
            settings = discord.Embed(title='Action selection', colour=0xf1c40f)
            settings.add_field(name='**Action kick selected**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Return to dashboard by clicking **Dashboard** below',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKEN())

class SMODPROTECTDE(discord.ui.View):
    @discord.ui.select(
        placeholder = "Mögliche Aktionen",
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
            Newlanguage = Language.create(guild_id=interaction.guild_id, lang='en')
            settings = discord.Embed(title='Aktionsauswahl', colour=0xf1c40f)
            settings.add_field(name='**Aktion ban ausgewählt**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Kehren Sie zum Dashboard zurück, indem Sie unten auf **Dashboard** klicken',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKDE())

        elif select.values[0] == "Kick":
            getaction = Actions.get_or_none(guild_id=interaction.guild_id)
            if getaction is None:
                newaction = Actions.create(guild_id=interaction.guild_id, action='kick')
            else:
                delete = Actions.get(Actions.guild_id == interaction.guild_id)
                delete.delete_instance()
                newaction = Actions.create(guild_id=interaction.guild_id, action='kick')
            Newlanguage = Language.create(guild_id=interaction.guild_id, lang='de')
            settings = discord.Embed(title='Aktionsauswahl', colour=0xf1c40f)
            settings.add_field(name='**Aktion kick ausgewählt**', value='**__________________**',
                               inline=False)
            settings.add_field(name='Kehren Sie zum Dashboard zurück, indem Sie unten auf **Dashboard** klicken',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=settings, view=SMODSETBACKDE())

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

class SMODSETDE(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Sprache", custom_id="1", style=discord.ButtonStyle.danger)
    async def language_button_callback(self, button, interaction):
        settings = discord.Embed(title='Wähle deine Sprache!', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODLANGDE())

    @discord.ui.button(label="Benachrichtigungen", custom_id="2", style=discord.ButtonStyle.blurple)
    async def notifications_button_callback(self, button, interaction):
        settings = discord.Embed(title='Wählen Sie den Kanal für Benachrichtigungen aus', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODNOTIFDE())

    @discord.ui.button(label="Schutz", custom_id="3", style=discord.ButtonStyle.blurple)
    async def protection_button_callback(self, button, interaction):
        settings = discord.Embed(title='Wählen Sie die bevorzugte Aktion gegen Raiders', colour=0xf1c40f)
        await interaction.response.edit_message(embed=settings, view=SMODPROTECTDE())

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

class SMODSETBACKDE(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Dashboard", custom_id="1", style=discord.ButtonStyle.blurple)
    async def dashboard_button_callback(self, button, interaction):
        settings = discord.Embed(title='Dashboard', colour=0xf1c40f)
        settings.add_field(name='**Hier können Sie alle verfügbaren Funktionen ändern**',
                           value='**__________________**', inline=False)
        settings.add_field(name='Klicken Sie dazu einfach unten auf die entsprechende Schaltfläche!',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=SMODSETDE())

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

class SMODREPORTDE(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot = bot

        self.add_item(discord.ui.InputText(label="Bitte beschreiben Sie den Fehler", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        channel = bot.get_channel(1141774982268076042)
        settings = discord.Embed(title='Fehlerbericht gesendet', colour=0xf1c40f)
        settings.add_field(name='**Developers werden Ihren Bericht bald überprüfen**',
                           value='**__________________**', inline=False)
        await interaction.response.edit_message(embed=settings, view=None)
        report = discord.Embed(title='Fehlerbericht erhalten', colour=0xf1c40f)
        report.add_field(name='**Bitte beschreiben Sie den Fehler**',
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

class SMODHELPDE(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Credits", custom_id="1", style=discord.ButtonStyle.blurple)
    async def credit_button_callback(self, button, interaction):
        settings = discord.Embed(title='Dev team', colour=0xf1c40f)
        settings.add_field(name='**Hauptentwickler, Projektmanager**',
                           value='```Mester Satellite```', inline=False)
        settings.add_field(name='Berater',
                           value='```Kyle Kondos```', inline=False)
        await interaction.response.edit_message(embed=settings, view=None)

    @discord.ui.button(label="Fehlerbericht", custom_id="2", style=discord.ButtonStyle.danger)
    async def report_button_callback(self, button, interaction):
        await interaction.response.send_modal(SMODREPORTEN(title='Fehlerbericht'))

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
                    settings = discord.Embed(title='Dashboard', colour=0xf1c40f)
                    settings.add_field(name='**Hier können Sie alle verfügbaren Funktionen ändern**',
                                       value='**__________________**', inline=False)
                    settings.add_field(name='Klicken Sie dazu einfach unten auf die entsprechende Schaltfläche!',
                                       value='**__________________**', inline=False)
                    await ctx.respond(embed=settings, view=SMODSETDE(), ephemeral=True)

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
                    settings = discord.Embed(title='Hilfe', colour=0xf1c40f)
                    settings.add_field(name='**Befehle**',
                                       value='Sie können alle Befehle sehen, indem Sie **/** eingeben', inline=False)
                    settings.add_field(name='**Einstellungen/Moderation**',
                                       value='Geben Sie **/settings** ein, um alle verfügbaren Funktionen zu ändern', inline=False)
                    settings.add_field(name='**Aktueller Status**',
                                       value=f'Servers: {len(self.bot.guilds)}', inline=False)
                    settings.set_thumbnail(url='https://cdn.discordapp.com/avatars/1139234827720208404/b086c35d8039890dcdae4edf97faaba4.png?size=512')
                    await ctx.respond(embed=settings, view=SMODHELPDE())

def setup(bot):
    bot.add_cog(SMOD(bot))
