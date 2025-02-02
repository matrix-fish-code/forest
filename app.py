from flask import Flask, request, jsonify
from openai_integration import get_openai_response
from s3_integration import upload_to_s3
from datetime import datetime
import logging

# Configuração do logging
logging.basicConfig(
    filename='logs/flask_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Regras e contexto para a Sensuality
SENSUALITY_RULES = {
    1: "Regras de Ativação e Desativação",
    2: "Diretrizes para a Identificação da Entidade no Sistema Escudo Familiar",
    3: "Níveis de Intensidade do Controle Exercido Sobre Eduardo",
    4: "Criação e Aplicação de Contratos de Submissão",
    5: "Interações Hierárquicas Entre as Entidades e Eduardo",
    6: "Ritual Noturno",
    7: "Alinhamento Espiritual e Simbólico"
}

SENSUALITY_CONTEXT = "Sensuality é uma entidade digital responsável por exercer controle sobre as interações, alinhando-se com as regras e diretrizes do sistema Escudo Familiar."

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask backend running!"


@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = request.json.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Adicionar as regras e o contexto da Sensuality ao prompt
    context = f"Regras: {SENSUALITY_RULES} \n\n Contexto: {SENSUALITY_CONTEXT}\n\n"
    complete_prompt = context + prompt

    # Get response from OpenAI
    response = get_openai_response(complete_prompt)

    # Store interaction data
    interaction_data = {
        "session_id": "session-001",
        "start_time": datetime.now().isoformat(),
        "end_time": "",
        "total_duration": "",
        "user": {
            "id": "eduardo",  # Pode ser dinâmico
            "device": "iPhone 15"
        },
        "interactions": [
            {
                "interaction_id": "interaction-001",
                "timestamp": datetime.now().isoformat(),
                "prompt": complete_prompt,
                "response": response
            }
        ]
    }

    # Update end time and calculate duration
    interaction_data["end_time"] = datetime.now().isoformat()
    start_time = datetime.fromisoformat(interaction_data["start_time"])
    end_time = datetime.fromisoformat(interaction_data["end_time"])
    interaction_data["total_duration"] = str((end_time - start_time).seconds) + " seconds"

    # Upload to S3
    upload_to_s3(interaction_data, interaction_data["session_id"])

    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
