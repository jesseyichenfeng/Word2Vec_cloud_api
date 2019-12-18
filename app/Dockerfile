FROM python:3.6

WORKDIR /var/app
COPY . .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--timeout", "3600" ,"app:app", "--bind", "0.0.0.0:5000"]