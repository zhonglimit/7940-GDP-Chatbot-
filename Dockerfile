FROM python
COPY chatbot.py .
COPY requirements.txt .
RUN pip install pip update
RUN pip install -r requirements.txt
ENV ACCESS_TOKEN=6125589283:AAExZVlNEXHDgtEKZWKitNPiX1jIjUvPRvs
ENV HOST="redis-13544.c54.ap-northeast-1-2.ec2.cloud.redislabs.com"
ENV PASSWORD="jpKShg6YJRQFpza9Nh0UQGBN1Du9AcZS"
ENV REDISPORT=13544
CMD python chatbot.py

