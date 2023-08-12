import discord
from discord.ext import commands
import random
import peewee
from peewee import *
from Sienna import Language, Economy

class SECOSELECTEN(discord.ui.View):
    @discord.ui.select(
        placeholder = "Work selection",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Factory worker",
                description="Nothing special here"
            ),
            discord.SelectOption(
                label="Run your own business",
                description="Be careful here! Business may fail!"
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Factory worker":
            salary = random.randint(1, 50)
            for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user_id):
                delete = Economy.get(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user_id)
                delete.delete_instance()
                neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user_id, amount=economy.amount + salary)
                eco = discord.Embed(title='Work selection', colour=0xf1c40f)
                eco.add_field(name=f'**You have earned {salary} 💎, as a factory worker**', value='**__________________**',
                                   inline=False)
                eco.add_field(name='Check your balance by clicking **Balance** below',
                                   value='**__________________**', inline=False)
                await interaction.response.edit_message(embed=eco, view=SECOBALANCEEN())


        elif select.values[0] == "Run your own business":
            luck = random.randint(1, 20)
            if luck < 9:
                salary = random.randint(1, 150)
                for economy in Economy.select().where(Economy.guild_id == interaction.guild_id,
                                                      Economy.user_id == interaction.user_id):
                    delete = Economy.get(Economy.guild_id == interaction.guild_id,
                                         Economy.user_id == interaction.user_id)
                    delete.delete_instance()
                    neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user_id,
                                            amount=economy.amount + salary)
                    eco = discord.Embed(title='Work selection', colour=0xf1c40f)
                    eco.add_field(name=f'**You have earned {salary} 💎, while running your business**',
                                       value='**__________________**',
                                       inline=False)
                    eco.add_field(name='Check your balance by clicking **Balance** below',
                                       value='**__________________**', inline=False)
                    await interaction.response.edit_message(embed=eco, view=SECOBALANCEEN())
            else:
                eco = discord.Embed(title='Work selection', colour=0xf1c40f)
                eco.add_field(name=f'**Your business has sadly failed :(**',
                                   value='**__________________**',
                                   inline=False)
                eco.add_field(name='Check your balance by clicking **Balance** below',
                                   value='**__________________**', inline=False)
                await interaction.response.edit_message(embed=eco, view=SECOBALANCEEN())

class SECOSELECTDE(discord.ui.View):
    @discord.ui.select(
        placeholder = "Arbeitsauswahl",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Fabrik Arbeiter",
                description="Hier gibt es nichts Besonderes"
            ),
            discord.SelectOption(
                label="Ihr eigenes Unternehmen führen",
                description="Seien Sie hier vorsichtig! Das könnte scheitern!"
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Fabrik Arbeiter":
            salary = random.randint(1, 50)
            for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user_id):
                delete = Economy.get(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user_id)
                delete.delete_instance()
                neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user_id, amount=economy.amount + salary)
                eco = discord.Embed(title='Arbeitsauswahl', colour=0xf1c40f)
                eco.add_field(name=f'**Sie haben {salary} 💎, als Fabrikarbeiter bekommen**', value='**__________________**',
                                   inline=False)
                eco.add_field(name='Überprüfen Sie Ihr Kontostand, indem Sie unten auf **Kontostand** klicken',
                                   value='**__________________**', inline=False)
                await interaction.response.edit_message(embed=eco, view=SECOBALANCEDE())


        elif select.values[0] == "Ihr eigenes Unternehmen führen":
            luck = random.randint(1, 20)
            if luck < 9:
                salary = random.randint(1, 150)
                for economy in Economy.select().where(Economy.guild_id == interaction.guild_id,
                                                      Economy.user_id == interaction.user_id):
                    delete = Economy.get(Economy.guild_id == interaction.guild_id,
                                         Economy.user_id == interaction.user_id)
                    delete.delete_instance()
                    neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user_id,
                                            amount=economy.amount + salary)
                    eco = discord.Embed(title='Arbeitsauswahl', colour=0xf1c40f)
                    eco.add_field(name=f'**Sie haben {salary} 💎, während Sie Ihr Unternehmen geführt haben bekommen**',
                                       value='**__________________**',
                                       inline=False)
                    eco.add_field(name='Überprüfen Sie Ihr Kontostand, indem Sie unten auf **Kontostand** klicken',
                                       value='**__________________**', inline=False)
                    await interaction.response.edit_message(embed=eco, view=SECOBALANCEDE())
            else:
                eco = discord.Embed(title='Arbeitsauswahl', colour=0xf1c40f)
                eco.add_field(name=f'**Ihr Unternehmen ist leider gescheitert :(**',
                                   value='**__________________**',
                                   inline=False)
                eco.add_field(name='Überprüfen Sie Ihr Kontostand, indem Sie unten auf **Kontostand** klicken',
                                   value='**__________________**', inline=False)
                await interaction.response.edit_message(embed=eco, view=SECOBALANCEDE())

class SECOBALANCEEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Balance", custom_id="1", style=discord.ButtonStyle.blurple)
    async def balance_button_callback(self, button, interaction):
        for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user_id):
            eco = discord.Embed(title='Your balance', colour=0xf1c40f)
            eco.add_field(name=f'**You have {economy.amount} 💎**',
                               value='**__________________**', inline=False)
            eco.add_field(name='Want to have more? Click **work** button below!',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=eco, view=SECOWORKEN())

class SECOBALANCEDE(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Kontostand", custom_id="1", style=discord.ButtonStyle.blurple)
    async def balance_button_callback(self, button, interaction):
        for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user_id):
            eco = discord.Embed(title='Ihr Kontostand', colour=0xf1c40f)
            eco.add_field(name=f'**Sie haben {economy.amount} 💎**',
                               value='**__________________**', inline=False)
            eco.add_field(name='Lust auf mehr? Klicken Sie unten auf die Schaltfläche **Arbeiten**!',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=eco, view=SECOWORKDE())

class SECOWORKEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 60, commands.BucketType.member)

    @discord.ui.button(label="Work", custom_id="1", style=discord.ButtonStyle.blurple)
    async def work_button_callback(self, button, interaction):
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(f"Cooldown! Try again in {round(retry, 1)} seconds!", ephemeral = True)
        eco = discord.Embed(title='Choose preferred work', colour=0xf1c40f)
        await interaction.response.edit_message(embed=eco, view=SECOSELECTEN())

class SECOWORKDE(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 60, commands.BucketType.member)

    @discord.ui.button(label="Arbeit", custom_id="1", style=discord.ButtonStyle.blurple)
    async def work_button_callback(self, button, interaction):
        bucket = self.cooldown.get_bucket(interaction.message)
        retry = bucket.update_rate_limit()
        if retry:
            return await interaction.response.send_message(f"Abkühlen! Versuchen Sie es in {round(retry, 1)} Sekunden noch einmal!", ephemeral=True)
        eco = discord.Embed(title='Wählen Sie Ihre bevorzugte Arbeit', colour=0xf1c40f)
        await interaction.response.edit_message(embed=eco, view=())

class SECONOMY(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="balance", description="check your balance")
    @commands.has_permissions(administrator=True)
    async def balance(self, ctx):
        geteco = Economy.get_or_none(guild_id=ctx.guild.id, user_id=ctx.author.id)
        if geteco is None:
            neweco = Economy.create(guild_id=ctx.guild.id, user_id=ctx.author.id, amount='0')
        else:
            pass
        for economy in Economy.select().where(Economy.guild_id == ctx.guild.id, Economy.user_id == ctx.author.id):
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                eco = discord.Embed(title='Your balance', colour=0xf1c40f)
                eco.add_field(name=f'**You have {economy.amount} 💎**',
                                   value='**__________________**', inline=False)
                eco.add_field(name='Want to have more? Click **work** button below!',
                                   value='**__________________**', inline=False)
                await ctx.respond(embed=eco, view=SECOWORKEN())
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        eco = discord.Embed(title='Your balance', colour=0xf1c40f)
                        eco.add_field(name=f'**You have {economy.amount} 💎**',
                                           value='**__________________**', inline=False)
                        eco.add_field(name='Want to have more? Click **work** button below!',
                                           value='**__________________**', inline=False)
                        await ctx.respond(embed=eco, view=SECOWORKEN())
                    else:
                        eco = discord.Embed(title='Ihr Kontostand', colour=0xf1c40f)
                        eco.add_field(name=f'**Sie haben {economy.amount} 💎**',
                                           value='**__________________**', inline=False)
                        eco.add_field(name='Lust auf mehr? Klicken Sie unten auf die Schaltfläche **Arbeiten**!',
                                           value='**__________________**', inline=False)
                        await ctx.respond(embed=eco, view=SECOWORKDE())

def setup(bot):
    bot.add_cog(SECONOMY(bot))