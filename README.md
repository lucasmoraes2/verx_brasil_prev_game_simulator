# Teste Dev Brasil Prev (Verx)

Teste Dev Brasil Prev (Verx)

## Linguagens Utilizadas:
<ul>
    <li><a href="https://www.python.org/" target="_blank" rel="noopener noreferer">Python</a></li>
</ul>

## Dependências
<ul>
    <li><a href="https://www.python.org/downloads/release/python-312/" target="_blank" rel="noopener noreferer">Python - 3.12+</a></li>
    <li><a href="https://libraries.io/pypi/pip" target="_blank" rel="noopener noreferer">Pip - 23.2.1</a></li>
</ul>

## Tecnologias e Bibliotecas Utilizadas:
<ul>
<li><a href="https://fastapi.tiangolo.com/" target="_blank" rel="noopener noreferer">FastAPI - 0.115.3</a></li>
<li><a href="https://pypi.org/project/pytest/" target="_blank" rel="noopener noreferer">Pytest - 8.3.3</a></li>
<li><a href="https://pypi.org/project/SQLAlchemy/" target="_blank" rel="noopener noreferer">SQLAlchemy - 2.0.36</a></li>
<li><a href="https://pypi.org/project/uvicorn/" target="_blank" rel="noopener noreferer">Uvicorn - 0.32.0</a></li>
<li><a href="https://www.docker.com/products/docker-desktop/" target="_blank" rel="noopener noreferer">Docker</a></li>
<li><a href="https://hub.docker.com/_/postgres" target="_blank" rel="noopener noreferer">Postgres 13 (Imagem do Docker)</a></li>
</ul>


## Configurando Ambiente de Desenvolvimento

<p>1- Clone o repositório atual especificando a branch criada</p>

```bash
git clone --branch <branchname> "https://github.com/lucasmoraes2/verx_brasil_prev_game_simulator"
```

<p>2 - Abra o diretório do projeto em um editor de sua escolha</p>

<p>3 - Dentro da raiz do projeto, realize a instalação do banco de dados com o Docker Compose</p>

```bash
docker-compose up -d
```

<p>4 - Dentro da raiz do projeto, crie um virtual environment:</p>

```bash
python3 -m venv <nome_de_pasta_para_o_venv>
```

<p>5 - Ative o virtual environment: </p>

```bash
cd ./nome_de_pasta_para_o_venv

./Scripts/activate.bat  # windows
source ./bin/activate # linux
```

<p>6 - Realize a instalação das dependências do projeto</p>

```bash
    pip install -r requirements.txt -v
```

<p>7 - Para rodar a aplicação, na raiz do projeto execute:</p>

```bash
uvicorn app.main:app
```

<p>8 - Para rodar os testes unitários, na raiz do projeto execute:</p>

```bash
pytest
```
