.PHONY: runserver test report

runserver:
	python manage.py runserver 0.0.0.0:8000 --settings=terpbooks.settings.local

test:
	coverage run manage.py test --settings=terpbooks.settings.test

report:
	coverage html --omit=/home/vagrant/venvs/books/*,*/tests/*,*/migrations/*,*/admin.py
