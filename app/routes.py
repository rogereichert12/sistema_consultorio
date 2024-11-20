from flask import Blueprint, request, jsonify
from .models import db, Paciente, Medico, Agendamento

app_routes = Blueprint('app_routes', __name__)

# Login
@app_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Simulação: substituir por lógica real
    if username == "admin" and password == "admin":
        return jsonify({"message": "Login realizado com sucesso!"}), 200
    return jsonify({"error": "Credenciais inválidas"}), 401

# Logout
@app_routes.route('/logout', methods=['POST'])
def logout():
    return jsonify({"message": "Logout realizado com sucesso!"}), 200

# Cadastro de pacientes
@app_routes.route('/pacientes', methods=['POST'])
def cadastrar_paciente():
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

# Listagem de pacientes
@app_routes.route('/pacientes', methods=['GET'])
def listar_pacientes():
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

# Cadastro de médicos
@app_routes.route('/medicos', methods=['POST'])
def cadastrar_medico():
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

# Listagem de médicos
@app_routes.route('/medicos', methods=['GET'])
def listar_medicos():
    medicos = Medico.query.all()
    return jsonify([{
        "id": m.id,
        "nome": m.nome,
        "telefone": m.telefone,
        "email": m.email,
        "horario_inicio": m.horario_inicio.strftime('%H:%M:%S'),
        "horario_fim": m.horario_fim.strftime('%H:%M:%S')
    } for m in medicos]), 200

# Criação de agendamentos
@app_routes.route('/agendamentos', methods=['POST'])
def criar_agendamento():
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
