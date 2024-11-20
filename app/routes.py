from flask import Blueprint, request, jsonify
from .models import db, Paciente, Medico, Agendamento

# Definição do Blueprint
app_routes = Blueprint('app_routes', __name__)

# ---------------------------
# Autenticação
# ---------------------------

@app_routes.route('/login', methods=['POST'])
def login():
    """
    Rota de login do sistema.

    Recebe um JSON contendo `username` e `password`. Verifica as credenciais e retorna 
    uma mensagem de sucesso ou erro. Simulação simples para fins de desenvolvimento.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Simulação de login
    if username == "admin" and password == "admin":
        return jsonify({"message": "Login realizado com sucesso!"}), 200
    return jsonify({"error": "Credenciais inválidas"}), 401


@app_routes.route('/logout', methods=['POST'])
def logout():
    """
    Rota de logout do sistema.

    Realiza o logout do usuário e retorna uma mensagem de sucesso.
    """
    return jsonify({"message": "Logout realizado com sucesso!"}), 200

# ---------------------------
# Gerenciamento de Pacientes
# ---------------------------

@app_routes.route('/pacientes', methods=['POST'])
def cadastrar_paciente():
    """
    Rota para cadastrar pacientes.

    Recebe um JSON com os dados do paciente (`nome`, `cpf`, `data_nascimento`, 
    `telefone`, `email`, `endereco`). Armazena os dados no banco de dados e 
    retorna uma mensagem de sucesso.
    """
    data = request.json
    paciente = Paciente(
        nome=data.get('nome'),
        cpf=data.get('cpf'),
        data_nascimento=data.get('data_nascimento'),
        telefone=data.get('telefone'),
        email=data.get('email'),
        endereco=data.get('endereco')
    )
    db.session.add(paciente)
    db.session.commit()
    return jsonify({"message": "Paciente cadastrado com sucesso!"}), 201


@app_routes.route('/pacientes', methods=['GET'])
def listar_pacientes():
    """
    Rota para listar pacientes.

    Retorna uma lista em formato JSON com todos os pacientes cadastrados, incluindo 
    `id`, `nome`, `cpf`, `data_nascimento`, `telefone`, `email` e `endereco`.
    """
    pacientes = Paciente.query.all()
    return jsonify([{
        "id": p.id,
        "nome": p.nome,
        "cpf": p.cpf,
        "data_nascimento": p.data_nascimento.strftime('%Y-%m-%d'),
        "telefone": p.telefone,
        "email": p.email,
        "endereco": p.endereco
    } for p in pacientes]), 200

# ---------------------------
# Gerenciamento de Médicos
# ---------------------------

@app_routes.route('/medicos', methods=['POST'])
def cadastrar_medico():
    """
    Rota para cadastrar médicos.

    Recebe um JSON com os dados do médico (`nome`, `telefone`, `email`, 
    `horario_inicio`, `horario_fim`). Armazena os dados no banco de dados e 
    retorna uma mensagem de sucesso.
    """
    data = request.json
    medico = Medico(
        nome=data.get('nome'),
        telefone=data.get('telefone'),
        email=data.get('email'),
        horario_inicio=data.get('horario_inicio'),
        horario_fim=data.get('horario_fim')
    )
    db.session.add(medico)
    db.session.commit()
    return jsonify({"message": "Médico cadastrado com sucesso!"}), 201


@app_routes.route('/medicos', methods=['GET'])
def listar_medicos():
    """
    Rota para listar médicos.

    Retorna uma lista em formato JSON com todos os médicos cadastrados, incluindo 
    `id`, `nome`, `telefone`, `email`, `horario_inicio` e `horario_fim`.
    """
    medicos = Medico.query.all()
    return jsonify([{
        "id": m.id,
        "nome": m.nome,
        "telefone": m.telefone,
        "email": m.email,
        "horario_inicio": m.horario_inicio.strftime('%H:%M:%S'),
        "horario_fim": m.horario_fim.strftime('%H:%M:%S')
    } for m in medicos]), 200

# ---------------------------
# Gerenciamento de Agendamentos
# ---------------------------

@app_routes.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    """
    Rota para criar agendamentos.

    Recebe um JSON com os dados do agendamento (`data`, `horario`, `paciente_id`, 
    `medico_id`). Armazena o agendamento no banco de dados e retorna uma mensagem 
    de sucesso.
    """
    data = request.json
    agendamento = Agendamento(
        data=data.get('data'),
        horario=data.get('horario'),
        paciente_id=data.get('paciente_id'),
        medico_id=data.get('medico_id'),
        status='Agendado'
    )
    db.session.add(agendamento)
    db.session.commit()
    return jsonify({"message": "Agendamento criado com sucesso!"}), 201


@app_routes.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    """
    Rota para listar agendamentos.

    Retorna uma lista em formato JSON com todos os agendamentos, incluindo 
    `id`, `data`, `horario`, `paciente_id`, `medico_id` e `status`.
    """
    agendamentos = Agendamento.query.all()
    return jsonify([{
        "id": a.id,
        "data": a.data.strftime('%Y-%m-%d'),
        "horario": a.horario.strftime('%H:%M:%S'),
        "paciente_id": a.paciente_id,
        "medico_id": a.medico_id,
        "status": a.status
    } for a in agendamentos]), 200
