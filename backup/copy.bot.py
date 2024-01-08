import discord
from discord.ext import commands
import random
import platform
import datetime
import psutil
import os
import aiohttp
import ipaddress
import logging
import requests
from redbot.pytest.core import ctx
import time
import urllib
import subprocess
import io
from redbot.core.utils import embed
from redbot.core.utils import embed
from discord import message, role, user

logging.basicConfig(level=logging.INFO)


print("Starting bot...")

client = discord.Client()

TOKEN = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '>')
START_TIME = datetime.datetime.utcnow()

@client.event
async def on_ready():
    print('Logged in as username %s with user ID %s' % (client.user.name, client.user.id))
    activity = discord.Activity(name="Replays Commands | >help",
                                type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    print('----------------------------------------')

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor



@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)  # set a 5 second cooldown for each command per user
async def botinfo(ctx):
    """Displays information about the bot."""

    embed = discord.Embed(
        title="Bot Information",
        description="Detailed information about the bot",
        color=10181046,
        timestamp=datetime.datetime.utcnow()
    )

    current_process = psutil.Process(os.getpid())

    # The process CPU utilization can be > 100.0 if a process is running multiple threads on different CPUS,
    # so divide by the number of threads currently used
    cpu_usage = current_process.cpu_percent(interval=1) / current_process.num_threads()

    mem = psutil.virtual_memory()
    memory_usage = current_process.memory_info().rss

    # Bytes to megabytes
    memory_usage_mb = memory_usage / (2 ** 20)
    total_memory_mb = mem.total / (2 ** 20)

    discord_py_version = discord.__version__
    python_version = platform.python_version()

    system = platform.system()

    
    latency_ms = client.latency * 1000

    now = datetime.datetime.utcnow()
    difference = now - START_TIME

    hours, remainder = divmod(int(difference.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    time_format = "{d} days, {h} hours, {m} minutes, and {s} seconds." if days \
        else "{h} hours, {m} minutes, and {s} seconds."
    timestamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

    embed.add_field(name='Owner', value='`Replays#0002`', inline=True)
    embed.add_field(name='Developer', value='`Replays#0002`', inline=True)
    embed.add_field(name='CPU Usage', value='`{0:.2f}%`'.format(cpu_usage), inline=True)
    embed.add_field(name="RAM Usage", value='`%d/%d MB`' % (memory_usage_mb, total_memory_mb), inline=True)
    embed.add_field(name='Platform', value='`{}`'.format(system), inline=True)
    embed.add_field(name='Discord.py Version', value='`{}`'.format(discord_py_version), inline=True)
    embed.add_field(name='Python Version', value='`{}`'.format(python_version), inline=True)
    embed.add_field(name='API Latency', value='`{:d} ms`'.format(round(latency_ms)), inline=True)
    embed.add_field(name='Uptime', value='`{}`'.format(timestamp), inline=True)

    embed.set_footer(text="Benis", icon_url=client.user.avatar_url)

    await ctx.send("", embed=embed)
 


@client.command()
async def ping(ctx):
    embed = discord.Embed(title=f":ping_pong: Pong! {round (client.latency * 1000)}ms", color=10181046)
    await ctx.message.delete()
    await ctx.send(embed=embed)
    


@client.command()
async def quotes(ctx):
    await ctx.message.delete()
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

@client.event
async def on_command_error(ctx, error):
    await ctx.message.delete()
    embed = discord.Embed(title=f"Error. Try >help ({error})", color=10181046)
    await ctx.send(embed=embed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(pass_context=True)
async def pscan(ctx, ip):

        portscanurl = ("https://api.hackertarget.com/nmap/?q="+ip)
        response = requests.get(portscanurl)
        embed = discord.Embed(title="Port Scan <3", description="%s"%(response.text), color=10181046)
        embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed)
        await ctx.message.delete()


@client.command()
async def penis(ctx, *, user: discord.Member = None): 
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    embed = discord.Embed(title=f"{user.name}'s Dick Size :heart:", description=f"8{dong}D", color=10181046)
    embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    await client.logout()


@client.command()
async def boot(ctx):
    await ctx.message.delete()
    await ctx.send("Booting You Offline.")
    time.sleep(1)
    await ctx.send("**3**")
    await ctx.send("**2**")
    await ctx.send("**1**")
    time.sleep(1)
    await ctx.send("`Nigga you Offline.`")


@client.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@client.command()
async def joke(ctx):  
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])   

