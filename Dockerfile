FROM python:3.6
ENV PYTHONUNBUFFERED 1
MAINTAINER Rodrigo Teobaldo rgomes090@gmail.com

# Create config folder on /
# RUN mkdir /config

# Copy pip requirements file to the container
# ADD /Pipfile /

# Copy the start_command.sh file to the container
# ADD /config/start_command.sh /config/

# Give run permissions to the start_command file
# RUN chmod 755 /config/start_command.sh

# Install pip requirements
RUN pip install pipenv
RUN pipenv install --system

# Create web-media folder to handle static files
# RUN mkdir /web-media

# Set the work directory to all commands after here
# WORKDIR /src
