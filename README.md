# Projeto de Integração com OpenAI e AWS S3

Este projeto tem como objetivo integrar a API da OpenAI com a AWS S3 para armazenar interações em tempo real. Utiliza Flask como backend para processar as requisições e exibir respostas.

## Como Rodar o Projeto

### Instalação

1. Clonar o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Instalar dependências:

   pip install -r requirements.txt

### Configuração

Adicionar chaves de API no arquivo .env:

OPENAI_API_KEY=your_openai_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key

### Rodar o Servidor Flask

python src/app.py

### Testes

Rodar testes:

python -m unittest discover

### Estrutura do Projeto

- /src: Código fonte
- /templates: Arquivos HTML
- /static: Arquivos estáticos (CSS, JS)
- /logs: Logs de execução
- /tests: Testes automatizados
- README.md: Documentação do projeto
- .env: Configuração de variáveis sensíveis