@client.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)

async def get_ip_type(ip_address: str):
    ip = ipaddress.ip_address(ip_address)
    ip_type = None

    if ip.is_global:
        ip_type = 'global'
    if ip.is_loopback:
        ip_type = 'loopback'
    elif ip.is_multicast:
        ip_type = 'multicast'
    elif ip.is_reserved:
        ip_type = 'reserved'
    elif ip.is_private:
        ip_type = 'private'

    return ip_type


async def ip_info(ip_address: str):
    """Fetches info for an IP address."""

    ip_type = await get_ip_type(ip_address)

    if ip_type != 'global':
        raise ValueError('IP address is {}'.format(ip_type))

    async with aiohttp.ClientSession() as session:
        response = await session.get('http://ip-api.com/json/' + ip_address, timeout=10)
        data = await response.json()

    if data['status'] != 'success':  # something went wrong
        raise RuntimeError('Failed querying IP address ' + ip_address + ': ' + data['status'])

    return data

async def proxy_vpn_detect(ip_address: str):
    """Checks to see if an IP address is a proxy or VPN"""

    ip_type = await get_ip_type(ip_address)

    if ip_type != 'global':
        raise ValueError('IP address is {}'.format(ip_type))

    auth_header = {
        'X-Key': ' NTYwNjphcGpmODRYMWJ2YkpNNXpGME1WbEpNSUt2UzZSZkNPaA=='
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get('https://v2.api.iphub.info/ip/' + ip_address, headers=auth_header, timeout=10)
        if response.status != 200:  # HTTP OK
            raise RuntimeError('Failed quering IP address: Received HTTP status ' + response.status)

        data = await response.json()
        return data


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)  # set a 5 second cooldown for each command per user
async def lookup(ctx, ip_address: str):
    """Fetches info for an IP address."""
    try:
        data = await ip_info(ip_address)
    except Exception as e:
        embed = discord.Embed(title="IP Lookup Error", color=10181046, timestamp=datetime.datetime.utcnow())
        embed.add_field(name='Error', value=str(e))
        embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
        await ctx.send("", embed=embed)
        return

    embed = discord.Embed(title="IP Lookup Results for {}".format(ip_address), color=10181046,
                          timestamp=datetime.datetime.utcnow())
    for key, value in data.items():
        # You can't send embeds with empty values so the value becomes 'N/A' instead of null
        # If you try sending a field with an empty value, the entire message won't get sent
        embed.add_field(name=(key if key else 'N/A'), value=str(value) if value else 'N/A', inline=True)

    embed.set_footer(text="Benis", icon_url=client.user.avatar_url)

    await ctx.send("", embed=embed)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def is_residential(ctx, ip_address: str):
    """Checks to see if the IP address is a VPN or proxy"""

    try:
        data = await proxy_vpn_detect(ip_address)
    except Exception as e:
        embed = discord.Embed(title="Detection Error", color=10181046, timestamp=datetime.datetime.utcnow())
        embed.add_field(name='Error', value=str(e))
        embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
        await ctx.send("", embed=embed)

    embed = discord.Embed(title="IP Lookup Results for {}".format(ip_address), color=10181046,
                          timestamp=datetime.datetime.utcnow())
    if data['block'] == 1:
        embed.add_field(name="Results",
                        value=":chains: IP has been identified as a non-residential IP, "
                              "such as a hosting provider or proxy",
                        inline=True)
    else:
        embed.add_field(name="Results", value=":house: IP has been identified as a residential or business IP",
                        inline=True)
    embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
    await ctx.send("", embed=embed)


