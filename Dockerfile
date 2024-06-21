#base image
FROM python:3.11.5

#app working directory
WORKDIR /foodclass

# copy and install project requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN chmod +x entrypoint.sh
#RUN Project
ENTRYPOINT [ "./entrypoint.sh" ]
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]