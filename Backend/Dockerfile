# Use a lightweight Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt into the container
COPY Backend/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the backend code into the container
COPY Backend /app/Backend

# Set environment variables (if needed)
ENV PYTHONUNBUFFERED=1

# Expose the app port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "Backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