@client.command()
async def tits(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Gives {member.name} Titties :heart:", color=10181046)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
    await message.send(embed=embed)

@client.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
        embed = discord.Embed(title=f"User Info <3", color=10181046)
        embed.add_field(name="`User ID:`", value=member.id, inline=True)
        embed.add_field(name="`Name:`", value=member.display_name, inline=True)
        embed.add_field(name="`Creation Date:`", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=True)
        embed.add_field(name="`Bot Check`", value=member.bot, inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="Server Info :heart:", color=10181046)
        embed.add_field(name="`Server ID:`", value=ctx.guild.id, inline=True)
        embed.add_field(name="`Server Name:`", value=ctx.guild.name, inline=True)
        embed.add_field(name="`Server Owner:`", value=ctx.guild.owner.display_name, inline=True)
        embed.add_field(name="`Creation Date:`", value=ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=True)
        embed.add_field(name="`Members:`", value=len(ctx.guild.members), inline=True)
        embed.add_field(name="`Roles:`", value=len(ctx.guild.roles), inline=True)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
        await ctx.send(embed=embed)        

@client.command()
async def slap(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Slaps TF Outta {member.name} :heart:", color=10181046)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
    await message.send(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


@client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))

@client.command()
async def pussy(message, member: discord.Member = None):
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json() 
    embed = discord.Embed(title=f"{message.author.name} Gives {member.name} Coochie :heart:", color=10181046)
    embed.set_image(url=res['url'])
    embed.set_footer(text="Benis", icon_url=client.user.avatar_url)
    await message.send(embed=embed)

@client.command()
async def on_member_join(member, ctx):
    for channel in member.guild.channels:
        if str(channel) == "735194439928119347":
            embed = discord.Embed(color=10181046)
            embed.add_field(name="Welcome", value=f"{member.name} has joined {member.guild.name}", inline=True)
            embed.set_image(url="https://64.media.tumblr.com/01143f5e6b42246d40e5c820700531bb/tumblr_pioavsk5oX1rqp6teo1_500.gifv")
            await channel.send(embed=embed)

#We delete default help command
client.remove_command('help')
#Embeded help with list and details of commands
@client.command(pass_context=True)
async def help(ctx, member: discord.Member = None):
    embed = discord.Embed(
        color = discord.Color.purple())
    embed.set_author(name='⋆ Help ⋆ : List of Commands Available',)
    embed.add_field(name='>admin', value='Shows Admin Commands', inline=True)
    embed.add_field(name='>fun', value='Shows Fun Commands', inline=True)
    embed.add_field(name='>tools', value='Shows Tool Commands', inline=True)
    embed.add_field(name='>nsfw', value='Not Safe For Work Commands', inline=True)
    embed.set_footer(text=f"Commands requested by {ctx.author.display_name}", icon_url=client.user.avatar_url,)
    await ctx.send(embed=embed)
    

@client.command(pass_context=True)
async def admin(ctx):
    embed = discord.Embed(
        color = discord.Color.purple())
    embed.add_field(name='>purge', value='Clear A Specific Amount of Messages', inline=True)
    embed.add_field(name='>clearall', value='Clears All Messages', inline=True)
    embed.set_footer(text=f"Commands requested by {ctx.author.display_name}", icon_url=client.user.avatar_url,)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def fun(ctx):
    embed = discord.Embed(
        color = discord.Color.purple())
    embed.add_field(name='>penis', value='Shows Penis Size of User', inline=True)
    embed.add_field(name='>boot', value='Boot User Offline LOL', inline=True)
    embed.add_field(name='>joke', value='Converts Text to Ascii', inline=True)
    embed.add_field(name='>8ball', value='Magic 8Ball :)', inline=True)
    embed.add_field(name='>slap', value='Slaps Tagged User', inline=True)
    embed.set_footer(text=f"Commands requested by {ctx.author.display_name}", icon_url=client.user.avatar_url,)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def tools(ctx):
    embed = discord.Embed(
        color = discord.Color.purple())
    embed.add_field(name='>ascii', value='Converts Text to Ascii', inline=True)
    embed.add_field(name='>whois', value='Shows You Information on a Specific Host', inline=True)
    embed.add_field(name='>pscan', value='Port Scans A Specific Host', inline=True)
    embed.add_field(name='>lookup', value='Shows Info On Looked Up IP', inline=True)
    embed.add_field(name='>info', value='Shows Info On User', inline=True)
    embed.add_field(name='>serverinfo', value='Shows Server Information', inline=True)
    embed.set_footer(text=f"Commands requested by {ctx.author.display_name}", icon_url=client.user.avatar_url,)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def nsfw(ctx):
    embed = discord.Embed(
        color = discord.Color.purple())
    embed.add_field(name='>tits', value='Shows Tagged User Some Tits', inline=True)
    embed.add_field(name='>pussy', value='Shows Tagged User Some Coochie', inline=True)
    embed.set_footer(text=f"Commands requested by {ctx.author.display_name}", icon_url=client.user.avatar_url,)
    await ctx.send(embed=embed)


    

client.run(TOKEN)