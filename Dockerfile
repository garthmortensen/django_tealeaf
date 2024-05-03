FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# for clarity, copy requirements first
COPY requirements.txt /app/

# copy everything else
COPY . /app/

# Give execution rights on the entrypoint script
RUN chmod +x /app/manage.py

# upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Collect static files
# RUN python manage.py collectstatic --noinput
# Start Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]

# Build the image
# if using docker, simply replace the word podman with docker
# (.venv) ➜  leftbrace git:(main) ✗ podman build -t leftbrace_django .
# (.venv) ➜  leftbrace git:(main) ✗ podman run -d -p 8000:8000 leftbrace_django:latest
# (.venv) ➜  leftbrace git:(main) ✗ podman ps -a
# (.venv) ➜  leftbrace git:(main) ✗ podman stop {id}
# (.venv) ➜  leftbrace git:(main) ✗ podman rm {id}
# (.venv) ➜  leftbrace git:(main) ✗ podman container prune

# (.venv) ➜  leftbrace git:(main) ✗ podman-compose up --build

# you can also run the container in interactive mode and test
# (.venv) ➜  leftbrace git:(main) ✗ podman run -it -p 8000:8000 --entrypoint /bin/bash leftbrace_django:latest 
# (.venv) ➜  leftbrace git:(main) ✗ python manage.py runserver 0.0.0.0:8000

# to remove the images that you've already built
# (.venv) ➜  leftbrace git:(main) ✗ podman images
# (.venv) ➜  leftbrace git:(main) ✗ podman rmi {id}