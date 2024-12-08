document.getElementById('gramatica').addEventListener('click', () => {
    fetch('/gramatica', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resposta').innerHTML = `<p><strong>Correção:</strong> ${data.correcao}</p><p><strong>Explicação:</strong> ${data.explicacao}</p>`;
    });
});

document.getElementById('plano_estudos').addEventListener('click', () => {
    fetch('/plano_estudos', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resposta').innerHTML = `<p><strong>Plano de Estudos:</strong> ${data.plano}</p>`;
    });
});
