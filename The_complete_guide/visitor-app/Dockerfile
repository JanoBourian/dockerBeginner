#FROM
FROM python:3-alpine

#WORKDIR
WORKDIR /code

#COPY
COPY ./requirements.txt /code/requirements.txt

#RUN
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#COPY
COPY ./app /code/app

# CMD 
CMD ["uvicorn", "app.main:app", "--reload",  "--host", "0.0.0.0", "--port", "80"]