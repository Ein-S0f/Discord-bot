import discord
import pandas
from discord.ext import commands
import random
import os


client = commands.Bot(command_prefix="--")

token = 'NzYzNjgzMzkxODI0NDYxODM0.X37RlQ.OThvhWshuustNFjGaagFtQEWcbg'

# 763749597515743262   763601924758306851 -------------These are the two channels (bot_test, general)


@client.command(name="version")
async def version(context):
    general_channel = client.get_channel(763749597515743262)
    version_embed = discord.Embed(title="Current Version", description="This is the first version/iteration", color=0x00ff00)
    version_embed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    version_embed.add_field(name="Date Released:", value="October 08, 2020", inline=False)
    version_embed.set_author(name="Wulfsbane")
    await context.message.channel.send(embed=version_embed)



@client.command(name="ping")
async def ping(context):
    general_channel = client.get_channel(763749597515743262)
    await context.send(f"Ping: {round(context.bot.latency * 1000)}")

@client.command(name="kick")
async def kick(ctx, member : discord.Member, *, reason=None):
    general_channel = client.get_channel(763749597515743262)
    await member.kick(reason=reason)

@client.command(name="ban")
async def ban(ctx, member : discord.Member, *, reason=None):
    general_channel = client.get_channel(763749597515743262)
    await member.ban(reason=reason)

@client.event
async def on_member_join(context, member : discord.Member):
    general_channel = client.get_channel(763601924758306851)
    await context.send("Why hello there!")

@client.event
async def on_ready():
    general_channel = client.get_channel(763601924758306851)
    # await general_channel.send(f'{client.user} Has joined. PLease be nice to them')
    await client.change_presence(activity=discord.Game("Suthy's Mutha"), status=discord.Status.do_not_disturb)
    
    
    # df = pd.DataFrame({"A": []})
    # df.to_csv("/home/sergei/PycharmProjects/pythonProject/output.csv")





'''
@client.event
async def on_disconnect():
    general_channel = client.get_channel(76360192475830685)
    print("CYA nerds")
'''
@client.event
async def on_message(message):
    if message.content == ("!DM"):
        await message.author.send("This is my test DM")
        '''
    if message.content == "Append":
        df = pd.read_csv("PLace filepath to csv file here", index_col=0)
        df.append({"A": })
    '''
    await client.process_commands(message)




@client.event
async def on_member_join():
    general_channel = client.get_channel(763601924758306851)
    # await general_channel.send(f'{client.user} Has joined. PLease be nice to them')
    await general_channel.send(f'A new fuckboi has joined and their name is  + {client.user}')



client.run(token)