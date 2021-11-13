from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from .models import Consulta
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

@views.route('/consultas/nova_consulta/', methods=['GET', 'POST'])
@login_required
def nova_consulta():
    if request.method == 'POST':
        local = request.form['local']
        data = request.form.getlist('data')
        hora = request.form.getlist('hora')

        print(local[0])
        print(data[0])
        print(hora[0])

    return redirect('/consultas')

@views.route('/consultas/editar/<cod_consulta>')
def editar(cod_consulta):
    consulta = Consulta.query.get(cod_consulta)
    db.session.delete(consulta)
    db.session.commit()

    return redirect('/consultas')

@views.route('/consultas/apagar/<cod_consulta>')
def apagar(cod_consulta):
    consulta = Consulta.query.get(cod_consulta)
    db.session.delete(consulta)
    db.session.commit()

    return redirect('/consultas')

@views.route('/vacinas', methods=['GET', 'POST'])
@login_required
def vacinas():
    return render_template("vacinas.html", user=current_user)