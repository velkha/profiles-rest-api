vagrant up
vagrant ssh
# Generate enviroment server
python -m venv ~/env

# Activar enviroment server
source ~/env/bin/activate

# Desactivar
deactivate

# En caso de dudas
[text](https://python-guide.readthedocs.io/en/latest/dev/virtualenvs/)

# Generate django
django-admin.py startproject profiles_project .

# Create project
python manage.py startapp profiles_api

# Start server
cd /vagrant
python manage.py runserver 0.0.0.0:8000

# Generate migrations
python manage.py makemigrations app_name

# Migrate
python manage.py migrate

# Create default admin
Email: Admin@django.com
Password: LocalAdmin2468++