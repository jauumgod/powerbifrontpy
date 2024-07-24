from app import *
from app.models.usuarios import User
from ..controller import autenticacao

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        result = autenticacao.loginUser(username=username,password=password)
        if result == True:
            redirect(url_for('homepage'))
        else:
            return redirect(url_for('loginPage'))
    
    return render_template('auth/login.html')

@app.route('/novoUserPage', methods=['GET','POST'])
def novoUserPage():
    username = request.form.get('username')
    password = request.form.get('password')
    result = autenticacao.cadastroUser(username=username, password=password)
    return render_template('auth/novoUsuarioDisable.html')


@app.route("/alterarNome/<int:id>", methods=['GET','POST'])
def alterarNome(id):
    autenticacao.alterarNome(id=id)
    

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