from flask import Flask, render_template, request
import os

# Define o caminho para as pastas templates e static
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# Cria a instância do aplicativo Flask
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# --- Garanta que esta parte esteja aqui, no topo do arquivo ---
meus_projetos = [
    {
        'titulo': 'Biblioteca em C', 
        'descricao': 'Um sistema de gerenciamento de biblioteca utilizando alocação dinâmica de memória.', 
        'linguagem': 'C',
        'imagem': 'lib-c.jpg',
        'link_projeto': 'https://github.com/Jhonyb2/Biblioteca-protejo-ads-em-C'
    },
    {
        'titulo': 'Jogo de Cartas em C', 
        'descricao': 'A base de um jogo de cartas (como Super Trunfo ou War) para um trabalho universitário.', 
        'linguagem': 'C',
        'imagem': 'game-c.jpg',
        'link_projeto': 'https://github.com/Cursos-TI/desafio-l-gica-super-trunfo-Jhonyb2'
    },
    {
        'titulo': 'Portfólio com Flask', 
        'descricao': 'Este site, criado para demonstrar habilidades em Flask.', 
        'linguagem': 'Python',
        'imagem': 'portiflas.jpg',
        'link_projeto': 'https://github.com/seu-usuario/meu-portfolio'
    }
]
# -----------------------------------------------------------------

# Página inicial
@app.route('/')
def home():
    # Agora a variável 'meus_projetos' está definida e acessível
    return render_template('index.html', projetos=meus_projetos)