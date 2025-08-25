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
    return render_template('index.html')

# Página de projetos
@app.route('/projetos')
def projetos():
    return render_template('projetos.html', projetos=meus_projetos)

# Página sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Página de contato (GET para exibir, POST para processar formulário)
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    # As rotas para o email e whatsapp não precisam de processamento de formulário.
    # Apenas a página de contato com formulário precisaria dessa lógica.
    return render_template('contato.html')

# Executa o servidor de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)