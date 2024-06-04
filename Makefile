run:
	@python3 -m uvicorn tibiapi.main:app --reload

start-env:
	source .venv/bin/activate

stop-env:
	source .venv/bin/deactivate
