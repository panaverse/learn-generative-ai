# Use a specific tag for a more stable and predictable base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

# Set work directory
WORKDIR /workspace/

# Install curl and other dependencies you might need
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies required for installing Python packages
# This is skipped because the base image should already contain all the necessary build tools

# Install Poetry in a single layer to reduce image size and complexity
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copying poetry files first to cache dependencies
COPY pyproject.toml poetry.lock* /workspace/

# Install only production dependencies in a single layer to reduce image size
RUN poetry install --no-root --no-dev

# Copy the application code in a later step to take advantage of Docker layer caching
COPY ./app /workspace/app
COPY .env /workspace/

# Set up a non-root user for better security
RUN useradd --create-home --home-dir /home/appuser appuser \
    && chown -R appuser:appuser /workspace

USER appuser

# Set the work directory and continue with the Dockerfile setup...
ENV PYTHONPATH=/workspace

# Optimize Gunicorn config for production
# This includes adjustments for worker numbers, timeouts, etc., based on your app's needs and the hardware it runs on
CMD ["poetry", "run", "gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "4", "--worker-tmp-dir", "/dev/shm", "--log-file", "-", "--bind", "0.0.0.0:8000"]
