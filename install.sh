#!/bin/bash

# Installer script for Hashmicro Django Project

# Update package list and install Python and pip
echo "Installing Python and pip..."
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install virtualenv
echo "Installing virtualenv..."
pip3 install virtualenv

# Create a virtual environment
echo "Creating virtual environment..."
virtualenv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate

Create a superuser (optional)
echo "Creating superuser..."
python manage.py createsuperuser

# Collect static files (if needed)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn..."
gunicorn --config gunicorn.conf.py project.wsgi:application

echo "Installation complete! Access the application at http://<server-ip>:8000/hashmicro_project/"