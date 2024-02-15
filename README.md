# 1. Pull Docker Image
$ docker pull ghcr.io/nobodyknowse/gibis-rest:latest

# 2. Run Container
$ docker run -p 5000:5000 -p 5173:5173 ghcr.io/nobodyknowse/gibis-rest:latest

# 3. Open app
Local: http://localhost:5173/ \
Network: http://172.17.0.2:5173/


