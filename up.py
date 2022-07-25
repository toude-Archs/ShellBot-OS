import os
import discord

client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763
id1=967120400003780611

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id1) # replace with channel_id
    while not client.is_closed():
        await channel.send('Stage 1 / 1 (Installing the update)')
        print("Stage 1 / 1 (Installing the update)")
        os.system("clear")
        os.system("rm main.py")
        os.system("rm reb.py")
        os.system("rm kern.py")
        os.system("rm keep_alive.py")
        os.system("rm krn_temp.py")
        os.system("rm syst.py")
        os.system("rm cdrom.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/main-new.py > main.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/reb-new.py > reb.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/kern-new.py > kern.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/bios-new.py > bios.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/keep_alive-new.py > keep_alive.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/syst-new.py > syst.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/cdrom-new.py > cdrom.py")
        os.system("curl https://updatepakager.legamer4.repl.co/systpak/knet-new.py > knet.py")
        await channel.send('Updated')
        print("Updated")
        os.system("clear")
        os.system('python3 main.py')
        break;

async def my_background_task2():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
        await channel.send('-=Update Log=-\nStage 1 / 1 (Installing the update)')
        await channel.send('Updated')
        break;


@client.event
async def on_ready():
    print('Updater is updating..')

client.loop.create_task(my_background_task())
client.loop.create_task(my_background_task2())
client.run(token)