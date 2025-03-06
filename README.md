<div align="center">

# 📊 Gestão de Projetos 

</div>

<p align="center">
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/IasminBorba/Gestao-de-Projetos" />
  <a href="https://github.com/IasminBorba" target="_blank"><img alt="Follow Me" src="https://img.shields.io/github/followers/IasminBorba.svg?style=social&label=Follow&maxAge=2592000" /></a>
</p>

---

## 🚀 Tecnologias
- Python 3.11.9
- Django
- Django Rest Framework
- PostgreSql

## 🛠 Como rodar o projeto?

Antes de mais nada, para executar o projeto, é necessário que você clone o repositório:
```sh
git clone https://github.com/IasminBorba/Gestao-de-Projetos.git
```

Após isso, crie seu ambiente virtual:

```sh
python -m venv env
```

Com o env definido, você precisa instalar as dependências:

```sh
source env/bin/activate
pip install -r requirements.txt
```
Depois, configure o banco de dados e crie o superusuário (necessário, para acessar o admin):

```sh
python manage.py migrate
python manage.py createsuperuser
```

Por fim, basta rodar o servidor local com o comando:

```sh
python manage.py runserver
```

## 📂 Estrutura do Repositório
- `src/` → Código-fonte do sistema
- `test/` → Testes unitários
- `docs/` → Documentação extra
- `README.md` → Explicação do projeto
- `.gitignore` → Arquivos ignorados no Git


## 📑 **Documentação da API**

A API permite gerenciar projetos, colaboradores, áreas tecnológicas e financiadores.

### 🔑 **Admin**  
| Método | Endpoint   | Descrição |
|--------|------------|-----------|
| `GET`  | `/admin/`  | Acesso ao painel administrativo do Django. |

### 🚀 **Endpoints de Projetos**  
| Método  | Endpoint                                    | Descrição |
|---------|---------------------------------------------|-----------|
| `GET`   | `/projetos/form/`                           | Retorna o formulário para cadastro de projetos. |
| `GET`   | `/projetos/listar/`                         | Lista todos os projetos cadastrados. |
| `POST`  | `/projetos/cadastrar/`                      | Cadastra um novo projeto. |
| `POST`  | `/projetos/{id_projeto}/inativar/`          | Inativa um projeto específico. |
| `PATCH` | `/projetos/{id_projeto}/editar/`            | Edita as informações de um projeto. |
| `GET`   | `/projetos/{id_projeto}/visualizar/`        | Retorna detalhes de um projeto específico. |
| `GET`   | `/projetos/{id_projeto}/equipe/`            | Lista a equipe de um projeto. |
| `PATCH` | `/projetos/{id_projeto}/equipe/atualizar/`  | Atualiza a equipe de um projeto. |

### 👥 **Endpoints de Colaboradores**  
| Método  | Endpoint                                   | Descrição |
|---------|--------------------------------------------|-----------|
| `GET`   | `/colaboradores/listar/`                   | Lista todos os colaboradores cadastrados. |
| `POST`  | `/colaboradores/cadastrar/`                | Cadastra um novo colaborador. |
| `GET`   | `/colaboradores/{id_colaborador}/visualizar/`         | Retorna detalhes de um colaborador específico. |
| `PATCH` | `/colaboradores/{id_colaborador}/editar/`             | Edita as informações de um colaborador. |

### 📚 **Endpoints de Áreas Tecnológicas**  
| Método  | Endpoint                                   | Descrição |
|---------|--------------------------------------------|-----------|
| `GET`   | `/areas_tecnologicas/listar/`              | Lista todas as áreas tecnológicas cadastradas. |

### 💰 **Endpoints de Financiadores**  
| Método  | Endpoint                                   | Descrição |
|---------|--------------------------------------------|-----------|
| `GET`   | `/financiadores/listar/`                   | Lista todos os financiadores cadastrados. |