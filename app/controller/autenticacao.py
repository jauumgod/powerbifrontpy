from app import *
from ..models.usuarios import User



def loginUser(username, password):
    user = User.query.filter_by(username=username)
    if not user or not check_password_hash(user.password, password):
        flash('Por favor, verifique seu login e tente novamente.')
        return False
    login_user(user, remember=True)
    return True


def cadastroUser(username, password):
    cadastro = User(
        username = username,
        password = generate_password_hash(password, method='sha256')
    )
    user = User.query.filter_by(username=username)
    if user:
        return redirect(url_for('loginPage'))
    db.session.add(cadastro)
    db.session.commit()
    return redirect(url_for('loginPage'))


def update_status_bd(id):
    query = User.query.filter_by(id=id).first()
    if query:
        query.resolvido = 'S'
        db.session.commit()

    else:
        print(f"Registro com ID {id} não encontrado")
        flash(f"Registro com ID {id} não encontrado")


def alterarNome(id):
    if request.method == 'POST':
        update_status_bd(id)
        flash('Atualizado com sucesso!')
    return redirect(url_for('alterar_pedido'))