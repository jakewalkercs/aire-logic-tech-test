run: setup
	./venv/bin/python3 main.py

test-application: setup
	pipenv run pytest

setup: setup.py
	python3 -m venv venv
	. venv/bin/activate
	pip3 install -e .

clean:
	rm -rf __pycache__