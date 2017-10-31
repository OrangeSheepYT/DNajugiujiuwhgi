import discord
import asyncio
import math
import os
import random
import requests
import time
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_extensions = ['Music']

class Main_Commands():
        def __init__(self, bot):
         self.bot = bot

Client = discord.Client()
bot_prefix= "~"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Dank Memez Loading...")
    print("Welcome My Lord DankMemez")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Extra 1
    await client.change_presence(game=discord.Game(name='~about | https://discord.gg/p5wBxQS '))
    
client.remove_command("help")
client.remove_command("HelpFormatter")

@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(title = "Help", description = ("""
  help Shows this message.
  eightball  Talk to the bot!
  inviteme Invite the bot to your server!
  servers Show what servers DankBot is in.
  dm  Dm a user (Bot owner only)
  em  Make a embed message!
  getbans Get the bans of the current server
  about About me! :D 
  prefix My Prefix!
  owner DankBot's Owners
  clear Clear messages!
  meme      Random Memes
  stream    Sets the streaming status with the specified name
  
  + DankBot is now 24/7! :D
  
  Any Issues with DankBot? Contact `Squazy#6883` Or `Heads#1424`
  partners"""), color = 0xFF0000)
    return await client.say(embed = embed) 

@client.command(pass_context = True, aliases=['sinfo', 'si'])
async def serverinfo(ctx):
        server = ctx.message.server
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles);
        channels = len(server.channels);
        time = str(server.created_at); time = time.split(' '); time= time[0];

        embed = discord.Embed(description= "Info on this server",title = ':thinking:', colour = {0xFF0000});
        embed.set_thumbnail(url = server.icon_url);
        embed.add_field(name = '__Server __', value = str(server))
        embed.add_field(name = '__Server ID__', value = str(server.id))
        embed.add_field(name = '__Owner__', value = str(server.owner));
        embed.add_field(name = '__Owner ID__', value = server.owner.id)
        embed.add_field(name = '__Members__', value = str(server.member_count));
        embed.add_field(name = '__Text/Voice Channels__', value = str(channels));
        embed.add_field(name = '__Roles__', value = '%s'%str(role_length));
        embed.add_field(name = '__Server Region__', value = '%s'%str(server.region));
        embed.add_field(name = '__AFK Timeout__', value = server.afk_timeout +'seconds');
        embed.add_field(name = '__AFK Channel__', value = server.afk_channel);
        embed.add_field(name = '__Verification Level__', value = server.verification_level)
        embed.add_field(name = '__Created on__', value = server.created_at.__format__('Date - %d %B %Y at time - %H:%M:%S'));
        
        return await client.say(embed = embed);

@client.command(pass_context = True, aliases=['8ball'])
async def eightball(ctx):
    result = [' nah m8, It is certain', ' As I see it, yes', ' Reply hazy try again', ' Dont count on it', ' It is decidedly so', ' Most likely', ' Ask again later', ' My reply is no', ' Without a doubt', ' Outlook good',' Better not tell you now',' My sources say no',' Yes definitely',' Yes',' Cannot predict now',' Outlook not so good',' You may rely on it',' Signs point to yes',' Concentrate and ask again',' Very doubtful']
    choice = random.choice(result)
    await client.say(choice)
 
@client.command(pass_context = True)
async def inviteme(ctx):
    embed = discord.Embed(title = "Invite DankBot", description = ("""
***Hello there my name is*** `Dank Bot` as you all know there are some bot users in discord, one of those is me. 
I'm made by Squazy#6883 and Heads#1424
+ DankBot is now 24/7! :D
Invite me here: https://discordapp.com/api/oauth2/authorize?client_id=373477442079162369&scope=bot&permissions=1
"""), color = 0xFF0000)
    return await client.say(embed = embed)   


@client.command(pass_context = True)
async def addrole(self, ctx, user: discord.Member, *, role: str):
    server_roles = [role for role in ctx.message.server.roles if not role.is_everyone]
    add = discord.utils.find(lambda m: role.lower() in m.name.lower(), ctx.message.server.roles)
    if not add:
        await self.client.say('That role doesnt exist')
    if ctx.message.author.server_permissions.manage_roles:
        try:
            await self.client.add_roles(user, add)
            await self.client.say('I gave {} the {} role'.format(user, role))
        except discord.Forbidden:
            await self.client.say('I need **Manage Roles** for this')
    else:
            await self.client.say('You need *Manage Roles** for this')

