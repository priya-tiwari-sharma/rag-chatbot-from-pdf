# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Django's development server will run on
EXPOSE 8000

# Start the Django development server with IP 0.0.0.0
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
