WORKDIR = scripts
MAIN = $(WORKDIR)/main.py
current_dir = $(shell pwd)

ifeq ($(OS),Windows_NT)
    PYTHON = python
	PIP = pip
else
    PYTHON = python3
	PIP = pip3
endif

# starting

default:
	make run

run:
	@PYTHONPATH=$(current_dir) $(PYTHON) $(MAIN)

# requirements

pip:
	@$(PYTHON) -m pip install --upgrade pip

req:
	@$(PIP) install -r requirements.txt

style-req:
	@$(PIP) install -r requirements-style.txt

all-req:
	@make req
	@make style-req
# styling

style:
	isort $(WORKDIR)
	black -S -l 79 $(WORKDIR)
	flake8 $(WORKDIR)
	mypy $(WORKDIR)
