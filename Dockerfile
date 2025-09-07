# Instruct BuildKit to pull the latest stable version of Dockerfile syntax before the build
# syntax=docker/dockerfile:1
FROM mambaorg/micromamba:latest AS base

ARG MAMBA_DOCKERFILE_ACTIVATE=1
WORKDIR /workspace
USER mambauser

# Copy the env file
COPY --chown=mambauser:mambauser devops-conda-env.yml /tmp/env.yml
# Install Python deps into the *base* environment (most robust in containers)
RUN micromamba install -y -n base -f /tmp/env.yml && micromamba clean -a -y

# Copy app files
COPY --chown=mambauser:mambauser app /workspace/app

# Expose Gradio's default port
EXPOSE 7860

# Simple healthcheck for root path using Python
HEALTHCHECK --interval=60s --timeout=5s --start-period=20s --retries=3 \
  CMD micromamba run -n base python -c "import sys,urllib.request; \
    import socket; socket.setdefaulttimeout(4); \
    urllib.request.urlopen('http://127.0.0.1:7860/'); \
    sys.exit(0)"

# Run the app
CMD ["micromamba", "run", "-n", "base", "python", "-m", "app.main"]
