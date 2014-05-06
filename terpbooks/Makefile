.PHONY: runserver test report

runserver:
	python manage.py runserver 0.0.0.0:8000 --settings=terpbooks.settings.local

test:
	coverage run --source=books,terpbooks,transactions --omit=terpbooks/settings/*,*/admin.py,*/tests/*,terpbooks/wsgi.py manage.py test --settings=terpbooks.settings.test

report:
	coverage html
