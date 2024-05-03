# Using official ubuntu image as a parent image
FROM python:3.9

ARG GRADIO_SERVER_PORT=7860
ENV GRADIO_SERVER_PORT=${GRADIO_SERVER_PORT}

# Setting the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD requirements.txt app.py /app/
# COPY . /app

# Getting the updates for Ubuntu and installing python into our environment
RUN python -m pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]