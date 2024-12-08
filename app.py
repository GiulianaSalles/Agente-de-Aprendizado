from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend do Guia de Idiomas está funcionando!"

@app.route('/gramatica', methods=['POST'])
def gramatica():
    dados = request.json
    frase = dados.get('frase', '')
    # Aqui chamamos a função corrigir_frase_e_explicar
    correcao, explicacao = corrigir_frase_e_explicar(client, frase)
    return jsonify({"correcao": correcao, "explicacao": explicacao})

@app.route('/plano_estudos', methods=['POST'])
def plano_estudos():
    dados = request.json
    frases = dados.get('frases', [])
    plano = gerar_plano_de_estudos(" ".join(frases))
    return jsonify({"plano": plano})

if __name__ == "__main__":
    app.run(debug=True)
