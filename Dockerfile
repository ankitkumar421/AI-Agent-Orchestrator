FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for AI libraries and search tools
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    python3-dev \
    gcc \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade core pip tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Final networking cleanup
RUN rm -rf .streamlit/config.toml

EXPOSE 8501

# Headless mode ensures the WebSocket handshake succeeds in Docker
CMD ["streamlit", "run", "app.py", \
    "--server.port=8501", \
    "--server.address=0.0.0.0", \
    "--server.headless=true", \
    "--server.enableCORS=false", \
    "--server.enableXsrfProtection=false"]