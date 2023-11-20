# Using Python as a parent image
FROM python:3.10-slim-buster
# Working directory to my app in app.py
WORKDIR /app
# Copy the contents from the current directory into the app container
COPY . /app/
# Ensure that needed packages in the requirements.txt file are being installed
RUN pip install -r requirements.txt
# Specify the port 5000 being used and can be accessed
EXPOSE 5000
# Ensure the app can run container starts running
CMD ["python", "app.py"]

# Docker build command: docker build -t app .
# Docker run command: docker run -d -p 5001:5000 app