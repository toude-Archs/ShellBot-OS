import os
import discord
client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id ) # replace with channel_id
    while not client.is_closed():
        PATH = './kern.py'
        await channel.send('welcome to ShellOS bot')
        print("welcome to ShellOS bot")
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            await channel.send('Checking kern.py...OK')
            print("Checking kern.py...OK")
            os.system("python3 syst.py")
            os.system('clear')
            break;
        else:
            await channel.send('Checking kern.py...ERROR')
            print("Checking kern.py...ERROR")
            os.system("curl https://updatepakager.legamer4.repl.co/systpak/kern-new.py > kern.py")
            await channel.send('Downloaded kern.py...100%')
            print("Downloaded kern.py...100%")
            os.system('mv kern-new.py kern.py')
            os.system('clear')
            await channel.send('Rebooting...')
            print("Rebooting...")
            os.system("python3 main.py")
            break;


@client.event
async def on_ready():
  print("hey")

client.loop.create_task(my_background_task())
client.run(token)