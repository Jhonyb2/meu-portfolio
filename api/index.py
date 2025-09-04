from flask import Flask, render_template, request

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Armazene seus projetos em uma lista de dicionários
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

# Página inicial
@app.route('/')
def home():
    # Passa a lista de projetos para o template principal
    return render_template('index.html', projetos=meus_projetos)

