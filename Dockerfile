FROM ubuntu:latest 

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*


RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install flask flask_cors

COPY frontend/package*.json .

RUN npm install

COPY frontend .
COPY backend .

EXPOSE 5000 5173

CMD ["sh", "-c", "flask run --host=0.0.0.0 & npm run dev -- --port 5173 --host=0.0.0.0"]
