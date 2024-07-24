# Usando uma imagem base do Python
FROM python:3.8-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos de requisitos
COPY requirements.txt requirements.txt

# Instala as dependências do Python
RUN pip install -r requirements.txt

# Copia o código do aplicativo para o contêiner
COPY . .

# Expõe a porta da API
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "igor/api.py"]
