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
      await channel.send(':: kboot v1 stared...\n:: starting iner menu...')
      await channel.send('1 start CustOS \n2 continue the boot')
      break;

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    if message.content.startswith('1'):
      await message.channel.send(':: starting KernSys...')
      os.system("curl https://updatepakager.legamer4.repl.co/custom-kernel/custOS.py > CustOS.py")
      await message.channel.send(':: starting KernSys...DONE\n:: starting the OS...')
	  os.system("python CustOS.py")
    
    if message.content.startswith('2'):
      await message.channel.send('continue startup...')
      os.system("python cdrom.py")
                

client.run(token)