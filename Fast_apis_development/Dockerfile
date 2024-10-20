
FROM python:3.12


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt

# Debugging step: Check if the file exists
RUN ls -l /app/requirements.txt
RUN cat /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install "fastapi[standard]"


COPY . /app/


CMD ["fastapi", "run", "main.py", "--port", "8000"]