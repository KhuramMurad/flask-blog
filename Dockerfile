# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP run.py
ENV FLASK_ENV production

# Expose the Flask port
EXPOSE 5000

# Command to run the app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]

