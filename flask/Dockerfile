FROM python:3-slim
COPY app.py /app/app.py
WORKDIR /app 
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python", "app.py"] 
