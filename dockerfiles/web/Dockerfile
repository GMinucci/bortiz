FROM kennethreitz/pipenv
ENV PYTHONUNBUFFERED 1
MAINTAINER Rodrigo Teobaldo rgomes090@gmail.com

# Install pip requirements
# RUN set -ex && pip install pipenv --upgrade
RUN set -ex && pip install gunicorn

# Create config folder on /app
# RUN set -ex && mkdir /app

# Copy entrypoint script
COPY dockerfiles/web/entrypoint.sh /entrypoint.sh

# Give scripts run permission
RUN chmod +x /entrypoint.sh

# Set the work directory to all commands after here
WORKDIR /app

# Copy pip requirements file to the container
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

ONBUILD RUN set -ex && pipenv install --deploy --system
