
help:
	@echo "Please use \'make <target>\' where <target> is one of"
	@echo "  run		to run main python file"
	@echo "  generate	to generate results"
	@echo "  install	to install required python modules"


run:
	@echo "Running..."
	python ./simulation/main.py

generate:
	@echo "Generate results..."
	python ./simulation/generate_results.py

install:
	@echo "Installing..."
	pip install -r requirements.txt