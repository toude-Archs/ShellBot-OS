#made by LeGamer,iplux,quetin72000, YOmi, kokolor
#goulex le bg (goulatex) ist my repo for the updater ist here ist pul the updated code for the bot 
#ELIP4444 et passer par la :)

from keep_alive import keep_alive
from datetime import datetime
import discord
import requests
import platform
import os
import json
import shutil
import multiprocessing
import psutil

client = discord.Client()
token = open("TOKEN.txt","r").readline()
id=967120742464499763
ver: str = "3.1r"
core: str = multiprocessing.cpu_count()
ram: str = psutil.virtual_memory()[2]
avram: str = psutil.virtual_memory()[1]
osn: str = os.name
osk: str = platform.system()
oskv: str = platform.release()
CPU_Pct: str = str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
      await channel.send('Starting the Shell...OK\nStarting up Bot Module....')
      print("Starting the Shell...OK\nStarting up Bot Module....")
      break;
      
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2fG" % (G)
        else:
            return "%.2fM" % (M)
    else:
        return "%.2fkb" % (kb)
usage = shutil.disk_usage("/")
free_space = formatSize(usage[2])

total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
  

client = discord.Client()


async def my_background_task2():
    await client.wait_until_ready()
    channel = client.get_channel(id) # replace with channel_id
    while not client.is_closed():
      await channel.send('Starting up bot module...OK')
      print("Starting up bot module...OK")
      break;
  
client.loop.create_task(my_background_task())
client.loop.create_task(my_background_task2())
@client.event
async def on_ready():
#le chargement
    channel = client.get_channel(id)
    os.system('clear')
    print("Welcome on ShellOS!")
    await channel.send('Welcome on ShellOS!')
    print(f"Ver {ver}")
    await channel.send(f"Ver {ver}")
    print("-------------------")
    await channel.send("-------------------")
    PATH = './Userfolder'
    print("Setting up in Userfolder...")
    await channel.send("Setting up in Userfolder...")
    if os.path.isdir(PATH) and os.access(PATH, os.R_OK):
        os.chdir('Userfolder/')
        print("Setting up in Userfolder...Done\nSystem started")
        await channel.send("Setting up in Userfolder...Done\nSystem Started")

    else:
        print("Setting up in Userfolder...ERROR")
        await channel.send("Setting up in Userfolder...ERROR")
        os.makedirs("./Userfolder")
        print("Userfolder folder created...")
        await channel.send("Userfolder folder created...")
        os.chdir('Userfolder/')
        print("Userfolder folder created...OK\nRebooting...")
        await channel.send("Userfolder folder created...OK\nRebooting...")
        os.system("python reb.py")

