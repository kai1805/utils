# Start with a base ubuntu image
FROM python:3.10-slim

# install python3 and needed packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command
CMD ["python", "index.py"]
