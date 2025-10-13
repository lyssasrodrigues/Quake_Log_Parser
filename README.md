# QUAKE LOG PARSER

## Descrição

O parser lê o arquivo `games.log` do **Quake III Arena**, agrupa os dados de cada partida e contabiliza:
- O número total de mortes (`total_kills`);
- A lista de jogadores participantes (`players`);
- As mortes por jogador (`kills`), desconsiderando `<world>` e aplicando penalidades de -1 quando aplicável.

Também é gerado um **ranking geral** de kills entre todos os jogos e uma **API Flask** para consultar os resultados.

---

## Funcionalidades
- Leitura automática do arquivo `games.log`;  
- Agrupamento de dados por jogo (`game_1`, `game_2`, ...);  
- Cálculo de estatísticas de cada partida;  
- Geração de ranking geral de jogadores;  
- API REST para consultar resultados por ID de jogo.

---

## ⚙️ Como rodar o parser
```bash
# Instalar dependências
pip install flask

# Executar o parser + ranking no terminal
python main.py

Saída esperada:
game_1:
{'total_kills': 4, 'players': ['Dono da Bola', 'Isgalamido'], 'kills': {'Isgalamido': 1, 'Dono da Bola': 0}}

game_2:
{'total_kills': 3, 'players': ['Dono da Bola', 'Isgalamido'], 'kills': {'Isgalamido': 1, 'Dono da Bola': 1}}

RANKING GERAL 
Isgalamido: 2 kills
Dono da Bola: 1 kills

Como rodar a API
python api.py

A API será iniciada em:
http://127.0.0.1:5000

Endpoints
Método	Rota	Descrição
GET	/games/<game_id>	Retorna os dados de um jogo específico (game_1, game_2, etc.)

Exemplo:

nginx

GET http://127.0.0.1:5000/games/game_1

Resposta:

json
{
  "total_kills": 4,
  "players": ["Dono da Bola", "Isgalamido"],
  "kills": {"Isgalamido": 1, "Dono da Bola": 0}
}

 Estrutura do projeto
.
├── data/
│   └── games.log
├── parser/
│   └── log_parser.py
├── main.py
├── api.py
└── README.md

Tecnologias usadas:

Python 3;
Flask (para API);
Programação Orientada a Objetos (POO);

