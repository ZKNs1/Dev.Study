# Dev. Study Bot

Dev. Study Bot é um bot interativo para Discord, o seu objetivo é fornecer comandos úteis e divertidos para membros de um servidor. Ele oferece funcionalidades como rolar dados, jogar jogos de adivinhação, exibir informações sobre o servidor e realizar pesquisas rápidas na Wikipedia.

## Funcionalidades

O Dev. Study Bot conta com vários comandos interativos para melhorar a experiência do usuário no servidor. Aqui estão alguns dos principais comandos:

### Comandos Disponíveis

- **!dado `<lados>`**  
   Rola um dado com a quantidade de lados que você escolher.  
   Exemplo: `!dado 6` para um dado de 6 lados.

- **!adivinhe `<número>`**  
   O bot pensa em um número entre 1 e 10, e você deve adivinhar.  
   Exemplo: `!adivinhe 5`.

- **!serverinfo**  
   Retorna o nome do servidor e o número total de membros.

- **!soma `<número1>` `<número2>`**  
   Soma dois números fornecidos.  
   Exemplo: `!soma 6 10`.

- **!hello**  
   O bot faz uma pequena apresentação sobre si mesmo e menciona seu criador.

- **!servidor**  
   Disponibiliza o link de convite para o servidor.

- **!pesquisa `<tópico>`**  
   Faz uma pesquisa rápida na Wikipedia sobre o tópico informado.  
   Exemplo: `!pesquisa Python`.

- **!comandos**  
   Exibe a lista completa de comandos disponíveis.

## Pré-requisitos

Para rodar o bot localmente, você precisará ter as seguintes dependências instaladas:

- Python 3.8 ou superior
- Biblioteca `discord.py`
- Biblioteca `aiohttp`

Você pode instalar as dependências executando o seguinte comando:

```bash
pip install discord.py aiohttp
