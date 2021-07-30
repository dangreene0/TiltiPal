from constants import *
import json
import requests
import logging
import discord
from discord.ext import commands
from discord.ext import tasks
from colorama import Fore as color

class donoUpdater(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # currently commented out because the campaign auth code is invalid
        # @bot.event
        # async def on_ready():
        #     await update.start()

        @tasks.loop(hours=1)
        async def update():
            # fetch info of target
            channel = bot.get_channel(MIDSUM21)
            donomessage = await channel.fetch_message(DMSGMIDSUM21)
            # this shit is outdated, the auth code was revoked somehow
            response = requests.get(
                # USE THIS LINK UNTIL PAGE IS LIVE
                'https://tiltify.com/api/v3/users/cheddzy-tfconnect/campaigns/tfconnect-2020')
                # USE THIS LINK WHEN THE PAGE IS LIVE !!!
            #     'https://tiltify.com/api/v3/users/cheddzy-tfconnect/campaigns/tfconnect-summer-2021')
            # using json it fetches the data we use.
            response = json.loads(response.text)
            total = response["data"]["totalAmountRaised"]

            # creates embed to edit
            num = '{:,.2f}'.format(total)
            # TODO make embed common method
            donoembed = discord.Embed(title=f'We\'ve successfully raised ${num} USD \nfor \"Stop AAPI Hate\" in 2021!',
                                    description="**Click here to donate: http://www.tfconnect.org/**",
                                    color=0x80007f)
            donoembed.set_image(url='https://cdn.discordapp.com/attachments/772477603465658399/795411090770100277/fkh.png')
            await donomessage.edit(embed=donoembed, content='')
            # Logs the new total.
            logging.warning(color.MAGENTA + f"Update: ${num} USD"+ color.RESET)
        
def setup(bot):
    bot.add_cog(donoUpdater(bot))