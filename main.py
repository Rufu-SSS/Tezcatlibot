import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()  # Activa els intents per defecte
intents.messages = True  # Permet llegir i interactuar amb els missatges
intents.guilds = True  # Permet interactuar amb guilds (servidors)
intents.members = True  # Permet veure i gestionar membres

bot=commands.Bot(command_prefix="&", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')


bot.run(TOKEN)









""" Com a minim fer aquestes comandes
&servant nom_servant
&servant_list classe_servant
&kick
&ban
&ce_recommendations nom_servant
&servant_tierlist
&summon_simulator na
&summon_simulator jp
&summon_banner_list
&materials
&quests
&ce_list
"""

"""
Enllaç d'invitació: 
https://discord.com/oauth2/authorize?client_id=1328750028646252554&scope=bot%20applications.commands&permissions=1529478638678
"""