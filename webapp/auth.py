from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Usuarios, Pessoa
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        senha = request.form.get('senha')

        usuario = Usuarios.query.filter_by(cpf=cpf).first()
        if usuario:
            if check_password_hash(usuario.senha, senha):
                flash('Usuário autenticado com sucesso.', category='success')
                login_user(usuario, remember=True)
                return redirect(url_for('views.paciente'))
            else:
                flash('Senha incorreta! Por favor, tente novamente.', category='error')
        else:
            flash('CPF não encontrado.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/sair')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.inicio'))


@auth.route('/cadastrar-se', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        cns = request.form.get('cns')
        cpf = request.form.get('cpf')
        primeiro_nome = request.form.get('primeiro_nome')
        ultimo_nome = request.form.get('ultimo_nome')
        tipo_sanguineo = request.form.getlist('tipo_sanguineo')
        sexo = request.form.getlist('sexo')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')

        print(sexo[0])
        print(tipo_sanguineo[0])

        usuario = Usuarios.query.filter_by(cns=cns).first()
        if usuario:
            flash('CPF já existe.', category='error')
        elif len(cns) != 15:
            flash('CNS deve ter 15 números.', category='error')
        elif len(cpf) != 11:
            flash('CPF deve ter 11 números.', category='error')
        elif senha1 != senha2:
            flash('Senhas não coincidem.', category='error')
        elif len(senha1) < 7:
            flash('Senha deve ter pelo menos 7 caractéres.', category='error')
        else:
            novaPessoa = Pessoa(cns=cns, cpf=cpf, primeiro_nome=primeiro_nome, ultimo_nome=ultimo_nome, tipo_sanguineo=tipo_sanguineo[0], sexo=sexo[0])
            db.session.add(novaPessoa)
            novoUsuario = Usuarios(cns=cns, cpf=cpf, senha=generate_password_hash(senha1, method='sha256'))
            db.session.add(novoUsuario)
            db.session.commit()
           
            login_user(novoUsuario, remember=True)
            flash('Cadastro criado.', category='success')
           
            return redirect(url_for('views.paciente'))

    return render_template("signup.html", user=current_user)