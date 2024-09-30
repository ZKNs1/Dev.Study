# Dev. Study Bot

Dev. Study Bot é um bot interativo para Discord, criado para fornecer comandos úteis, divertidos e educacionais aos membros de um servidor. Ele oferece funcionalidades como jogos de adivinhação, rolar dados, realizar cálculos rápidos, exibir informações sobre o servidor e até realizar pesquisas na Wikipedia!

## Funcionalidades

O Dev. Study Bot possui uma variedade de comandos interativos que visam melhorar a experiência dos usuários no servidor. Veja abaixo os comandos disponíveis:

### Comandos Disponíveis

- **`!dado <lados>`**  
   Rola um dado com a quantidade de lados que você escolher.  
   Exemplo: `!dado 6` para um dado de 6 lados.

- **`!adivinhe <número>`**  
   O bot pensa em um número entre 1 e 10, e você deve adivinhar.  
   Exemplo: `!adivinhe 5`.

- **`!serverinfo`**  
   Retorna o nome do servidor e o número total de membros.

- **`!soma <número1> <número2>`**  
   Soma dois números fornecidos.  
   Exemplo: `!soma 6 10`.

- **`!hello`**  
   O bot faz uma pequena apresentação sobre si mesmo e menciona seu criador.

- **`!servidor`**  
   Disponibiliza o link de convite para o servidor.

- **`!pesquisa <tópico>`**  
   Faz uma pesquisa rápida na Wikipedia sobre o tópico informado.  
   Exemplo: `!pesquisa Python`.

- **`!react`**  
   Adiciona uma reação de 👍 à mensagem.

- **`!enquete <pergunta>`**  
   Cria uma enquete com reações de 👍, 👎 e 🤷.

- **`!moeda`**  
   Joga uma moeda virtual, retornando "Cara" ou "Coroa".

- **`!escolher <opção1> <opção2> ...`**  
   Escolhe aleatoriamente uma das opções fornecidas.

- **`!avatar [membro]`**  
   Mostra o avatar do membro especificado ou do próprio autor do comando.

- **`!limpar <quantidade>`**  
   Apaga um número específico de mensagens no canal atual (necessita de permissão).

- **`!comandos`**  
   Exibe a lista completa de comandos disponíveis.

## Pré-requisitos

Para rodar o bot localmente, você precisará ter as seguintes dependências instaladas:

- Python 3.8 ou superior
- Biblioteca `discord.py`
- Biblioteca `aiohttp`

Você pode instalar as dependências executando o seguinte comando:

```bash
pip install discord.py aiohttp