@client.command(pass_context = True)
async def servers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)    
          
@client.command(pass_context = True)
async def dm(ctx, member : discord.Member, *, message):
    if ctx.message.author.id == '374198115730849793':
        return await client.send_message(member, message)
        await client.say("Done, Boss!")
    else:
        await client.say(":warning:Nope!:warning:")

@client.command(pass_context = True)
async def em(ctx, *, text: str):
    mesg = discord.Embed(description = text, color = 0xFF000)
    await client.say(embed = mesg)
        
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFF0000)
    return await client.say(embed = embed) 


    
    
@client.command(pass_context = True)
async def about(ctx):
    embed = discord.Embed(title = "About DankBot", description = ("""
***Hello there my name is*** `Dank Bot` :robot:  as you all know there are some bot users in discord, one of those is me. 
Sooo Here are sum of mah commands:

- ***~prefix***`[ Tell you my prefix ]`

- ***~about*** `[By typing this command , all that will happen is this message , will be sent again ]`

- ***~info*** `[Gives you all info available about Dank Bot]`

- ***~owner*** `Squazy#6883 and Heads#1424 is the founders of DankBot`

- ***~invite*** `[ Gives you an invite of a partnered bot ( super useful) ]`

- ***~warn*** `[ Adds a warn to a players database]`

- ***~suggest*** `[This commands needs Squazy#6883 after you wrote your suggestion so the bot can translate it and send it to his owner. ]`

If you would like any help plz contact `@Squazy#6883 or Heads#1424`
Me `Dank Bot` will be able to contact you as soon as possible!

This bot was coded but the one and only one`@Squazy#6883` And `Heads#1424`
Thx for your time i hope you enjoy my helpful bot!"""), color = 0xFF0000)
    return await client.say(embed = embed)


 
 
@client.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    msg = "Bye Bye {0} :(".format(member.mention)
    await client.send_message(Channel, msg)
    
@client.command(pass_context = True)
async def prefix(ctx):
    embed = discord.Embed(title = "DankBot's Prefix", description = ("Oh hi there! I didnt even see you, anyways my prefix is `~`"), color = 0xFF0000)
    return await client.say(embed = embed)
  
@client.command(pass_context = True)
async def owner(ctx):
    embed = discord.Embed(title = "DankBot's Founder ", description = ("""Beep boop beep oh hi there! I was playing with my new computer anyways. I seen you wanted to know my founder? Okay!
    
    My founder is the one and only `Squazy#6883 and Heads#1424` :smile:"""), color = 0xFF0000)
    return await client.say(embed = embed)
  
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

    
@client.command(pass_context=True)
async def meme(ctx):
    """Random Memez"""
    Meme = [ 'https://imgur.com/Wh489hL', 'https://goo.gl/iJeByU', 'https://goo.gl/KdkvEy', 'https://goo.gl/dCBucV', 'https://goo.gl/h3Pgcz', 'https://goo.gl/Nm1Ppu', 'https://goo.gl/KhED74', 'https://goo.gl/6WezBG', 'https://goo.gl/4F56oc']
    choice  = random.choice(Meme)
    await client.say(choice)    

@client.command(pass_context=True)
async def stream(ctx, *, name:str):
    """Sets the streaming status with the specified name"""
    if ctx.message.author.id == '374198115730849793':
        await client.change_presence(game=discord.Game(name=name, type=1, url="https://twitch.tv/orangesheepyt"))
        await client.say("Done :heart:")
    else:
        await client.say("Nope")
    
@client.command(pass_context = True)
async def partners(ctx):
    embed = discord.Embed(title = "Partners", description = ("""Uhh what? Im here! Okay partners was requested!
    
***Partners:***
    


    """), color = 0xFF0000)
    return await client.say(embed = embed)
    
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format (extension, exc))
            
client.run("MzczNDc3NDQyMDc5MTYyMzY5.DNTTew.aSkkSY5i7hdzdCSmOLEPLJe8IqA")
