
help:
	@echo "Please use \'make <target>\' where <target> is one of"
	@echo "  run		to run main python file"
	@echo "  install	to install required python modules"


run:
	@echo "Running..."
	python ./simulation/main.py

install:
	pip install -r requirements.txt