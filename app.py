from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Carrega o modelo treinado
model = tf.keras.models.load_model('modelo_ia.keras')

# Rota principal para verificar se o servidor está funcionando
@app.route('/')
def home():
    return "Servidor Flask está rodando!"

# Rota para renderizar uma página HTML
@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

# Rota para previsão usando o modelo treinado
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Verifica se os dados estão no formato esperado
        dados = request.get_json()
        if not dados or 'input' not in dados:
            return jsonify({'error': 'O campo "input" não foi encontrado no JSON fornecido.'}), 400
        
        # Converte os dados de entrada para o formato esperado pelo modelo (um array numpy)
        input_data = np.array(dados['input'])
        
        # Certifique-se de que a entrada tem a forma correta (n_samples, 4)
        if input_data.ndim == 3 and input_data.shape[1] == 2:
            input_data = input_data.reshape(-1, input_data.shape[-1])
        
        # Realiza a previsão
        previsao = model.predict(input_data)
        
        # Retorna a previsão como resposta JSON
        return jsonify({'previsao': previsao.tolist()})
    
    except Exception as e:
        # Retorna uma mensagem de erro detalhada
        return jsonify({'error': f'Erro ao processar a solicitação: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
