# Pull a base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Change working directory
WORKDIR /backend/

# Copy requirements to the container
COPY requirements.txt /backend/

# Install the requirements to the container
RUN pip3 install -r requirements.txt

# Copy the project files into the working directory
COPY . /backend/

# Open a port on the container
EXPOSE 8000
