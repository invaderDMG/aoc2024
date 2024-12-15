# Makefile

# Activate virtual environment
VENV = source venv/bin/activate

# Create the folder for a new day and an associated branch
create_day:
	git checkout main
	git pull origin main
	git checkout -b day$(DAY)
	mkdir -p day$(DAY) && touch day$(DAY)/first.py && touch day$(DAY)/second.py && touch day$(DAY)/input.txt
	echo "# Day $(DAY) - First puzzle" > day$(DAY)/first.py
	echo "# Day $(DAY) - Second puzzle" > day$(DAY)/second.py
	git add day$(DAY)
	git commit -m "Initialize Day $(DAY)"
	git push origin day$(DAY)

# Execute the script for a specific day
run_first:
	export PYTHONPATH=$(pwd)
	$(VENV) && python day$(DAY)/first.py

run_second:
	export PYTHONPATH=$(pwd)
	$(VENV) && python day$(DAY)/second.py

debug_first:
	$(VENV) && code --wait --file-uri $(pwd)/day$(DAY)/first.py

debug_second:
	$(VENV) && code --wait --file-uri $(pwd)/day$(DAY)/second.py