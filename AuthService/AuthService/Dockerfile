# Include a python environment (alpine environments are small)
FROM python:3.9.10-slim-buster

# Set the working directory to /app
WORKDIR /AuthService

COPY requirements.txt requirements.txt

# Install the python dependencies
RUN apt-get update
RUN apt-get -y install gcc

RUN pip3 install -r requirements.txt


# Copy the current directory at host to /app of container
COPY . /AuthService

# Command for running python app
CMD [ "python", "manage.py", "runserver", "8000"]
