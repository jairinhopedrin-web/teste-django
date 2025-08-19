# 1. Pega uma imagem oficial do Python como base

FROM python:3.13.6-slim

# 2) Evita criação de .pyc e melhora logs

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3) Cria uma pasta de trabalho dentro do container (pode ter QUALQUER nome)

WORKDIR /app

# 4) Copia só requirements primeiro pra aproveitar cache entre builds

COPY requirements.txt .

# 5) Instala dependências do sistema (curl opcional; gcc apenas se sua lib precisar compilar)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
    && rm -rf /var/lib/apt/lists/*


# 6) Instala as dependências Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

# 7) Copia o restante do código
COPY . .

# 8) Expõe a porta do Django
EXPOSE 7030



# 9) Comando padrão: migrações + servidor dev
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0  :7030"]