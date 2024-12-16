



# Autor: Fernando Pereira Alves
# GitHub: @Fernandodev0102
# Contato: 85976014779


from flask import Flask, render_template, request, redirect, url_for
import bd  # Importa o arquivo bd.py para interação com o banco de dados

# Cria uma instância da aplicação Flask
app = Flask(__name__)
# Rota para a página inicial de cadastro de contatos
# A função 'cadastro' renderiza a página HTML 'Cadastro.html'
@app.route('/')
def cadastro():
    return render_template('Cadastro.html')
# Rota para adicionar um contato ao banco de dados
# O método POST é utilizado para enviar os dados do formulário
@app.route('/adicionar', methods=['POST'])
def adicionar():
    # Obtém os dados do formulário (nome, número e cidade)
    nome = request.form['nome']
    numero = request.form['numero']
    cidade = request.form['cidade']
    
    # Chama a função 'adicionar_contato' do arquivo bd.py para salvar o contato no banco de dados
    bd.adicionar_contato(nome, numero, cidade)
    
    # Redireciona o usuário para a rota 'listar', que exibe a lista de contatos
    return redirect(url_for('listar'))

# Rota para listar todos os contatos cadastrados
@app.route('/listar')
def listar():
    # Chama a função 'listar_contatos' do arquivo bd.py para obter todos os contatos
    contatos = bd.listar_contatos()
    
    # Renderiza a página HTML 'Lista.html' e envia a lista de contatos para o template
    return render_template('Lista.html', contatos=contatos)

# Rota para deletar um contato do banco de dados com base no número de telefone
# O número é passado como parâmetro na URL
@app.route('/deletar/<numero>')
def deletar(numero):
    # Chama a função 'deletar_contato' do arquivo bd.py para remover o contato pelo número
    bd.deletar_contato(numero)
    
    # Redireciona o usuário para a rota 'listar', atualizando a lista de contatos exibida
    return redirect(url_for('listar'))

# Verifica se o script está sendo executado diretamente (não importado como módulo)
# Inicia o servidor Flask em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)
