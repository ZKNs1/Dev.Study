import discord
import random
import aiohttp
import math
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

# Comando de cálculo
@bot.command(name='soma')
async def sum(ctx, a: float, b: float):
    result = a + b
    await ctx.send(f'O resultado de {a} + {b} é {result}.')

@bot.command(name='sub')
async def sub(ctx, a: float, b: float):
    result = a - b
    await ctx.send(f'O resultado de {a} - {b} é {result}.')

@bot.command(name='mult')
async def mult(ctx, a: float, b: float):
    result = a * b
    await ctx.send(f'O resultado de {a} * {b} é {result}.')

@bot.command(name='div')
async def div(ctx, a: float, b: float):
    result = a / b
    await ctx.send(f'O resultado de {a} / {b} é {result}.')

@bot.command(name='bhaskara')
async def bhaskara(ctx, a: int, b: int, c: int):
    delta = math.pow(b, 2) - (4*a*c)
    result1 = (-b - math.sqrt(delta)) / (2*a)
    result2 = (-b + math.sqrt(delta)) / (2*a)
    if delta>0:
        await ctx.send(f'O resultado de **b+** é {round(result2, 2)} e o de **b-** é {round(result1, 2)}');
    if delta==0:
        await ctx.send(f'O Delta é igual a 0, portanto não há raiz');
    if delta<0:
        await ctx.send(f'O Delta é negativo, portanto não há raiz');

# Comando de informações do servidor
@bot.command(name='serverinfo')
async def serverinfo(ctx):
    guild = ctx.guild
    num_members = guild.member_count
    server_name = guild.name
    await ctx.send(f'O servidor {server_name} tem {num_members} membros.')

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
                page_url = data.get('content_urls', {}).get('desktop', {}).get('page', '')

                embed = discord.Embed(
                    title=f"📖 {title}",
                    description=extract,
                    color=discord.Color.light_embed()
                )

                if page_url:
                    embed.add_field(name="🔗 Leia mais", value=f"[Clique aqui para ler mais]({page_url})", inline=False)

                if 'thumbnail' in data:
                    embed.set_thumbnail(url=data['thumbnail']['source'])
                
                await ctx.send(embed=embed)
                embed.set_footer(text="Bot Dev. Study | Criado por _ytrnhx")
            else:
                await ctx.send("❌ Não encontrei informações sobre isso.")

# Comando que retorna o link para o servidor
@bot.command(name='servidor')
async def hello(ctx):
    await ctx.send(f'Este é o link de convite para nosso servidor https://discord.gg/HvBbJvVbQ5')

# Comando que retorna link para o github
@bot.command(name='bot')
async def bot(ctx):
    await ctx.send(f'Este é o link para o código do bot https://github.com/ZKNs1/Dev.Study, neste repositório você terá acesso a todas as atualizações e ao código')

@bot.command(name='comandos')
async def comandos(ctx):
    embed = discord.Embed(
        title="📜 Comandos Disponíveis do Bot Dev. Study",
        description="Aqui está a lista de comandos que você pode usar.",
        color=discord.Color.light_embed()
    )

    embed.add_field(
        name="🎲 !dado `<lados>`",
        value="Rola um dado com a quantidade de lados que você escolher.\n**Exemplo**: `!dado 6`",
        inline=False
    )
    embed.add_field(
        name="🔢 !adivinhe `<número>`",
        value="O bot pensa em um número entre 1 e 10, e você deve adivinhar.\n**Exemplo**: `!adivinhe 5`",
        inline=False
    )
    embed.add_field(
        name="🪙 !moeda",
        value="Joga uma moeda e retorna o resultado: **Cara** ou **Coroa**.",
        inline=False
    )
    embed.add_field(
        name="🎯 !escolher `<opção1>` `<opção2>` ...",
        value="Escolhe uma entre várias opções fornecidas.\n**Exemplo**: `!escolher Pizza Burger Sushi`",
        inline=False
    )
    embed.add_field(
        name="📊 !enquete `<pergunta>`",
        value="Cria uma enquete com reações de 👍, 👎 e 🤷.\n**Exemplo**: `!enquete Qual seu editor de texto favorito?`",
        inline=False
    )
    embed.add_field(
        name="🎨 !avatar `[membro]`",
        value="Mostra o avatar de um membro. Se não for mencionado, mostra o seu próprio avatar.\n**Exemplo**: `!avatar @Melina`",
        inline=False
    )
    embed.add_field(
        name="➕ !soma `<número1>` `<número2>`",
        value="Soma dois números que você escolher.\n**Exemplo**: `!soma 5 10`",
        inline=False
    )
    embed.add_field(
        name="➖ !sub `<número1>` `<número2>`",
        value="Subtrai dois números que você escolher.\n**Exemplo**: `!sub 10 5`",
        inline=False
    )
    embed.add_field(
        name="✖️ !mult `<número1>` `<número2>`",
        value="Multiplica dois números que você escolher.\n**Exemplo**: `!mult 5 3`",
        inline=False
    )
    embed.add_field(
        name="➗ !div `<número1>` `<número2>`",
        value="Divide dois números que você escolher.\n**Exemplo**: `!div 10 2`",
        inline=False
    )
    embed.add_field(
        name="📐 !bhaskara `<a>` `<b>` `<c>`",
        value="Resolve a equação de segundo grau usando a fórmula de Bhaskara.\n**Exemplo**: `!bhaskara 1 -5 6`",
        inline=False
    )
    embed.add_field(
        name="🔍 !pesquisa `<tópico>`",
        value="Faz uma busca na Wikipedia sobre o tópico desejado.\n**Exemplo**: `!pesquisa Python`",
        inline=False
    )
    embed.add_field(
        name="🧹 !limpar `<quantidade>`",
        value="Apaga uma quantidade específica de mensagens no canal.\n**Exemplo**: `!limpar 10`",
        inline=False
    )
    embed.add_field(
        name="👋 !hello",
        value="O bot faz uma pequena apresentação sobre si mesmo.",
        inline=False
    )
    embed.add_field(
        name="📊 !serverinfo",
        value="Exibe o nome do servidor e o número de membros.",
        inline=False
    )
    embed.add_field(
        name="🔗 !servidor",
        value="Fornece o link de convite para o servidor DevStudy.",
        inline=False
    )
    embed.add_field(
        name="🤖 !bot",
        value="Fornece o link para o repositório do bot Dev. Study no GitHub.",
        inline=False
    )
    embed.set_footer(text="Bot Dev. Study | Criado por _ytrnhx")

    await ctx.send(embed=embed)

bot.run('token')
