from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from .models import Consulta, Pessoa, Profissional_saude, Vacinas
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template("inicio.html", user=current_user)

@views.route('/area-do-paciente', methods=['GET', 'POST'])
@login_required
def paciente():
    return render_template("paciente.html", user=current_user)

@views.route('/consultas', methods=['GET', 'POST'])
@login_required
def consultas():

    return render_template("consultas.html", user=current_user)

@views.route('/nova-consulta/', methods=['GET', 'POST'])
@login_required
def nova_consulta():
    especialidades = db.session.query(Profissional_saude.especialidade)

    if request.method == 'POST':
        local = request.form.get('local')
        data = request.form.get('data')
        hora = request.form.get('hora')

        print(local)
        print(data)
        print(hora)

        return redirect('/consultas')
    return render_template("novaconsulta.html", user=current_user, especialidades=especialidades)


@views.route('/editar/<cod_consulta>')
def editar(cod_consulta):
    consulta = Consulta.query.get(cod_consulta)
    db.session.delete(consulta)
    db.session.commit()

    return redirect('/consultas')

@views.route('/apagar/<cod_consulta>')
def apagar(cod_consulta):
    consulta = Consulta.query.get(cod_consulta)
    db.session.delete(consulta)
    db.session.commit()

    return redirect('/consultas')

@views.route('/vacinas/<cns>', methods=['GET', 'POST'])
@login_required
def vacinas(cns):
    vacinas = Vacinas.query.filter_by(cns=cns)
    
    return render_template("vacinas.html", user=current_user, vacinas=vacinas)