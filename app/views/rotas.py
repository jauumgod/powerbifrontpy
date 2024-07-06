from app import *


@app.route('/')
def loginPage():
    return render_template('auth/login.html')


@app.route('/novoUserPage')
def novoUserPage():
    return render_template('auth/novoUsuarioDisable.html')


@app.route('/configuracao')
def configuracao():
    usuarios = 'Usuarios.query.all()'
    return render_template('config/configuracao.html')


@app.route('/profile')
def profile():
    return render_template('config/profile.html')


@app.route('/homepage')
def homepage():
    return render_template('routes/homepage.html')


@app.route('/visaoPedidos')
def visaoPedidos():
    return render_template('routes/visaoPedidos.html')


@app.route('/visaoAPagar')
def visaoAPagar():
    return render_template('routes/visaoAPagar.html')


@app.route('/visaoAReceber')
def visaoAReceber():
    return render_template('routes/visaoAReceber.html')


@app.route('/visaoClientes')
def visaoClientes():
    return render_template('routes/visaoClientes.html')


@app.route('/visaoEmpresas')
def visaoEmpresas():
    return render_template('routes/visaoEmpresas.html')


@app.route('/visaoVendas')
def visaoVendas():
    return render_template('routes/visaoVendas.html')


@app.route('/visaoCarregamentos')
def visaoCarregamentos():
    return render_template('routes/visaoCarregamentos.html')


@app.route('/visaoProducao')
def visaoProducao():
    return render_template('routes/visaoProducao.html')