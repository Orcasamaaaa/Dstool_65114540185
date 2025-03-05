
FROM python:3.11-slim 

WORKDIR /webproject

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate

EXPOSE 9999

CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]
