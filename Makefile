run:
	@python3 -m uvicorn tibiapi.main:app --reload

requirements-dev:
	@python3 -m pip install -r requirements/dev.txt
