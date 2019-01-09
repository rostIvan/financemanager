git clone https://github.com/rostIvan/financemanager
cd financemanager
virtualenv venv --no-site-packages
source venv/bin/activate
pip install -r requirements.txt
./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
./manage.py migrate
./manage.py makemigrations financemanager
./manage.py migrate
./manage.py runserver
