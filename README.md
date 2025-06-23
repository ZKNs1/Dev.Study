# Dev. Study Bot ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Discord](https://img.shields.io/badge/Discord-Bot-7289DA)


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

- **`!sub <número1> <número2>`**  
  Subtrai dois números fornecidos.  
  Exemplo: `!sub 10 5`.

- **`!mult <número1> <número2>`**  
  Multiplica dois números fornecidos.  
  Exemplo: `!mult 5 3`.

- **`!div <número1> <número2>`**  
  Divide dois números fornecidos.  
  Exemplo: `!div 10 2`.

- **`!bhaskara <a> <b> <c>`**  
  Resolve uma equação do 2º grau usando a fórmula de Bhaskara. Se houver raízes reais, o bot também envia o gráfico da parábola.  
  Exemplo: `!bhaskara 1 -5 6`.

- **`!hello`**  
  O bot faz uma pequena apresentação sobre si mesmo e menciona seu criador.

- **`!servidor`**  
  Disponibiliza o link de convite para o servidor.

- **`!bot`**  
  Fornece o link para o repositório do código-fonte no GitHub.

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
  Exemplo: `!escolher Pizza Hambúrguer Sushi`.

- **`!avatar [membro]`**  
  Mostra o avatar do membro especificado ou, se não for mencionado, o seu próprio.

- **`!limpar <quantidade>`**  
  Apaga um número específico de mensagens no canal atual (necessita de permissão).

- **`!comandos`**  
  Exibe a lista completa de comandos disponíveis.


## Configuração

1. Crie um bot no [Discord Developer Portal](https://discord.com/developers/applications) e copie seu token.
2. Crie um arquivo chamado `.env` ou uma variável de ambiente chamada `DISCORD_TOKEN`.
3. No seu código Python, use:

```python
import os
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
```

### Como executar

**Pré-requisitos**

Para rodar o bot localmente, você precisará ter as seguintes dependências instaladas:

- Python 3.8 ou superior
- Biblioteca `discord.py`
- Biblioteca `aiohttp`
- Biblioteca `matplotlib`
- Biblioteca `numpy`

1. Clone o repositório:
```bash
git clone https://github.com/ZKNs1/Dev.Study.git
cd Dev.Study
```
2. Instale as dependências
```bash
pip install discord.py aiohttp matplotlib numpy
```
## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
