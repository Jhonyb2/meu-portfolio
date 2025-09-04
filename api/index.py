from flask import Flask, render_template, request
import os

app = Flask(__name__)

# A lista de projetos precisa estar aqui, no topo do arquivo
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

# AQUI ESTÁ A CORREÇÃO
@app.route('/')
def home():
    # Agora a variável 'projetos' está sendo enviada para o template
    return render_template('index.html', projetos=meus_projetos)