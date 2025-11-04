FROM python:3.8-slim

# 安装Tkinter依赖
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# 安装项目依赖
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "src/calculator.py"]

