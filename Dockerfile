FROM python:3.11-alpine
WORKDIR /ascii-lab3
COPY summ.py .
ENTRYPOINT ["python", "summ.py"]
