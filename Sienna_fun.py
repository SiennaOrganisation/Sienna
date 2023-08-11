import discord
from discord.ext import commands
import json
import requests
import random
import peewee
from peewee import *
from Sienna import Language

class SFUNREGEN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Again", custom_id="1", style=discord.ButtonStyle.danger)
    async def again_button_callback(self, button, interaction):
        response = requests.get('https://randomfox.ca/floof/')
        json_fox = json.loads(response.text)
        fox = discord.Embed(color=0xff9900, title='Random Fox')
        fox.set_image(url=json_fox['image'])
        await interaction.response.edit_message(embed=fox, view=SFUNREGEN())

class SFUN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="fox", description="Cute foxes included :3")
    @commands.has_permissions(ban_members=True)
    async def fox(self, ctx):
        response = requests.get('https://randomfox.ca/floof/')
        json_fox = json.loads(response.text)
        fox = discord.Embed(color=0xff9900, title='Random Fox')
        fox.set_image(url=json_fox['image'])
        await ctx.response.defer()
        await ctx.followup.send(embed=fox, view=SFUNREGEN())

def setup(bot):
    bot.add_cog(SFUN(bot))