# Organizador de Anotações com Gemini

Este é um projeto simples de aplicação web construído com Flask e a API do Gemini (via biblioteca `google-generativeai`). Ele permite que você insira anotações bagunçadas e as formate de maneira organizada usando o poder da inteligência artificial do Gemini. A interface é minimalista, inspirada no visual do próprio Gemini, com um tema escuro e cores azuis.

## Funcionalidades

* **Formatação de Anotações:** Insira qualquer tipo de anotação desorganizada e a IA do Gemini as processará, estruturando-as com títulos, subtítulos e listas em Markdown para melhor legibilidade.
* **Interface Minimalista:** Design limpo e focado no conteúdo, com um tema escuro e paleta de cores azuis, proporcionando uma experiência de uso agradável e sem distrações.

## Como Rodar o Projeto Localmente

Siga estes passos para executar o projeto no seu ambiente de desenvolvimento:

### Pré-requisitos

* **Python 3.7+:** Certifique-se de ter o Python instalado no seu sistema. Você pode verificar sua versão com o comando:

    ````bash
    python --version
    ````
* **pip:** O gerenciador de pacotes do Python, que geralmente vem instalado com o Python.
* **Conta no Google AI Studio e uma Chave de API:** Você precisará criar uma chave de API no [Google AI Studio](https://makersuite.google.com/app/apikey) para autenticar as requisições à API do Gemini.

### Passos para Execução

1.  **Clone o Repositório (se ainda não o fez):**

    ````bash
    git clone [https://github.com/isaacnewton-tech/organizador-de-anotacoes.git](https://github.com/isaacnewton-tech/organizador-de-anotacoes.git)
    cd organizador-de-anotacoes
    ````
2.  **Crie e Ative um Ambiente Virtual:**

    É recomendado criar um ambiente virtual para isolar as dependências do projeto.

    ````bash
    python -m venv .venv
    source .venv/bin/activate  # No Linux/macOS
    .venv\Scripts\activate  # No Windows
    ````
3.  **Instale as Dependências:**

    Use o arquivo `requirements.txt` para instalar as bibliotecas necessárias.

    ````bash
    pip install -r requirements.txt
    ````
4.  **Configure a Chave de API:**

    Crie um arquivo chamado `.env` na raiz do seu projeto e adicione sua chave de API do Google AI Studio:

    ````
    GOOGLE_API_KEY="SUA_CHAVE_DE_API"
    ````

    Substitua `"SUA_CHAVE_DE_API"` pela sua chave real. **Mantenha este arquivo privado e não o compartilhe.**
5.  **Execute a Aplicação Flask:**

    Na raiz do seu projeto, execute o seguinte comando para iniciar o servidor de desenvolvimento do Flask:

    ````bash
    python app.py
    ````
6.  **Acesse a Aplicação no seu Navegador:**

    Abra seu navegador web e vá para `http://127.0.0.1:5000/`. Você deverá ver a interface do Organizador de Anotações.

### Como Usar

1.  Na página inicial, você verá uma caixa de texto rotulada "1. Insira suas anotações bagunçadas:".
2.  Cole ou digite suas anotações desorganizadas nessa caixa de texto.
3.  Clique no botão "Formatar Anotações".
4.  Abaixo, na seção "2. Anotações Formatadas:", a IA do Gemini processará suas anotações e exibirá uma versão organizada e formatada em Markdown.

## Estrutura do Projeto
organizador-de-anotacoes/
├── .venv/             # Ambiente virtual Python (ignorado pelo Git)
├── .env                # Arquivo de variáveis de ambiente (contém a chave da API - ignorado pelo Git)
├── app.py              # O código principal da aplicação Flask
├── templates/
│   └── index.html    # O template HTML da página web
├── requirements.txt    # Lista das dependências Python
└── README.md           # Este arquivo
