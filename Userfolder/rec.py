import os
import discord

client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763
PATH = './kern.py'
PATH2 = './keep_alive.py'
PATH3 = './kern.py'

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
      await channel.send(':: starting recovery environement')
      print(":: starting recovery environement")
      await channel.send(':: cheking module')
      print(":: cheking module")
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            await channel.send(':: Checking kern.py...OK')
            print(":: Checking kern.py...OK")
            break;
        else:
            await channel.send(':: Checking kern.py...ERROR')
            print(":: Checking kern.py...ERROR")
            os.system("curl https://updatepakager.legamer4.repl.co/systpak/kern-new.py > kern.py")
            await channel.send('Downloaded kern.py...100%')
            print("Downloaded kern.py...100%")
            os.system('mv kern-new.py kern.py')
            os.system('clear')
            break;
        if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
            await channel.send('Checking keep_alive.py...OK')
            print("Checking keep_alive.py..OK")
            os.system('clear')
            os.system("python3 kern.py")
            break;
        else:
            await channel.send('Checking keep_alive.py...ERROR')
            print("Checking keep_alive.py...ERROR")
            os.system("curl https://updatepakager.legamer4.repl.co/systpak/keep_alive-new.py > keep_alive.py")
            await channel.send('Downloaded reb.py...100%')
            print("Downloaded reb.py...100%")
            os.system('mv keep_alive-new.py keep_alive.py')
            os.system('clear')
        if os.path.isfile(PATH3) and os.access(PATH3, os.R_OK):
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
        await channel.send(':: module checked\n:: dowwnloading recovery update file')
        print(":: module checked\n:: dowwnloading recovery update file")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/rec-up-new.py > rec-up.py")
        print(":: file downloaded\n:: starting recovery update")
        os.system("python3 rec-up.py")


@client.event
async def on_ready():
  print("hey")