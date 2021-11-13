from flask import Blueprint, render_template
from flask_login import login_required, current_user

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

@views.route('/vacinas', methods=['GET', 'POST'])
@login_required
def vacinas():
    return render_template("vacinas.html", user=current_user)