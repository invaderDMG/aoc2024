# Makefile

# Activar entorno virtual
VENV = source venv/bin/activate

# Crear la carpeta para un nuevo día y una rama asociada
create_day:
	git checkout main
	git pull origin main
	git checkout -b day$(DAY)
	mkdir -p day$(DAY) && touch day$(DAY)/main.py && touch day$(DAY)/input.txt
	echo "# Day $(DAY)" > day$(DAY)/main.py
	git add day$(DAY)
	git commit -m "Initialize Day $(DAY)"
	git push origin day$(DAY)

# Ejecutar el script de un día específico
run:
	$(VENV) && python day$(DAY)/main.py

# Integrar los cambios de un día en main
merge_to_main:
	git checkout main
	git pull origin main
	git merge day$(DAY)
	git push origin main
	git branch -d day$(DAY)
	git push origin --delete day$(DAY)