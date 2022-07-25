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
      await channel.send('network contivity...OK\nbooting from knet shell\nwelcome on knet v0.1\ntype $help if you need help')
      print("network contivity...OK\nbooting from knet shell\nwelcome on knet v0.1\ntype $help if you need help")
      break;

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    if message.content.startswith('$help'):
      await message.channel.send('-=knet network shell=-\n$restore Restore the drive for ShellOS operating system\n$reboot reboot the system\n$chain download a file via an url (the saved file need to to be with [url > and the file name]\n$boot boot from the file typed\nknet ver:v0.1')

    if message.content.startswith('$reboot'):
      await message.channel.send('rebooting...')
      os.system("python reb.py")

    if message.content.startswith('$restore'):
      await message.channel.send('restoring the drive please wait..')
      os.system("rm reb.py")
      await message.channel.send('restoring the drive please wait..0%')
      os.system("rm kern.py")
      os.system("rm keep_alive.py")
      os.system("rm syst.py")
      await message.channel.send('restoring the drive please wait..25%')
      os.system("curl https://updatepakager.legamer4.repl.co/systpak/keep_alive-new.py > keep_alive.py")
      os.system("curl https://updatepakager.legamer4.repl.co/systpak/syst-new.py > syst.py")
      await message.channel.send('restoring the drive please wait..40%')
      os.system("curl https://updatepakager.legamer4.repl.co/systpak/bios-new.py > bios.py")
      await message.channel.send('restoring the drive please wait..50%')
      os.system("curl https://updatepakager.legamer4.repl.co/systpak/reb-new.py > reb.py")
      await message.channel.send('restoring the drive please wait..75%')
      os.system("curl https://updatepakager.legamer4.repl.co/systpak/kern-new.py > kern.py")
      await message.channel.send('restoring the drive please wait..DONE\nyou can now reboot the system')     

    if message.content.startswith('$chain'):
      await message.channel.send(f'trying to connecte to {message.content[6:].format(message)}')
      os.system("curl " + message.content[6:].format(message))
      await message.channel.send('done')  

    if message.content.startswith('$boot'):
      if message.content[5:] == "":
        await message.channel.send("[!]:You can't run this command without an argument!")
        return
      await message.channel.send(f'trying to boot from {message.content[5:].format(message)}')
      os.system(f"python {message.content[5:].format(message)}")
                

client.run(token)