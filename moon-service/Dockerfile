FROM python:3.11.5
WORKDIR /code
EXPOSE 80
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./main.py /code/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]