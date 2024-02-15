import discord
from discord.ext import commands
import random
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

ideas_ecologicas = [
    "1-Utiliza el transporte público. Nos hemos acostumbrado a utilizar el coche para todo, pero es hora de pensar en el planeta y en nuestro futuro y de usar medios de transporte más sostenibles y respetuosos con el medioambiente. El transporte público es una buena solución, más barata y menos contaminante que el coche"
    "2-Reduce, reutiliza y recicla: Minimiza tu consumo de productos desechables y trata de reutilizar o reciclar tanto como sea posible"
    "3-Recoger, separar y eliminar los residuos de forma segura para proteger la tierra y el agua, fomentar la reducción de sustancias nocivas para el medio ambiente y fomentar el reciclaje por parte de los ciudadanos y las empresas"
    "4-Educación y concienciación: Comparte información sobre la importancia de cuidar el medio ambiente con amigos, familiares para crear conciencia sobre la importancia de la sostenibilidad"
    "5-Hacer ladrillos ecológicos. Un Ladrillo ecológico se hace con una botella (por ejemplo) de jugo Watts de litro y medio. Después, a medida que se vayan adquiriendo productos que contengan plástico (como un paquete de galletas, una bolsa, cosas así) se van recortando con tijeras y colocando a través de la boquilla de la botella para ir llenándola. Estos ladrillos ecológicos, cuando estén llenos, pueden usarse para diversas cosas; como construir algo pequeño (una pequeña mesa por ejemplo) dependiendo de cuantos tengas. Son llamados Ladrillos ecológicos ya que cuanto más llenas estén las botellas más pesadas, duras y/o resistentes serán: como un ladrillo"]

@bot.command(description='for when you wanna settle the score for some other way')
async def ideas_ecologicas(ctx,*choices:str):
    """"Choses betwen Multiple choixces."""
    await ctx.send(random.choice(ideas_ecologicas))

bot.run('blanck') 