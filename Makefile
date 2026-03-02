# Paris Municipales 2026 — Pipeline
# Usage: make install | data | run | test | kappa

.PHONY: install data run test kappa-sample kappa-calc export clean

install:
	pip install -r requirements.txt

# Vérifier que les données sont en place
data:
	@test -f final/data/replies_classified.csv || (echo "Placer replies_classified.csv dans final/data/" && exit 1)
	@test -f final/data/tweets_twitter.csv || (echo "Placer tweets_twitter.csv dans final/data/" && exit 1)
	@echo "Données OK"

# Exporter les résultats chiffrés (nécessite d'avoir exécuté les notebooks)
export:
	python scripts/export_resultats_chiffres.py

# Cohen's kappa : préparer échantillon puis calculer (après annotation manuelle)
kappa-sample:
	python scripts/prepare_kappa_sample.py

kappa-calc:
	python scripts/compute_cohens_kappa.py

# Tests unitaires
test:
	python -m pytest tests/ -v

# Aide
help:
	@echo "Targets: install, data, export, kappa-sample, kappa-calc, test"
	@echo "  make install      — pip install -r requirements.txt"
	@echo "  make data         — vérifier présence des CSV dans final/data/"
	@echo "  make export       — régénérer docs/RESULTATS_CHIFFRES.md"
	@echo "  make kappa-sample — préparer 200 replies pour annotation"
	@echo "  make kappa-calc   — calculer Cohen's kappa (après annotation)"
	@echo "  make test         — lancer les tests unitaires"
