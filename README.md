Caixa de Mercado 🛒

Sistema simples de caixa de mercado feito em Python para registrar compras, visualizar produtos e calcular totais.

📌 Sobre o projeto

O Caixa de Mercado é um projeto desenvolvido para praticar conceitos fundamentais de programação em Python, incluindo organização modular, manipulação de arquivos JSON, orientação a objetos e interface de terminal.

O sistema permite:

✅ Visualizar mercadorias cadastradas
✅ Adicionar produtos ao carrinho
✅ Calcular o total da compra
✅ Configuração personalizada por JSON
✅ Interface personalizada com banners e mensagens estilizadas

---

📂 Estrutura do projeto

Caixa_de_mercado/
│
├── config/
│   └── app.json
│
├── core/
│   ├── __init__.py
│   ├── adicionar.py
│   ├── apagar.py
│   └── carregar.py
│
├── dados/
│   ├── __init__.py
│   ├── SQL.json
│   └── mercadorias.json
│
├── src/
│   ├── __init__.py
│   ├── carrinho.py
│   └── visualizar.py
│
├── ui/
│   ├── banner.py
│   └── mensagens.py
│
├── README.md
└── start.py

---

⚙️ Tecnologias utilizadas

- Python 3
- JSON
- Colorama
- Tabulate

---

📥 Instalação

Clone o repositório:

git clone https://github.com/ErikAndGabriel/Caixa_de_mercado.git

Acesse a pasta:

cd Caixa_de_mercado

Instale as dependências:

bash install.sh

Execute o sistema:

python start.py

---

📁 Explicação das pastas

"config/"

Armazena configurações gerais do sistema.

Exemplos:

- Nome da aplicação
- Moeda utilizada
- Configurações visuais

---

"core/"

Funções auxiliares responsáveis por operações internas.

Exemplos:

- Carregamento de arquivos JSON
- Adição de registros
- Limpeza da tela
- Utilitários do sistema

---

"dados/"

Arquivos de armazenamento utilizados pela aplicação.

Exemplos:

- Lista de mercadorias
- Dados temporários do carrinho
- Banco de dados em JSON

---

"src/"

Contém a lógica principal da aplicação.

Exemplos:

- Gerenciamento do carrinho
- Visualização de produtos
- Processamento de compras

---

"ui/"

Responsável pelos elementos visuais do terminal.

Exemplos:

- Banners personalizados
- Mensagens de erro
- Mensagens de sucesso
- Formatação da interface

---

📸 Screenshots

🏠 Menu Principal

<p align="center">
  <img src="FOTOS/IMG_20260517_233023_165.jpg" width="700">
</p>Tela inicial do sistema.

---

⚙️ Informações do Sistema

<p align="center">
  <img src="FOTOS/IMG_20260517_233115_603.jpg" width="700">
</p>Visualização das configurações carregadas pelo sistema.

---

🛒 Teste de Compra

<p align="center">
  <img src="FOTOS/IMG_20260517_233121_024.jpg" width="700">
</p>Adição de produtos utilizando código e quantidade.

---

📦 Produtos Disponíveis

<p align="center">
  <img src="FOTOS/IMG_20260517_233127_445.jpg" width="700">
</p>Lista completa de mercadorias cadastradas.

---

👥 Comunidade

Participe do grupo oficial do projeto no Telegram:

🔗 [LINK DO GRUPO AQUI]

---

🎯 Objetivo do projeto

Este projeto foi criado com fins educacionais para aprimorar conhecimentos em:

- Python Modular
- Programação Orientada a Objetos (POO)
- Manipulação de Arquivos JSON
- Organização Profissional de Projetos
- Interfaces em Terminal

---

👨‍💻 Autor

Desenvolvido por Erik

GitHub: https://github.com/ErikAndGabriel

---

⭐ Se o projeto foi útil para você, considere deixar uma estrela no repositório.
