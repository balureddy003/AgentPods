FROM python:3.10-slim

# Install runtime dependencies
RUN pip install --upgrade pip \
    && pip install autogenstudio

# Create a non-root user (optional, but best practice)
RUN useradd -m studiouser
USER studiouser
WORKDIR /home/studiouser

# Expose the default Studio port
EXPOSE 8081

# Run Studio
CMD ["autogenstudio", "ui", "--host", "0.0.0.0", "--port", "8081"]