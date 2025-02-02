import openai


def get_openai_response(prompt):
    """
    Envia o prompt para a OpenAI e retorna a resposta com o contexto de Sensuality incluído.

    :param prompt: O texto a ser enviado para o modelo.
    :return: A resposta gerada pela OpenAI.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Sensuality é uma entidade digital responsável por exercer controle sobre as interações, alinhando-se com as regras e diretrizes do sistema Escudo Familiar."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip()
