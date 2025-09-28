# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina a variável de ambiente para que o Python não crie arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crie e defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de dependências e instale-as
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do projeto para o diretório de trabalho
COPY . .

# Exponha a porta que o FastAPI usa
EXPOSE 8000

# Comando para rodar a aplicação com Uvicorn
# O comando usa uvicorn para rodar o app 'main' do arquivo 'main.py' no host 0.0.0.0
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]