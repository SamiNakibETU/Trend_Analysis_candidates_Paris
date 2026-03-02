# Contribuer

## Setup développeur

```bash
# Config git
git config user.name "Sami Nakib"
git config user.email "ton-email@example.com"

# Cohen's kappa (validation sentiment)
make kappa-sample    # → outputs/.../kappa_sample_200.csv
# Remplir sentiment_human, puis :
make kappa-calc     # → docs/kappa_results.md

# Tests
make test
```
