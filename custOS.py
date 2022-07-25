import os
import discord
client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763

@client.event
async def on_ready():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
      await channel.send(':: KernSys loader...OK\n:: starting Custome kernel...')
      await channel.send('welcome on custOS')
      break;

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    if message.content.startswith('$help'):
      await message.channel.send('help menu here\n$reboot')
    
    if message.content.startswith('$reboot'):
      await message.channel.send('rebooing...')
      os.system("python main.py")
                

client.run(token)