from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Alergias(db.Model):
    cod_alergia = db.Column(db.String(5), primary_key=True)
    cns = db.Column(db.String(15), db.ForeignKey('pessoa.cns'))
    tipo_alergia = db.Column(db.Boolean)
    nome_alergia = db.Column(db.String(50))

    def get_id(self):
        return (self.cod_consulta)

class Consulta(db.Model):
    cod_consulta = db.Column(db.String(10), primary_key=True)
    tipo_consulta = db.Column(db.Boolean())
    data = db.Column(db.DateTime(timezone=True))
    local = db.Column(db.String(50))
    cns_paciente = db.Column(db.String(15))

    def get_id(self):
        return (self.cod_consulta)

class Exames(db.Model):
    cod_exame = db.Column(db.String(10), primary_key=True)
    cod_consulta = db.Column(db.String(10), unique=True)
    nome_exame = db.Column(db.String(50))

    def get_id(self):
        return (self.cod_exame)

class Medicamentos(db.Model):
    cod_medicamento = db.Column(db.String(10), primary_key=True)
    cod_consulta = db.Column(db.String(10), unique=True)
    nome_medicamento = db.Column(db.String(50))

    def get_id(self):
        return (self.cod_medicamento)

class Paciente(db.Model):
    cns_paciente = db.Column(db.String(15), primary_key=True)
    altura = db.Column(db.Numeric(3,2))
    peso = db.Column(db.Numeric(4,1))

    def get_id(self):
        return (self.cns_paciente)

class Pessoa(db.Model):
    cns = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(11), unique=True)
    primeiro_nome = db.Column(db.String(50))
    utimo_nome = db.Column(db.String(50))
    tipo_sanguineo = db.Column(db.String(3))
    sexo = db.Column(db.String(1))

    def get_id(self):
        return (self.cns)

class Profssnl_sd_especialidade(db.Model):
    especialidade = db.Column(db.String(50), primary_key=True)
    cr = db.Column(db.String(6), unique=True)
    interno = db.Column(db.Boolean())

    def get_id(self):
        return (self.especialidade)

class Profissional_saude(db.Model):
    cr = db.Column(db.String(6), primary_key=True)
    tipo_profissional_saude = db.Column(db.String(1))
    cns_profissional_saude = db.Column(db.String(15))

    def get_id(self):
        return (self.cr)

class Realiza_consulta(db.Model):
    cr = db.Column(db.String(6), primary_key=True)
    cod_consulta = db.Column(db.String(10), unique=True)
    duracao_consulta = db.Column(db.Time())
    
    def get_id(self):
        return (self.cr)

class Usuario(db.Model, UserMixin):
    cns = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(11), unique=True)
    senha = db.Column(db.String(150))
    
    def get_id(self):
        return (self.cns)

class Vacina(db.Model):
    cod_vacina = db.Column(db.String(10), primary_key=True)
    obrigatoriedade = db.Column(db.Boolean())
    nome_vacina = db.Column(db.String(50))
    aplicada = db.Column(db.Boolean())

    def get_id(self):
        return (self.cod_vacina)