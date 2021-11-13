from . import db
from flask_login import UserMixin


class Alergias(db.Model):
    cod_alergia = db.Column(db.String(5), primary_key=True)
    cns = db.Column(db.String(15), db.ForeignKey('pessoa.cns'), primary_key=True)
    nome_alergia = db.Column(db.String(50), nullable=False)

    pessoa = db.relationship('Pessoa', back_populates='alergias')

    def get_id(self):
        return (self.cod_consulta)

class Consulta(db.Model):
    cod_consulta = db.Column(db.String(10), primary_key=True)
    tipo_consulta = db.Column(db.Boolean, nullable=False)
    data = db.Column(db.DateTime(timezone=True), nullable=False)
    local = db.Column(db.String(50), nullable=False)
    cns_paciente = db.Column(db.String(15), db.ForeignKey('paciente.cns_paciente'))

    exames = db.relationship('Exames', cascade='all, delete, save-update', back_populates='consulta')
    medicamentos = db.relationship('Medicamentos', cascade='all, delete, save-update', back_populates='consulta')
    paciente = db.relationship('Paciente', back_populates='consulta')
    profissional_saude = db.relationship('Profissional_saude', secondary='realiza_consulta', back_populates='consulta')
    
    def get_id(self):
        return (self.cod_consulta)

class Exames(db.Model):
    cod_exame = db.Column(db.String(10), primary_key=True)
    cod_consulta = db.Column(db.String(10), db.ForeignKey('consulta.cod_consulta'), primary_key=True)
    nome_exame = db.Column(db.String(50), nullable=False)

    consulta = db.relationship('Consulta', back_populates='exames')

    def get_id(self):
        return (self.cod_exame)

class Medicamentos(db.Model):
    cod_medicamento = db.Column(db.String(10), primary_key=True)
    cod_consulta = db.Column(db.String(10), db.ForeignKey('consulta.cod_consulta'), primary_key=True)
    nome_medicamento = db.Column(db.String(50), nullable=False)

    consulta = db.relationship('Consulta', back_populates='medicamentos')

    def get_id(self):
        return (self.cod_medicamento)

class Paciente(db.Model):
    cns_paciente = db.Column(db.String(15), db.ForeignKey('pessoa.cns'), primary_key=True)
    altura = db.Column(db.Numeric(3,2))
    peso = db.Column(db.Numeric(4,1))

    consulta = db.relationship('Consulta', back_populates='paciente')
    pessoa = db.relationship('Pessoa', cascade='all, delete, save-update', back_populates='paciente')

    def get_id(self):
        return (self.cns_paciente)

class Pessoa(db.Model):
    cns = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(11), unique=True)
    primeiro_nome = db.Column(db.String(50), nullable=False)
    ultimo_nome = db.Column(db.String(50), nullable=False)
    tipo_sanguineo = db.Column(db.String(3), nullable=False)
    sexo = db.Column(db.String(1), nullable=False)

    alergias = db.relationship('Alergias', cascade='all, delete, save-update', back_populates='pessoa')
    paciente = db.relationship('Paciente', cascade='all, delete, save-update', back_populates='pessoa', uselist=False)
    usuarios = db.relationship('Usuarios', cascade='all, delete, save-update', back_populates='pessoa', uselist=False)
    vacinas = db.relationship('Vacinas', cascade='all, delete, save-update', back_populates='pessoa')

    def get_id(self):
        return (self.cns)
    
    #def __init__(self, cns, cpf, primeiro_nome, ultimo_nome, tipo_sanguineo, sexo):
    #    self.cns = cns
    #    self.cpf = cpf
    #    self.primeiro_nome = primeiro_nome
    #    self.ultimo_nome = ultimo_nome
    #    self.tipo_sanguineo = tipo_sanguineo
    #    self.sexo = sexo

class Prfssnl_sd_especialidade(db.Model):
    especialidade = db.Column(db.String(50), primary_key=True)
    cr = db.Column(db.String(6), db.ForeignKey('profissional_saude.cr'), primary_key=True)

    profissional_saude = db.relationship('Profissional_saude', cascade='all, delete, save-update', back_populates='prfssnl_sd_especialidade')

    def get_id(self):
        return (self.especialidade)

class Profissional_saude(db.Model):
    cr = db.Column(db.String(6), primary_key=True)
    cns_profissional_saude = db.Column(db.String(15), db.ForeignKey('pessoa.cns'))

    consulta = db.relationship('Consulta', secondary='realiza_consulta', cascade='all, delete, save-update', back_populates='profissional_saude')
    prfssnl_sd_especialidade = db.relationship('Prfssnl_sd_especialidade', cascade='all, delete, save-update', back_populates='profissional_saude', uselist=False)

    def get_id(self):
        return (self.cr)

class Usuarios(db.Model, UserMixin):
    cns = db.Column(db.String(15), primary_key=True)
    cpf = db.Column(db.String(11), db.ForeignKey('pessoa.cpf'), unique=True)
    senha = db.Column(db.String(150))

    pessoa = db.relationship('Pessoa', cascade='all, delete, save-update', back_populates='usuarios')
    
    def get_id(self):
        return (self.cns)

class Vacinas(db.Model):
    cod_vacina = db.Column(db.String(10), primary_key=True)
    cns = db.Column(db.String(15), db.ForeignKey('pessoa.cns'), primary_key=True)
    obrigatoriedade = db.Column(db.Boolean, nullable=False)
    nome_vacina = db.Column(db.String(50), nullable=False)
    aplicada = db.Column(db.Boolean, nullable=False)

    pessoa = db.relationship('Pessoa', back_populates='vacinas')

    def get_id(self):
        return (self.cod_vacina)

## Tabela de associação entre Profissional_saude e Consulta
realiza_consulta = db.Table('realiza_consulta',
    db.Column('cr', db.String(6), db.ForeignKey('profissional_saude.cr'), primary_key=True),
    db.Column('cod_consulta', db.String(10), db.ForeignKey('consulta.cod_consulta'), primary_key=True)
)