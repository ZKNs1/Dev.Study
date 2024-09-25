import discord
import random
import aiohttp
from discord.ext import commands

# Configuração do bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento quando o bot está pronto
@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está pronto para uso!')

# Evento quando um membro entra no servidor
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='bem-vindo')
    if channel:
        await channel.send(f'Bem-vindo ao servidor, {member.mention}!')

# Comando simples
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Olá! Eu sou o bot do Dev. Study, criado por _ytrnhx!')

# Comando de reação
@bot.command(name='react')
async def react(ctx):
    await ctx.message.add_reaction('👍')

# Comando de cálculo
@bot.command(name='soma')
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f'O resultado de {a} + {b} é {result}.')

# Comando de informações do servidor
@bot.command(name='serverinfo')
async def serverinfo(ctx):
    guild = ctx.guild
    num_members = guild.member_count
    server_name = guild.name
    await ctx.send(f'O servidor {server_name} tem {num_members} membros.')

# Comando mencionando alguém específico
@bot.command(name='test')
async def mention_specific(ctx):
    user_id = #ID do usuário;
    user = await bot.fetch_user(user_id)
    await ctx.send(f'O {user.mention} é legal!')

# Rolar um dado
@bot.command(name='dado')
async def roll(ctx, sides: int):
    if sides < 1:
        await ctx.send("O número de lados deve ser maior que 0.")
        return
    
    result = random.randint(1, sides)
    await ctx.send(f'Você rolou um dado de {sides} lados e obteve {result}.')

# Acertar número
@bot.command(name='adivinhe')
async def guess(ctx, number: int):
    secret_number = random.randint(1, 10)
    
    if number == secret_number:
        await ctx.send(f'Parabéns! Você adivinhou o número {secret_number}!')
    else:
        await ctx.send(f'Errado! O número era {secret_number}. Tente novamente!')

# Comando para pesquisar um termo
@bot.command(name='pesquisa')
async def wiki(ctx, *, search_term):
    url = f"https://pt.wikipedia.org/api/rest_v1/page/summary/{search_term.replace(' ', '_')}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            if 'title' in data and 'extract' in data:
                title = data['title']
                extract = data['extract']
                await ctx.send(f"**{title}**\n{extract}")
            else:
                await ctx.send("Não encontrei informações sobre isso.")

# Comando que retorna o link para o servidor
@bot.command(name='servidor')
async def hello(ctx):
    await ctx.send(f'Este é o link de convite para nosso servidor https://discord.gg/HvBbJvVbQ5')

@bot.command(name='comandos')
async def comandos(ctx):
    message = (
        "**Comandos Disponíveis:**\n\n"
        "**1. !dado <lados>**\n"
        "   Rola um dado com a quantidade de lados que você escolher. Por exemplo, `!dado 6` para um dado de 6 lados.\n\n"
        "**2. !adivinhe <número>**\n"
        "   O bot pensa em um número entre 1 e 10 e você deve acertar para ganhar. Por exemplo, `!adivinhe 5`.\n\n"
        "**3. !serverinfo**\n"
        "   Retorna o nome do servidor e o número de membros.\n\n"
        "**4. !soma <número1> <número2>**\n"
        "   Soma dois números que você escolher. Por exemplo, `!soma 5 10`.\n\n"
        "**5. !hello**\n"
        "   O bot faz uma pequena apresentação sobre ele mesmo.\n\n"
        "**6. !servidor**\n"
        "   Disponibiliza o link de convite para o servidor.\n\n"
        "**7. !pesquisa <tópico>**\n"
        "   Faz uma pesquisa na Wikipedia sobre o tópico que você escolher. Por exemplo, `!pesquisa Python`."
    )

bot.run('token')
