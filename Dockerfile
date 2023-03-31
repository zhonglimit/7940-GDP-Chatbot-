FROM python
COPY chatbot.py .
COPY mongodb.py .
COPY OMDB.py .
COPY requirements.txt .
RUN pip install pip update
RUN pip install -r requirements.txt
ENV ACCESS_TOKEN=6125589283:AAExZVlNEXHDgtEKZWKitNPiX1jIjUvPRvs
ENV API_KEY=5e6f7556
ENV KEY=7940chatbot
ENV PASSWORD=O0kd7ozHMnmvmPQZ
ENV CLUSTER=cluster0.4tbcuza.mongodb.net
CMD python chatbot.py

