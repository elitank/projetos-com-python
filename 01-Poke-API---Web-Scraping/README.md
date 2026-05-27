# 🔴 Pokédex com PokeAPI — Web Scraping & APIs RESTful
 
> *"Aprendi mais com os erros do que com o código que funcionou."*
 
Projeto de estudo focado em **consumo de APIs RESTful** e nos limites éticos do **web scraping** — com um tema que eu amo: Pokémon. 🎮
 
---
 
## 💡 Como surgiu
 
Tudo começou com uma tentativa de fazer web scraping diretamente no site oficial da Pokédex.
 
O problema? O site possui **restrições explícitas contra acesso automatizado**, descritas nos seus Termos de Uso. Assim que identifiquei isso, interrompi a abordagem imediatamente — e foi aí que veio o aprendizado mais importante do projeto: **web scraping precisa ser feito com responsabilidade**.
 
A solução ética e viável foi a **[PokeAPI](https://pokeapi.co/)** — uma API RESTful pública, gratuita e criada especificamente para esse tipo de aplicação.
 
---
 
## 🎯 O que o projeto faz
 
Com a PokeAPI, construí um **DataFrame personalizado da Pokédex** explorando múltiplos endpoints para ir além dos dados básicos:
 
- 🔹 Tipos e habilidades
- 🔹 Espécies e habitat
- 🔹 Cadeias evolutivas completas
O resultado é uma base de dados estruturada, limpa e pronta para análise.
 
---
 
## ✔️ O que aprendi
 
- Entender e respeitar os **limites éticos e legais** do web scraping
- Consumir uma **API RESTful pública** de forma eficiente
- Trabalhar com **cache local** para evitar sobrecarga de requisições e melhorar performance
- Explorar **diferentes endpoints** de uma mesma API para enriquecer os dados
- Transformar dados brutos em um **DataFrame limpo e estruturado**
---
 
## 📦 Tecnologias utilizadas
 
| Biblioteca | Uso |
|------------|-----|
| `requests` | Requisições HTTP para a PokeAPI |
| `pandas` | Estruturação e manipulação dos dados |
| `tqdm` | Barra de progresso nas requisições |
| `time` | Controle de intervalo entre chamadas à API |
 
---
 
## 📂 Estrutura
 
```
01-Poke-API---Web-Scraping/
└── web_scraping/
    ├── main.py               # Script principal
    ├── pokemon_data.csv      # DataFrame gerado
    └── backup_pokemon.csv    # Backup dos dados
```
 
---
 
## 📫 Contato
 
- **LinkedIn:** [Ellen Tank](https://www.linkedin.com/in/ellen-tank/)
- **GitHub:** [elitank](https://github.com/elitank)
---
 
*Made with ❤️ 