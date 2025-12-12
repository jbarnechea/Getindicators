FROM python:3.14.0
WORKDIR /app
COPY requeriments.txt requeriments.txt
RUN pip3 install -r requeriments.txt
COPY . .
CMD ["python", "-m", "flask","run", "--host=0.0.0.0"]
