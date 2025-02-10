import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot que te indicara el tiempo de descomposición de un determinado objeto doméstico. Ejemplo: Objetos plasticos de la cocina.')

@bot.command()
async def plastic(ctx):
    await ctx.send(f'El tiempo que tarda en degradarse el plástico puede variar entre 100 y 1.000 años, dependiendo del tipo de plástico y las condiciones ambientales.')

@bot.command()
async def paper(ctx):
    await ctx.send(f'Papel: tarda entre 2 y 5 meses en degradarse completamente.')

@bot.command()
async def cardboard_box(ctx):
    await ctx.send(f'Cartón: puede tardar entre 5 meses y 1 año, dependiendo del grosor y las condiciones climáticas.')

bot.run("")