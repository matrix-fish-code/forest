import pytest
from app import app  # Certifique-se de que o caminho está correto

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200  # Verifica se o status da resposta é 200
        assert b'Flask backend running!' in response.data  # Verifica se a mensagem "Flask backend running!" está presente no conteúdo
