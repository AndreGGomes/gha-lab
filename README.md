# gha-lab

Projeto-base do laboratório de GitHub Actions (Aula 2): um pacote Python mínimo
(`calc`) com seis testes. Você **não precisa instalar Python** — todas as
ferramentas rodam em um contêiner Docker.

## 1. Construir a imagem (uma vez)

Na pasta do projeto (onde está o `Dockerfile`):

```bash
docker build -t gha-lab-dev .
docker run --rm gha-lab-dev python --version   # deve mostrar Python 3.12.x
```

Reconstrua só quando mudar o `Dockerfile` ou o `requirements-dev.txt`.

## 2. Abrir o shell interativo

| Terminal | Comando |
|---|---|
| Linux, macOS, Git Bash | `docker run --rm -it -v "$(pwd)":/app gha-lab-dev` |
| Windows PowerShell | `docker run --rm -it -v "${PWD}:/app" gha-lab-dev` |
| Windows cmd | `docker run --rm -it -v "%cd%":/app gha-lab-dev` |
| Qualquer um (Compose) | `docker compose run --rm dev` |

No Linux, para que os arquivos gerados não fiquem com dono `root`:

```bash
docker run --rm -it -v "$(pwd)":/app --user "$(id -u):$(id -g)" -e HOME=/tmp gha-lab-dev
```

A pasta do projeto aparece em `/app` dentro do contêiner: edite no seu editor,
rode no contêiner.

## 3. Comandos no shell do contêiner

```bash
pytest -v                                    # testes
pytest -v -k divide                          # só os testes com "divide" no nome
pytest --cov=calc --cov-report=term-missing --cov-fail-under=90   # cobertura
ruff check .                                 # lint
ruff check --fix .                           # corrige o que for possível
ruff format .                                # formata
ruff format --check .                        # só verifica a formatação
python -m build                              # gera dist/ (.whl e .tar.gz)
actionlint                                   # valida .github/workflows
python                                       # REPL: from calc import soma
exit                                         # sai (ou Ctrl+D)
```

Comando avulso, sem entrar no shell:

```bash
docker run --rm -v "$(pwd)":/app gha-lab-dev pytest -v
```

`git commit` e `git push` são feitos **no seu computador**, onde estão as
credenciais do GitHub.
