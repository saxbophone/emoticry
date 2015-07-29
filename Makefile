install:
	pip install -r python_requirements/base.txt
	pip install -r python_requirements/test.txt

clean:
	rm -rf emoticry/*.py[cod]
	rm -rf tests/*.py[cod]
	rm -rf *.py[cod]

lint:
	flake8 emoticry tests setup.py
	isort -rc -c emoticry
	isort -rc -c tests
	isort -c setup.py

test:
	coverage run --source='emoticry' ./tests/__main__.py

cover:
	coverage report -m --fail-under=0

tests: clean lint test cover
