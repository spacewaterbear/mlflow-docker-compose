VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
REQ_FILE := mlflow/requirements.txt
SCRIPT := update_user_admin.py

all: $(VENV_DIR)/bin/activate install run

$(VENV_DIR)/bin/activate:
	python3 -m venv $(VENV_DIR)

install: $(VENV_DIR)/bin/activate
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQ_FILE)

run:
	$(PYTHON) $(SCRIPT)

clean:
	rm -rf $(VENV_DIR)
