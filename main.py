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
    await ctx.send(f'Olá! Eu sou o bot do Dev. Study, criado por `_ytrnhx!`')

# Comando de reação
@bot.command(name='react')
async def react(ctx):
    await ctx.message.add_reaction('👍')

# Comandos de cálculos
@bot.command(name='soma')
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f'O resultado de {a} + {b} é {result}.')

@bot.command(name='sub')
async def add(ctx, a: int, b: int):
    result = a - b
    await ctx.send(f'O resultado de {a} - {b} é {result}.')

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

# Comando para criar uma enquete
@bot.command(name='enquete')
async def poll(ctx, *, question):
    message = await ctx.send(f"📊 **Enquete**: {question}")
    await message.add_reaction('👍')
    await message.add_reaction('👎')
    await message.add_reaction('🤷')

# Comando para jogar cara ou coroa
@bot.command(name='moeda')
async def coin_flip(ctx):
    moeda = random.choice(['Cara', 'Coroa'])
    await ctx.send(f'🪙 Você jogou a moeda e deu **{moeda}**!')

# Comando para escolher alguma opção
@bot.command(name='escolher')
async def choose(ctx, *choices: str):
    if len(choices) < 2:
        await ctx.send("❗ Você precisa fornecer pelo menos duas opções.")
        return
    choice = random.choice(choices)
    await ctx.send(f'Eu escolho: **{choice}**')

# Comando para mostrar avatar
@bot.command(name='avatar')
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

# Comando para apagar mensagens
@bot.command(name='limpar')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'🧹 {amount} mensagens foram apagadas!', delete_after=5)

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
        "**Comandos Disponíveis do Bot Dev. Study**\n"
        "```"
        "1. !dado <lados>\n"
        "   Rola um dado com a quantidade de lados que você escolher.\n"
        "   Exemplo: !dado 6\n\n"
        "2. !adivinhe <número>\n"
        "   O bot pensa em um número entre 1 e 10, e você precisa adivinhar.\n"
        "   Exemplo: !adivinhe 5\n\n"
        "3. !serverinfo\n"
        "   Exibe o nome do servidor e o número de membros.\n\n"
        "4. !soma <número1> <número2>\n"
        "   Soma dois números que você escolher.\n"
        "   Exemplo: !soma 5 10\n\n"
        "5. !hello\n"
        "   O bot se apresenta brevemente.\n\n"
        "6. !servidor\n"
        "   Disponibiliza o link de convite para o servidor.\n\n"
        "7. !pesquisa <tópico>\n"
        "   Realiza uma busca na Wikipedia sobre o tópico desejado.\n"
        "   Exemplo: !pesquisa Python\n"
        "```"
    )
    await ctx.send(message)

bot.run('token')
