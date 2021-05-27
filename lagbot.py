import mcstatus
from mcrcon import MCRcon
#from mctools import RCONClient
from mcstatus import MinecraftServer
import discord

client = discord.Client()
TOKEN = 'your token'

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
 
  if msg.startswith("#ip"):
    await message.channel.send('your server ip')

  if msg.startswith("#server"):
    server = MinecraftServer.lookup("server ip/ port")
    query = server.query()
    await message.channel.send(query.players.names)

  if msg.startswith("#info"):
    await message.channel.send('Lag-Bot v1.4 W3SLAV')

  if msg.startswith("#event"):
    await message.channel.send('will exist soon... :)')

  if msg.startswith("#msg"):
    user = message.author.name
    mess = str(msg)
    mess2 = mess.replace("#msg ", "", 1)
    mess3 = ("<" + str(user) + ">" + ":" + " " + str(mess2))
    mcr = MCRcon("rcon ip", "rcon password")
    mcr.connect()
    resp = mcr.command("/whitelist add bob")
    print(resp)
    mcr.disconnect()
    #rcon.command("/say " + mess3)
    await message.channel.send(mess3)
    
  if msg.startswith("#cmd"):
    mello = str(msg)
    mell0 = mello.replace("#cmd ", "", 1)
    if msg != "#cmd":
      if "@op" in message.author.roles:
        await message.channel.send(mell0)
      else:
        await message.channel.send("You need permission to preform this action")
    else:
      await messgae.channel.send("Please enter command")

client.run(TOKEN)
