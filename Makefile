PIP="venv/bin/pip"
PYTHON="venv/bin/python"
BLACK="venv/bin/black"

REQUIREMENTS:=requirements.txt

virtualenv:
	test -d venv || virtualenv -p python3.7 venv
	$(PIP) install -U "pip"
	$(PIP) install -r $(REQUIREMENTS)

black-check: virtualenv
	$(BLACK) wallapopy/src wallapopy/tests --check

black: virtualenv
	$(BLACK) wallapopy/src wallapopy/tests

test: virtualenv black-check
	$(PYTHON) -m pytest wallapopy/tests
