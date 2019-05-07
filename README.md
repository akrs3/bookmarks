# Bookmarks

# Ambiente de Desenvolvimento

1. Clone o repositório.git 
2. Crie um virtualenv com Python 3.6.8
3. Ative o virtualenv.
4. Instale as dependências
5. Configure a instância com o .myvenv
6. Aplique as migrações e execute o projeto

## Instalação
### Clone o repositório

```console
git clone https://github.com/akrs3/bookmarks.git
cd bookmarks
```

### Crie o virtualenv com Python 3.6.8

Unix
```console
python3 -m venv .myvenv
```
Windows
```console
C:\Python36\python -m venv .myvenv
```

### Ative o virtualenv

Unix
```console
source .myvenv/bin/activate
```
Windows
```console
.myvenv\Scripts\activate.bat
```

### Instale as dependências

```console
pip install -r requirements.txt
```

### Execute as migrações e os testes
```console
python manage.py migrate
python manage.py test
python manage.py runserver
```