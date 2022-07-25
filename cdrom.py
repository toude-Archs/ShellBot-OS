import os
import discord

client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
        PATH = './bios.py'
        await channel.send('testing hard drive...')
        print("testing hard drive...")
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            await channel.send('booting from hard drive..')
            print("booting from hard drive...")
            os.system('clear')
            os.system('python3 bios.py')
            break;
        else:
            await channel.send('testing from hard drive...ERROR\ntesting network conectivity')
            print('testing hard drive...ERROR\ntesting network conectivity')
            os.system("rm knet.py")
            os.system("curl https://updatepakager.legamer4.repl.co/systpak/knet-new.py > knet.py")
            os.system("python3 knet.py")
            break;


@client.event
async def on_ready():
  print("ok")
client.loop.create_task(my_background_task())
client.run(token)
