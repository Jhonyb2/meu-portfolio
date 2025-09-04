from flask import Flask, render_template, request
import os

# Define o caminho base para a pasta api
# Isso garante que o Flask encontre as pastas templates e static
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'static')

# Cria a instância do aplicativo Flask com os caminhos corretos
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# ... o restante do seu código ...

# Página inicial
@app.route('/')
def home():
    return render_template('index.html', projetos=meus_projetos)

