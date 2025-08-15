# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt if exists
COPY requirements.txt ./

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy application code
COPY app.py ./

# Expose port (commonly 5000 for Flask)
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]