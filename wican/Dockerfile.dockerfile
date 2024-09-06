FROM python:3.9-slim

# Install necessary dependencies
RUN pip install requests

# Copy over the Python script and configuration
COPY app.py /app.py

# Start the Python script
CMD ["python", "/app.py"]
