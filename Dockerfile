# Python light image
FROM python:3.11-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app
WORKDIR /app

# Copy project files into the app container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make sure the script is executable
RUN chmod +x entrypoint.sh

# Use it as the container entrypoint
CMD ["sh", "entrypoint.sh"]