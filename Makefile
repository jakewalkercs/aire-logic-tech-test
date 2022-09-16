run: setup
	./venv/bin/python3 src/main.py

test-application: setup
	pipenv run pytest

setup: setup.py
	pipenv install
	python3 -m venv venv
	. venv/bin/activate
	pip3 install -e .

clean:
	rm -rf __pycache__