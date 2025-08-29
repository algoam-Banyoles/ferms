.PHONY: install lint test run

install:
pip install -r requirements.txt

lint:
black --check .
ruff check .
mypy src/core

test:
pytest -q

run:
python -m src.app
