init:
	pip install -r requirements.txt

bundle:
	zip kapacitor-teams-handler.zip \
		README.md \
		main.py \
		requirements.txt \
		src/core.py \
		configuration/configuration.py \
		tests/* \
