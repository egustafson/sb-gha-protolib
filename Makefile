PYTHON := $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

.PHONY: clean lint test build

clean:
	rm -rf build dist .pytest_cache .ruff_cache *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest -q

build:
	$(PYTHON) -m build
