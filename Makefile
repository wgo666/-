# Makefile

.PHONY: run clean

run:
	@echo "Running the calculator..."
	@bash bin/run-calculator.sh

clean:
	@echo "Cleaning up temporary files..."
	@rm -rf __pycache__/
	@rm -f *.pyc
	@rm -f tests/__pycache__/