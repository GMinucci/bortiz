FROM kennethreitz/pipenv
ENV PYTHONUNBUFFERED 1
MAINTAINER Rodrigo Teobaldo rgomes090@gmail.com

# Install pip requirements
# RUN set -ex && pip install pipenv --upgrade
RUN set -ex && pip install gunicorn

# Create config folder on /app
# RUN set -ex && mkdir /app

# Set the work directory to all commands after here
WORKDIR /app

# Copy pip requirements file to the container
ONBUILD COPY Pipfile .
ONBUILD COPY Pipfile.lock .

ONBUILD RUN set -ex && pipenv install --deploy --system
