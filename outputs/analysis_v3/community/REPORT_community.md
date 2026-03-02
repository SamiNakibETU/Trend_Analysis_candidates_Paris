# Analyse 4 : Detection de Communautes et Reseau d'Audience
## Paris Municipales 2026 — Pipeline v3

### Methodologie
- **Graphe bipartite** : 22989 interactions auteur-candidat
- **Similarite Jaccard** : fraction d'audience partagee entre paires de candidats
- **Score chambre d'echo** : % d'audience qui n'engage qu'un seul camp politique
- **Algorithme** : Louvain community detection sur graphe auteur-auteur (multi-candidats)
- **Reseau mentions** : tweets croises entre candidats (N=21 paires)

---

### 1. Chevauchement d'audience (Jaccard)

Top 5 paires les plus proches :
| Paire | Jaccard |
|---|---|
| Belliard x Brossat | 0.0926 |
| Bournazel x Dati | 0.0926 |
| Belliard x Bournazel | 0.0784 |
| Dati x Knafo | 0.0760 |
| Belliard x Gregoire | 0.0633 |

**Interpretation** : Un Jaccard de 0.05 signifie que 5% des utilisateurs ayant commente l'un
ont aussi commente l'autre. Des valeurs > 0.05 indiquent une audience significativement partagee.

---

### 2. Chambres d'echo

| Candidat | Audience totale | % Exclusif | % Meme camp | % Inter-camps | Score echo |
|---|---|---|---|---|---|
| Knafo | 10,602 | 81.8% | 6.3% | 11.9% | **88.1%** |
| Chikirou | 701 | 74.6% | 3.1% | 22.3% | **77.7%** |
| Dati | 4,184 | 61.2% | 15.9% | 22.9% | **77.1%** |
| Gregoire | 551 | 61.2% | 6.4% | 32.5% | **67.5%** |
| Brossat | 1,340 | 60.6% | 1.6% | 37.8% | **62.2%** |
| Bournazel | 2,612 | 58.2% | 0.0% | 41.8% | **58.2%** |
| Mariani | 1,720 | 57.4% | 0.0% | 42.6% | **57.4%** |
| Belliard | 1,279 | 49.7% | 2.7% | 47.5% | **52.5%** |

- **Echo le plus fort** : Knafo (88.1% audience homogene)
- **Audience la plus traversante** : Belliard (47.5% inter-camps)

---

### 3. Reseau de mentions inter-candidats

- **Brossat** mentionne **Gregoire** (27x)
- **Chikirou** mentionne **Gregoire** (21x)
- **Chikirou** mentionne **Dati** (14x)
- **Belliard** mentionne **Gregoire** (13x)
- **Bournazel** mentionne **Gregoire** (11x)
- **Gregoire** mentionne **Brossat** (9x)
- **Gregoire** mentionne **Dati** (6x)
- **Bournazel** mentionne **Dati** (5x)
- **Dati** mentionne **Gregoire** (5x)
- **Gregoire** mentionne **Belliard** (5x)

---

### 4. Detection de communautes

- **8 communautes** detectees (Louvain) sur le reseau d'utilisateurs multi-candidats
- Distribution par candidat dominant : {'sarah_knafo': np.int64(1260), 'rachida_dati': np.int64(655), 'pierre_yves_bournazel': np.int64(355), 'thierry_mariani': np.int64(283), 'david_belliard': np.int64(146)}

---

### Conclusions

1. **Polarisation ideologique** : les audiences de gauche radicale (Chikirou, Brossat) et droite
   (Knafo, Mariani) se chevauchent peu, confirmant la fracture gauche/droite.
2. **Ambassadeurs trans-ideologiques** : Belliard attire une audience
   plus diverse (47.5% inter-camps).
3. **Alliance d'audience** : les paires a fort Jaccard (Belliard/Brossat = 0.093)
   partagent un socle d'audience commun — potentiel de vote utile.
