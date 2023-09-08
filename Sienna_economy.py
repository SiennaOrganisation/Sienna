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
            for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user.id):
                delete = Economy.get(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user.id)
                delete.delete_instance()
                neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user.id, amount=economy.amount + salary)
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
                                                      Economy.user_id == interaction.user.id):
                    delete = Economy.get(Economy.guild_id == interaction.guild_id,
                                         Economy.user_id == interaction.user.id)
                    delete.delete_instance()
                    neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user.id,
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

class SECOSELECTRU(discord.ui.View):
    @discord.ui.select(
        placeholder = "Выбор работы",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="Работник на фабрике",
                description="Ничего особенного"
            ),
            discord.SelectOption(
                label="Заняться бизнесом",
                description="Будьте осторожны! Бизнес может провалиться!"
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "Работник на фабрике":
            salary = random.randint(1, 50)
            for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user.id):
                delete = Economy.get(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user.id)
                delete.delete_instance()
                neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user.id, amount=economy.amount + salary)
                eco = discord.Embed(title='Выбор работы', colour=0xf1c40f)
                eco.add_field(name=f'**Вы получили {salary} 💎, работая на фабрике**', value='**__________________**',
                                   inline=False)
                eco.add_field(name='Проверьте баланс своего счета, нажав **Баланс** ниже',
                                   value='**__________________**', inline=False)
                await interaction.response.edit_message(embed=eco, view=SECOBALANCERU())


        elif select.values[0] == "Заняться бизнесом":
            luck = random.randint(1, 20)
            if luck < 9:
                salary = random.randint(1, 150)
                for economy in Economy.select().where(Economy.guild_id == interaction.guild_id,
                                                      Economy.user_id == interaction.user.id):
                    delete = Economy.get(Economy.guild_id == interaction.guild_id,
                                         Economy.user_id == interaction.user.id)
                    delete.delete_instance()
                    neweco = Economy.create(guild_id=interaction.guild_id, user_id=interaction.user.id,
                                            amount=economy.amount + salary)
                    eco = discord.Embed(title='Выбор работы', colour=0xf1c40f)
                    eco.add_field(name=f'**Вы получили {salary} 💎, развивая свой бизнес**',
                                       value='**__________________**',
                                       inline=False)
                    eco.add_field(name='Проверьте баланс своего счета, нажав **Баланс** ниже',
                                       value='**__________________**', inline=False)
                    await interaction.response.edit_message(embed=eco, view=SECOBALANCERU())
            else:
                eco = discord.Embed(title='Выбор работы', colour=0xf1c40f)
                eco.add_field(name=f'**Ваш бизнес к сожалению провалился :(**',
                                   value='**__________________**',
                                   inline=False)
                eco.add_field(name='Проверьте баланс своего счета, нажав **Баланс** ниже',
                                   value='**__________________**', inline=False)
                await interaction.response.edit_message(embed=eco, view=SECOBALANCERU())

class SECOBALANCEEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Balance", custom_id="1", style=discord.ButtonStyle.blurple)
    async def balance_button_callback(self, button, interaction):
        for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user.id):
            eco = discord.Embed(title='Your balance', colour=0xf1c40f)
            eco.add_field(name=f'**You have {economy.amount} 💎**',
                               value='**__________________**', inline=False)
            eco.add_field(name='Want to have more? Type **/work**!',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=eco, view=None)

