import discord
from discord.ext import commands
from googletrans import Translator
translator = Translator()

class SRA(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guld.id != 1150689721144574002:
            pass
        else:
            if message.channel.id != 1150690216831627286:
                pass
            else:
                if message.author.id == 1063985173349277756:
                    trans = translator.translate(message.content, dest='ru')
                    await message.delete()
                    await message.channel.send(f"{message.author.name}:   " + trans.text + "----------" + message.content)
                elif message.author.id == 786011616004669440:
                    trans = translator.translate(message.content, dest='ru')
                    await message.delete()
                    await message.channel.send(
                        f"{message.author.name}:   " + trans.text + "----------" + message.content)
                else:
                    trans = translator.translate(message.content, dest='en')
                    await message.delete()
                    await message.channel.send(
                        f"{message.author.name}:   " + message.content + "----------" + trans.text)

def setup(bot):
    bot.add_cog(SRA(bot))