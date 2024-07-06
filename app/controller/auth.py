from app import *
from app.models.usuarios import User


def loginUser():
    login_user()
    return redirect(url_for('homepage'))


def cadastroUser(username, password):
    cadastro = User(
        username = username,
        password = password
    )
    db.session.add(cadastro)
    db.session.commit()
    return redirect(url_for('loginUser'))


def update_status_bd(id):
    query = User.query.filter_by(id=id).first()
    if query:
        query.resolvido = 'S'
        db.session.commit()

    else:
        print(f"Registro com ID {id} não encontrado")
        flash(f"Registro com ID {id} não encontrado")


@app.route("/alterarNome/<int:id>", methods=['GET','POST'])
def alterarNome(id):
    if request.method == 'POST':
        update_status_bd(id)
        flash('Atualizado com sucesso!')
    return redirect(url_for('alterar_pedido'))