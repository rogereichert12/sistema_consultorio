document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const loginMessage = document.getElementById('login-message');
    const pacientesSection = document.getElementById('pacientes-section');
    const addPacienteForm = document.getElementById('add-paciente-form');
    const pacientesList = document.getElementById('pacientes-list');

    // Login
    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password }),
        });

        const result = await response.json();

        if (response.ok) {
            loginMessage.textContent = result.message;
            loginMessage.style.color = 'green';
            pacientesSection.style.display = 'block';
        } else {
            loginMessage.textContent = result.error;
            loginMessage.style.color = 'red';
        }
    });

    // Adicionar Paciente
    addPacienteForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const nome = document.getElementById('paciente-nome').value;
        const cpf = document.getElementById('paciente-cpf').value;
        const data_nascimento = document.getElementById('paciente-data-nascimento').value;

        const response = await fetch('http://127.0.0.1:5000/pacientes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nome, cpf, data_nascimento }),
        });

        if (response.ok) {
            const result = await response.json();
            alert(result.message);
            carregarPacientes(); // Atualiza a lista de pacientes
        }
    });

    // Carregar Pacientes
    async function carregarPacientes() {
        const response = await fetch('http://127.0.0.1:5000/pacientes');
        const pacientes = await response.json();

        pacientesList.innerHTML = ''; // Limpa a lista
        pacientes.forEach((paciente) => {
            const li = document.createElement('li');
            li.textContent = `${paciente.nome} (CPF: ${paciente.cpf})`;
            pacientesList.appendChild(li);
        });
    }
});
