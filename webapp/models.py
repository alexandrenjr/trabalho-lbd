from . import db
from flask_login import UserMixin


class Alergias(db.Model):
    cod_alergia = db.Column(db.String(5), primary_key=True)
    cns = db.Column(db.String(15), db.ForeignKey('pessoa.cns', ondelete='cascade', onupdate='cascade'), primary_key=True)
    nome_alergia = db.Column(db.String(50), nullable=False)

    pessoa = db.relationship('Pessoa', back_populates='alergias')

    def get_id(self):
        return (self.cod_consulta)

class Consulta(db.Model):
    cod_consulta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    local = db.Column(db.String(50), nullable=False)
    especialidade = db.Column(db.String(50), nullable=False)
    cns_paciente = db.Column(db.String(15), db.ForeignKey('paciente.cns_paciente', ondelete='cascade', onupdate='cascade'))

    exames = db.relationship('Exames', back_populates='consulta', cascade='all, delete')
    medicamentos = db.relationship('Medicamentos', back_populates='consulta', cascade='all, delete')
    paciente = db.relationship('Paciente', back_populates='consulta')
    profissional_saude = db.relationship('Profissional_saude', secondary='realiza_consulta', back_populates='consulta', passive_deletes=True)
    
    def get_id(self):
        return (self.cod_consulta)

class Exames(db.Model):
    cod_exame = db.Column(db.String(10), primary_key=True)
    cod_consulta = db.Column(db.Integer, db.ForeignKey('consulta.cod_consulta', ondelete='cascade', onupdate='cascade'), primary_key=True)
    nome_exame = db.Column(db.String(50), nullable=False)

    consulta = db.relationship('Consulta', back_populates='exames')

    def get_id(self):
        return (self.cod_exame)

class Medicamentos(db.Model):
    cod_medicamento = db.Column(db.String(10), primary_key=True)
    cod_consulta = db.Column(db.Integer, db.ForeignKey('consulta.cod_consulta', ondelete='cascade', onupdate='cascade'), primary_key=True)
    nome_medicamento = db.Column(db.String(50), nullable=False)

    consulta = db.relationship('Consulta', back_populates='medicamentos')

    def get_id(self):
        return (self.cod_medicamento)

class Paciente(db.Model):
    cns_paciente = db.Column(db.String(15), db.ForeignKey('pessoa.cns', ondelete='cascade', onupdate='cascade'), primary_key=True)
    altura = db.Column(db.Numeric(3,2))
    peso = db.Column(db.Numeric(4,1))

    consulta = db.relationship('Consulta', back_populates='paciente', cascade='all, delete')
    pessoa = db.relationship('Pessoa', back_populates='paciente', cascade='all, delete')

    def get_id(self):
        return (self.cns_paciente)

class Pessoa(db.Model):
    cns = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(11), unique=True)
    primeiro_nome = db.Column(db.String(50), nullable=False)
    ultimo_nome = db.Column(db.String(50), nullable=False)
    tipo_sanguineo = db.Column(db.String(3), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)

    alergias = db.relationship('Alergias', back_populates='pessoa', cascade='all, delete, delete-orphan')
    paciente = db.relationship('Paciente', back_populates='pessoa', uselist=False, cascade='all, delete, delete-orphan')
    profissional_saude = db.relationship('Profissional_saude', back_populates='pessoa', uselist=False, cascade='all, delete, delete-orphan')
    usuarios = db.relationship('Usuarios', back_populates='pessoa', uselist=False, cascade='all, delete, delete-orphan')
    vacinas = db.relationship('Vacinas', back_populates='pessoa', cascade='all, delete, delete-orphan')

    def get_id(self):
        return (self.cns)
    
    #def __init__(self, cns, cpf, primeiro_nome, ultimo_nome, tipo_sanguineo, sexo):
    #    self.cns = cns
    #    self.cpf = cpf
    #    self.primeiro_nome = primeiro_nome
    #    self.ultimo_nome = ultimo_nome
    #    self.tipo_sanguineo = tipo_sanguineo
    #    self.sexo = sexo

class Profissional_saude(db.Model):
    cr = db.Column(db.String(6), primary_key=True)
    cns_profissional_saude = db.Column(db.String(15), db.ForeignKey('pessoa.cns', ondelete='cascade', onupdate='cascade'))
    especialidade = db.Column(db.String(50))

    consulta = db.relationship('Consulta', secondary='realiza_consulta', back_populates='profissional_saude', cascade='all, delete')
    pessoa = db.relationship('Pessoa', back_populates='profissional_saude')

    def get_id(self):
        return (self.cr)

class Usuarios(db.Model, UserMixin):
    cns = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(11), db.ForeignKey('pessoa.cpf', ondelete='cascade', onupdate='cascade'), unique=True)
    senha = db.Column(db.String(150))

    pessoa = db.relationship('Pessoa', back_populates='usuarios')
    
    def get_id(self):
        return (self.cns)

class Vacinas(db.Model):
    cod_vacina = db.Column(db.String(10), primary_key=True)
    cns = db.Column(db.String(15), db.ForeignKey('pessoa.cns', ondelete='cascade', onupdate='cascade'), primary_key=True)
    obrigatoriedade = db.Column(db.Boolean, nullable=False)
    nome_vacina = db.Column(db.String(50), nullable=False)
    aplicada = db.Column(db.Boolean, nullable=False)

    pessoa = db.relationship('Pessoa', back_populates='vacinas')

    def get_id(self):
        return (self.cod_vacina)

## Tabela de associa????o entre Profissional_saude e Consulta
realiza_consulta = db.Table('realiza_consulta',
    db.Column('cr', db.String(6), db.ForeignKey('profissional_saude.cr', ondelete='cascade', onupdate='cascade'), primary_key=True),
    db.Column('cod_consulta', db.Integer, db.ForeignKey('consulta.cod_consulta', ondelete='cascade', onupdate='cascade'), primary_key=True)
)