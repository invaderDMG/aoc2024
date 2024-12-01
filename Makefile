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
	$(VENV) && python day$(DAY)/first.py

run_second:
	$(VENV) && python day$(DAY)/second.py

# Integrating one-day changes in main
merge_to_main:
	git checkout main
	git pull origin main
	git merge day$(DAY)
	git push origin main
	git branch -d day$(DAY)
	git push origin --delete day$(DAY)