class SECOBALANCERU(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Баланс", custom_id="1", style=discord.ButtonStyle.blurple)
    async def balance_button_callback(self, button, interaction):
        for economy in Economy.select().where(Economy.guild_id == interaction.guild_id, Economy.user_id == interaction.user.id):
            eco = discord.Embed(title='Ваш баланс', colour=0xf1c40f)
            eco.add_field(name=f'**У вас {economy.amount} 💎**',
                               value='**__________________**', inline=False)
            eco.add_field(name='Хотите иметь больше? Введите **/work**!',
                               value='**__________________**', inline=False)
            await interaction.response.edit_message(embed=eco, view=None)

class SECONOMY(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="balance", description="check your balance")
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
                eco.add_field(name='Want to have more? Type **/work**!',
                                   value='**__________________**', inline=False)
                await ctx.respond(embed=eco, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        eco = discord.Embed(title='Your balance', colour=0xf1c40f)
                        eco.add_field(name=f'**You have {economy.amount} 💎**',
                                           value='**__________________**', inline=False)
                        eco.add_field(name='Want to have more? Type **/work**!',
                                           value='**__________________**', inline=False)
                        await ctx.respond(embed=eco, ephemeral=True)
                    else:
                        eco = discord.Embed(title='Ваш баланс', colour=0xf1c40f)
                        eco.add_field(name=f'**У вас {economy.amount} 💎**',
                                           value='**__________________**', inline=False)
                        eco.add_field(name='Хотите иметь больше? Введите **/work**!',
                                           value='**__________________**', inline=False)
                        await ctx.respond(embed=eco, ephemeral=True)

    @commands.slash_command(name="work", description="earn some more")
    @commands.cooldown(1, 3600, commands.BucketType.guild)
    async def work(self, ctx):
        geteco = Economy.get_or_none(guild_id=ctx.guild.id, user_id=ctx.author.id)
        if geteco is None:
            neweco = Economy.create(guild_id=ctx.guild.id, user_id=ctx.author.id, amount='0')
        else:
            pass
        getlang = Language.get_or_none(guild_id=ctx.guild.id)
        if getlang is None:
            eco = discord.Embed(title='Choose preferred work', colour=0xf1c40f)
            await ctx.respond(embed=eco, view=SECOSELECTEN(), ephemeral=True)
        else:
            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                if language.lang == 'en':
                    eco = discord.Embed(title='Choose preferred work', colour=0xf1c40f)
                    await ctx.respond(embed=eco, view=SECOSELECTEN(), ephemeral=True)
                else:
                    eco = discord.Embed(title='Выберите предпочитаемую работу', colour=0xf1c40f)
                    await ctx.respond(embed=eco, view=SECOSELECTRU(), ephemeral=True)

    @commands.slash_command(name="transfer", description="transfer your credits to someone")
    async def transfer(self, ctx, user: discord.Member, amount: int):
        if amount < 0:
            getlang = Language.get_or_none(guild_id=ctx.guild.id)
            if getlang is None:
                eco = discord.Embed(title='Error!', colour=0xf1c40f)
                eco.add_field(name=f'**Only positive amounts can be specified! You have entered:** ```{amount}```',
                              value='**__________________**', inline=False)
                await ctx.respond(embed=eco, ephemeral=True)
            else:
                for language in Language.select().where(Language.guild_id == ctx.guild.id):
                    if language.lang == 'en':
                        eco = discord.Embed(title='Error!', colour=0xf1c40f)
                        eco.add_field(name=f'**Only positive amounts can be specified! You have entered:** ```{amount}```',
                                      value='**__________________**', inline=False)
                        await ctx.respond(embed=eco, ephemeral=True)
                    else:
                        eco = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                        eco.add_field(name=f'**Можно указывать только положительную сумму! Вы указали:** ```{amount}```',
                                      value='**__________________**', inline=False)
                        await ctx.respond(embed=eco, ephemeral=True)
        else:
            geteco = Economy.get_or_none(guild_id=ctx.guild.id, user_id=user.id)
            if geteco is None:
                neweco = Economy.create(guild_id=ctx.guild.id, user_id=user.id, amount='0')
            else:
                pass
            geteco = Economy.get_or_none(guild_id=ctx.guild.id, user_id=ctx.author.id)
            if geteco is None:
                neweco = Economy.create(guild_id=ctx.guild.id, user_id=ctx.author.id, amount='0')
                getlang = Language.get_or_none(guild_id=ctx.guild.id)
                if getlang is None:
                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                    eco.add_field(name=f'**You do not have enough 💎! Your current balance is: 0 💎**',
                                  value='**__________________**', inline=False)
                    eco.add_field(name='Want to have more? Type **/work**!',
                                  value='**__________________**', inline=False)
                    await ctx.respond(embed=eco, ephemeral=True)
                else:
                    for language in Language.select().where(Language.guild_id == ctx.guild.id):
                        if language.lang == 'en':
                            eco = discord.Embed(title='Error!', colour=0xf1c40f)
                            eco.add_field(name=f'**You do not have enough 💎! Your current balance is: 0 💎**',
                                          value='**__________________**', inline=False)
                            eco.add_field(name='Want to have more? Type **/work**!',
                                          value='**__________________**', inline=False)
                            await ctx.respond(embed=eco, ephemeral=True)
                        else:
                            eco = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                            eco.add_field(name=f'**У вас не хватает 💎! Ваш баланс: 0 💎**',
                                          value='**__________________**', inline=False)
                            eco.add_field(name='Хотите иметь больше? Введите **/work**!',
                                          value='**__________________**', inline=False)
                            await ctx.respond(embed=eco, ephemeral=True)
            else:
                for economy in Economy.select().where(Economy.guild_id == ctx.guild.id,
                                                      Economy.user_id == ctx.author.id):
                    if economy.amount < amount:
                        getlang = Language.get_or_none(guild_id=ctx.guild.id)
                        if getlang is None:
                            eco = discord.Embed(title='Error!', colour=0xf1c40f)
                            eco.add_field(
                                name=f'**You do not have enough 💎! Your current balance is: {economy.amount} 💎**',
                                value='**__________________**', inline=False)
                            eco.add_field(name='Want to have more? Type **/work**!',
                                          value='**__________________**', inline=False)
                            await ctx.respond(embed=eco, ephemeral=True)
                        else:
                            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                                if language.lang == 'en':
                                    eco = discord.Embed(title='Error!', colour=0xf1c40f)
                                    eco.add_field(
                                        name=f'**You do not have enough 💎! Your current balance is: {economy.amount} 💎**',
                                        value='**__________________**', inline=False)
                                    eco.add_field(name='Want to have more? Type **/work**!',
                                                  value='**__________________**', inline=False)
                                    await ctx.respond(embed=eco, ephemeral=True)
                                else:
                                    eco = discord.Embed(title='Ошибка!', colour=0xf1c40f)
                                    eco.add_field(
                                        name=f'**У вас не хватает 💎! Ваш баланс: {economy.amount} 💎**',
                                        value='**__________________**', inline=False)
                                    eco.add_field(name='Хотите иметь больше? Введите **/work**!',
                                                  value='**__________________**', inline=False)
                                    await ctx.respond(embed=eco, ephemeral=True)
                    else:
                        delete = Economy.get(Economy.guild_id == ctx.guild.id,
                                             Economy.user_id == ctx.author.id)
                        delete.delete_instance()
                        neweco = Economy.create(guild_id=ctx.guild.id, user_id=ctx.author.id,
                                                amount=economy.amount - amount)
                        for economy in Economy.select().where(Economy.guild_id == ctx.guild.id,
                                                              Economy.user_id == user.id):
                            delete = Economy.get(Economy.guild_id == ctx.guild.id,
                                                 Economy.user_id == user.id)
                            delete.delete_instance()
                            neweco = Economy.create(guild_id=ctx.guild.id, user_id=user.id,
                                                    amount=economy.amount + amount)
                            balance = economy.amount + amount
                        getlang = Language.get_or_none(guild_id=ctx.guild.id)
                        if getlang is None:
                            eco = discord.Embed(title='Credit transfer', colour=0xf1c40f)
                            eco.add_field(name=f'**You have transferred {amount} 💎 to {user.name}**',
                                          value='**__________________**', inline=False)
                            eco.add_field(name=f'{user.name} will receive notification soon',
                                          value='**__________________**', inline=False)
                            await ctx.respond(embed=eco, ephemeral=True)
                        else:
                            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                                if language.lang == 'en':
                                    eco = discord.Embed(title='Credit transfer', colour=0xf1c40f)
                                    eco.add_field(
                                        name=f'**You have transferred {amount} 💎 to {user.name}**',
                                        value='**__________________**', inline=False)
                                    eco.add_field(name=f'{user.name} will receive notification soon',
                                                  value='**__________________**', inline=False)
                                    await ctx.respond(embed=eco, ephemeral=True)
                                else:
                                    eco = discord.Embed(title='Перевод', colour=0xf1c40f)
                                    eco.add_field(
                                        name=f'**Вы успешно перевели {amount} 💎, {user.name}**',
                                        value='**__________________**', inline=False)
                                    eco.add_field(name=f'{user.name} уже получил уведомление',
                                                  value='**__________________**', inline=False)
                                    await ctx.respond(embed=eco, ephemeral=True)
                        getlang = Language.get_or_none(guild_id=ctx.guild.id)
                        if getlang is None:
                            eco = discord.Embed(title='Credit transfer', colour=0xf1c40f)
                            eco.add_field(name=f'**{ctx.author.name} transferred you {amount} 💎**',
                                          value='**__________________**', inline=False)
                            eco.add_field(name=f'Your current balance: **{balance} 💎**',
                                          value='**__________________**', inline=False)
                            await user.send(embed=eco)
                        else:
                            for language in Language.select().where(Language.guild_id == ctx.guild.id):
                                if language.lang == 'en':
                                    eco = discord.Embed(title='Credit transfer', colour=0xf1c40f)
                                    eco.add_field(
                                        name=f'**{ctx.author.name} transferred you {amount} 💎**',
                                        value='**__________________**', inline=False)
                                    eco.add_field(name=f'Your current balance: **{balance} 💎**',
                                                  value='**__________________**', inline=False)
                                    await user.send(embed=eco)
                                else:
                                    eco = discord.Embed(title='Перевод', colour=0xf1c40f)
                                    eco.add_field(
                                        name=f'**{ctx.author.name} перевел вам {amount} 💎**',
                                        value='**__________________**', inline=False)
                                    eco.add_field(name=f'Ваш баланс: **{balance} 💎**',
                                                  value='**__________________**', inline=False)
                                    await user.send(embed=eco)

def setup(bot):
    bot.add_cog(SECONOMY(bot))