#pour les commande  
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send('-=System Help =- \n$help: See disponible commands. \n$time: To see the time and date.\n$dir: Directory command. \n$session: To see your session. \n$botsession: To see bot session. \n$echo: To show your argument.\n$rep: To see your repertory.\n$mkdir: To make an directory or a files.\n$rmdir: To remove an directory.\n$filerm: To remove an files.\n$cd: To change your directory.\n$run: Run program via bash.\n$manual: Manual (not finish but started) explicate command for the system. \n$log: Show all updated maked. \n$dos Show info of dos.  \n$webget: Install package from an url. \n$bugk: Know bug list \n$update: Update all and relisting server for repo. \n$reboot: Reboot the system. \n$startcom: Run command.\n$upinstall: Install updated version of updater or reinstall it\n$credit: Show the credit of the os. \n$disk: For see disk space avalible.\n$fetch: fetch the server information. \n$source: For anyone want to help or create thier own distro of ShellOS\n$unzip: Unzip file. \n$info Show info about the sever and other thing.')
  
    if message.content.startswith('$source'):
        await message.channel.send("the source of the bot:http://updatepakager.legamer4.repl.co/package/btsc.zip")
    
    if message.content.startswith('$fetch'):
        await message.channel.send(f" CPU: {CPU_Pct}% \n CPU Core: {core} \n ram usage: {ram}% \n ram free: {avram}B \n free space: {free_space} \n os name: {osn} \n os kernel: {osk} \n kernel version: {oskv} \n -=fetch version beta=-")

    if message.content.startswith('$reboot'):
        await message.channel.send('rebooting..')
        os.chdir("..")
        os.system("python reb.py")
    
    if message.content.startswith('$dir'):
        dir = os.listdir()
        await message.channel.send(dir)
    
    if message.content.startswith('$ls'):
        dir = os.listdir()
        await message.channel.send(dir)

    if message.content.startswith('$session'):
        await message.channel.send('Your session is :'+ message.author.display_name )
  
    if message.content.startswith('$info'):
      await message.channel.send('-=info command=-\n link of discord bot:https://discord.com/api/oauth2/authorize?client_id=810549974814294057&permissions=0&scope=bot')

    if message.content.startswith('$botsession'):
        await message.channel.send('The server session is {0.user}'.format(client))

    if message.content.startswith('$time'):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        await message.channel.send('The actual date/time is: \n' + dt_string)
  
    if message.content.startswith('$echo'):
        await message.channel.send(message.content[5:].format(message))
    
    if message.content.startswith('$rep'):
      getcwd = os.getcwd() 
      await message.channel.send('Actual repertory:\n' + getcwd)

    if message.content.startswith('$mkdir'):
      os.makedirs(message.content[7:].format(message))
      await message.channel.send (message.content[7:].format(message) + " directory made.") 
    
    if message.content.startswith('$bugk'):
      await message.channel.send ("-=Know bug list=-\n no bug found \n-=You can submit bug to LeGamer#8130=-")
    
    if message.content.startswith('$unzip'):
      await message.channel.send ("extracting " + message.content[7:].format(message))
      os.system("unzip" + message.content[6:].format(message))
      await message.channel.send ("file " + message.content[6:].format(message) + " extracted")
      
    if message.content.startswith('$credit'):
      await message.channel.send ("Developped by iplux legamer quetin72000 kokolor and continued by legamer only")

    if message.content.startswith('$filerm'):
      os.system('rm ' + message.content[8:].format(message))
      await message.channel.send (message.content[8:].format(message) + " file DELETED.") 

    if message.content.startswith('$rmdir'):
      shutil.rmtree(message.content[7:].format(message))
      await message.channel.send (message.content[6:].format(message) + " directory removed.")


    if message.content.startswith('$cd'):
      os.chdir(message.content[4:].format(message))
      await message.channel.send ("You changed your directory to: " + message.content[4:].format(message))
    
    if message.content.startswith('$upinstall'):
      await message.channel.send ("Installing..")
      os.chdir("..")
      os.system('rm up.py')
      os.system('curl https://updatepakager.legamer4.repl.co/up-new.py > up.py')
      os.chdir("Userfolder")
      await message.channel.send ("Done")

    if message.content.startswith('$run'):
      if message.content[4:] == "":
        await message.channel.send("[!]:You can't run this command without an argument!")
        return

        await message.channel.send("[!]:You can't run this command like that")
        return
      if message.content[4:] == " sh":
        await message.channel.send("[!]:You can't run this command like that")
        return

      if message.content[4:] == " pause":
        await message.channel.send("[!]:You can't run this command like that")
        return
      if message.content[4:] == " yes":
        await message.channel.send("[!]:You can't run this command like that")
        return
      if message.content[4:] == " yes " + message.content[8:].format(message):
        await message.channel.send("[!]:You can't run this command like that")
        return
      os.system('bash ' + message.content[4:].format(message))
      await message.channel.send ("files: " + message.content[4:].format(message) + " stoped sucsesfully.")
    
    if message.content.startswith('$startcom'):
      if message.content[4:] == " bash":
        await message.channel.send("[!]:You can't run this command like that")
        return
      if message.content[4:] == " sh":
        await message.channel.send("[!]:You can't run this command like that")
        return
      if message.content[4:] == " pause":
        await message.channel.send("[!]:You can't run this command like that")
        return
      if message.content[4:] == " yes":
        await message.channel.send("[!]:You can't run this command like that")
        return
      if message.content[4:] == " yes " + message.content[8:].format(message):
        await message.channel.send("[!]:You can't run this command like that")
        return
      os.system(message.content[9:].format(message))
      await message.channel.send ("files: " + message.content[9:].format(message) + " is running or is stoped.")

    if message.content.startswith('$manual'):
      await message.channel.send ('-=Manual =-\n$run:Run programs via bash \n$mkdir/rmdir:For mkdir max type is 7 character for rmdir del file or folder before named ex test or test.txt\n$log:show update\n$install:install package frome the web\n$webget:get an pakage from an url\n$unzip you download an zip file from $webget then you type the file and type $unzip for unzip it')
    
    if message.content.startswith('$dos'):
      getcwd = os.getcwd() 
      await message.channel.send ('-=ShellOS dos system ver ' + ver + "=-\ncurrent directory: " + getcwd)
    
    if message.content.startswith('$log'):
      await message.channel.send ('ub030521: System updated with the release of the system in 1.5\n ub050521: Major bios update\n ub060521: System and command update\n ub080521: Correcting a glicth in command dir\n ub300521: New edit system and new system release\n ub050721: Rewriting editor and upgrading the dos\n ub150721: Adding new feature like webget unzip and install and upgrading open and rm command\n ub091021: Rewriting the updater script with a live updater\n ub081121: Add and remove command added credit bugk removed command unzip\n ub101121: Adedding new command disk\n ub111121: Addeding new log chanel com0\n ub051221: Addeding new ucpu command\n ub061221: Addeding new fastreb command for fast rebooting\nub020122: Removing the run bug for for information see bugk and addeding the source command\nub070122: Addeding the kernel check in the firmware (will check if all component are working)\nub080122: Addeding the bios loader\nub110822: Addeding the testing file protocol\nub149122: Updating the bios loader\nub150122: An major update for updating a serious security bug has been fixed for anyone have the old code of the ShellOS please download  the leastest version and removing the sysinfo progam\nub210122: Addeding the unzip command\nub300122: Migreting the bot source code to the official ShellOS repo\nub250322: Optimizing the bot code\nub300322: Updating VKbios and the updater\nub030422: Upgrading boot file checker\nub300622: $fastreb has been changed as $reboot and some code optimisation removing the command ucpu by fetch and for the time install is now remove temporaly for testing\nub040722: temporaly disable webget beacause of missing wget the program will be adapted to be used as curl and wget (you can use $startcom curl your url > your file name)\nub230722: upgrading firmware and addeding custom os suport')

    if message.content.startswith('$disk'):
      await message.channel.send (f'free space: {free_space}')
    
    if message.content.startswith('$webget'):
      await message.channel.send ("for using this command do $startcom curl (your url)>(your file name).(your extention)")
 #     await message.channel.send ('Installing via url...')
 #     os.system('wget ' + message.content[5:].format(message))
 #     await message.channel.send ('Installed sucsesfully')

    if message.content.startswith('$update'):
      await message.channel.send ('Updating...')
      os.chdir('..')
      os.system('python3 up.py')


keep_alive()

client.run(token)