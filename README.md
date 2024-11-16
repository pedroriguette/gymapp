# GYM-APP: Sistema de gerenciamente de Academia

Bem-vindo ao **GYM-APP**, um sistema desenvolvido para digitalizar o gerenciamento de 
academias, eliminando a necessidade de papel e permitindo que alunos visualizem fichas 
de exercícios de forma prática e que os professores administrem esses alunos, diretamente no smartphone
ou notebook.

## Funcionalidades

O projeto conta com funcionalidades como:

- **Gerenciamento de Usuários**: Cadastre e gerencie usuários de sistema, com a possibilidade de definir
diferentes papéis (Aluno ou Professor).
- **Gerenciamento Alunos e professores**: Registre Alunos e professores com todas informações necessárias
para acompanhamento e gestão. 
- **Exercícios personalizados**: Visualização de fichas de exercícios para alunos e Gerenciamento de 
Fichas pelos professores.
- **Sistema de permissão**: Controle o acesso ao sistema atribuindo permissões específicas para alunos e 
professores.
- **Autenticação**: Sistema de login e logout.
- **API integrada e Sistema de Autenticação por JWT**: Integração pronta para aplicação móveis, incluindo 
autenticação robusta com JSON Web Token (JWT).

## Pré-Requisitos

Para executar o projeto, você precisará:
- **Python** (recomendado: versão 3.7 ou superior)
- **Django** (instalado automaticamente)
- **Dependências Obrigatórias** (listadas em `requirements.txt`)

## Instalação das Dependências

1. Crie e ative o ambiente virtual:

    ```bash
    python -m venv venv
    source env/bin/activate  # Para Linux/Mac
    .\env\Scripts\activate   # Para Windows
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Rodar o projeto

1. Após instalar as dependências, aplique as migrations no banco de dados com o comando:
```bash
python manage.py migrate
```

2. Agora o projeto jã pode ser inicializado com o comando:
```bash
python manage.py runserver
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000](http://localhost:8000)
