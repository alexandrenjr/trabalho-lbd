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
    consultas = Consulta.query.filter_by(cns_paciente=current_user.cns)
    nomePrfssnlSd = Consulta.query.all()
    print(nomePrfssnlSd)
    return render_template("consultas.html", user=current_user, consultas=consultas, profissional_saude=nomePrfssnlSd)

@views.route('/nova-consulta/', methods=['GET', 'POST'])
@login_required
def nova_consulta():
    especialidades = db.session.query(Profissional_saude.especialidade)

    if request.method == 'POST':
        cns_paciente = current_user.cns
        especialidade = request.form.get('especialidade')
        local = request.form.get('local')
        data = request.form.get('data')
        hora = request.form.get('hora')

        novaConsulta = Consulta(cns_paciente=cns_paciente,
            local=local,
            hora=hora,
            data=data
        )

        cr = Profissional_saude.query.filter_by(especialidade=especialidade).first()
        novaConsulta.profissional_saude.append(cr)
        db.session.add(novaConsulta)
        db.session.commit()

        return redirect('/consultas')
    return render_template("nova.html", user=current_user, especialidades=especialidades)

@views.route('/editar/<cod_consulta>/', methods=['GET', 'POST'])
@login_required
def editar(cod_consulta):
    consulta = Consulta.query.get(cod_consulta)
    especialidades = db.session.query(Profissional_saude.especialidade)

    if request.method == 'POST':
        consulta.especialidade = request.form.get('especialidade')
        consulta.local = request.form.get('local')
        consulta.data = request.form.get('data')
        consulta.hora = request.form.get('hora')

        cr = Profissional_saude.query.filter_by(especialidade=consulta.especialidade).first()
        consulta.profissional_saude.append(cr)
        db.session.commit()

        return redirect('/consultas')
    return render_template("editar.html", user=current_user, consulta=consulta, especialidades=especialidades)

@views.route('/desmarcar/<cod_consulta>')
@login_required
def desmarcar(cod_consulta):
    consulta = Consulta.query.get(cod_consulta)
    db.session.delete(consulta)
    db.session.commit()

    return redirect('/consultas')

@views.route('/vacinas/<cns>', methods=['GET', 'POST'])
@login_required
def vacinas(cns):
    vacinas = Vacinas.query.filter_by(cns=cns)
    
    return render_template("vacinas.html", user=current_user, vacinas=vacinas)