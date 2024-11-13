# Busca de editais FINEP
## Integrantes
Ahmad Kheder Mahfoud - 20.01323-0

Caio Bartolozzi Bastos Godoy de Toledo - 20.01430-9

Davi Fernandes Simões Soares - 20.01099-0

Leonardo Campos - 20.00786-8

Lucas Romanato de Oliveira - 20.00313-7
## Sobre o projeto
O objetivo principal do projeto é auxiliar a busca de editais do site da FINEP por meio da digitação de algum projeto.

Inicialmente foi feito um web scraping no site da FINEP buscando todos os editais existentes desde 2015, em seguida realizamos o embeding - transformar texto em número - de todos os PDFs obtidos com o modelo pré-treinado `gemma-2-2b`.
Em seguida criamos um FAISS (Facebook AI Similarity Search), um banco de dados vetorial com os embedings feitos, para realizar uma busca de similaridade entre um texto e os documentos e colocamos em uma API.
A API tem o objetivo de pegar o texto digitado pelo usuário (na parte de front-end) e retornar uma lista de editais similares a ele, sendo dos mais similares para os menos similares.

## Documentação
- [backend](https://github.com/LucasRomanato0/IMT_CD_ECM514_2_SEM/tree/main/backend):

    Diretório aonde foi criada a API com o framework FLASK e o framework da Google Functions Framework para aplicar serveless call functions.

- [banco_de_dados](https://github.com/LucasRomanato0/IMT_CD_ECM514_2_SEM/tree/main/banco_de_dados):

    Diretório aonde foi realizado o web scraping, a extração dos dados dos PDFs, os embedings e a criação do banco de dados vetorial.

- [frontend](https://github.com/LucasRomanato0/IMT_CD_ECM514_2_SEM/tree/main/frontend):

    Diretório aonde foi criado um SPA (Single Page Application) com o framework ReactJS para consumir o backend enviando dados do projeto.

### Como executar

<strong>Pré-requisito:</strong> possuir Node.js, Python e Docker instalado na máquina.

#### Back-end:
Antes de iniciar o projeto, é necessário baixar as bibliotecas python com o comando `pip install -r requirements.txt`. Só é necessário instalar na primeira vez que for executar.

Para iniciar, basta rodar o comando `functions-framework --target=rag_api` no terminal direcionado para a pasta [backend](https://github.com/LucasRomanato0/IMT_CD_ECM514_2_SEM/tree/main/backend).
#### Front-end:
Para iniciar a parte front-end, basta rodar o comando `npm start` no terminal direcionado para a pasta [frontend](https://github.com/LucasRomanato0/IMT_CD_ECM514_2_SEM/tree/main/frontend).
