from pulp import *

# -----------------------------------
# Lecture des données
# -----------------------------------

# Nombre de travailleurs/tâches
n = int(input(
    "Nombre de travailleurs/tâches : "
))

# Création des listes
workers = [
    f"W{i+1}" for i in range(n)
]

tasks = [
    f"T{j+1}" for j in range(n)
]

# -----------------------------------
# Matrice des coûts
# -----------------------------------

costs = {}

print("\n--- Coûts ---")

for w in workers:
    for t in tasks:

        c = float(input(
            f"Coût {w} -> {t} : "
        ))

        costs[(w, t)] = c

# -----------------------------------
# Création du problème
# -----------------------------------

prob = LpProblem(
    "Assignment_Problem",
    LpMinimize
)

# -----------------------------------
# Variables de décision
# -----------------------------------

x = LpVariable.dicts(
    "x",
    [(w, t)
     for w in workers
     for t in tasks],
    cat='Binary'
)

# -----------------------------------
# Fonction objectif
# -----------------------------------

prob += lpSum(
    costs[(w, t)] * x[(w, t)]
    for w in workers
    for t in tasks
)

# -----------------------------------
# Contraintes travailleurs
# -----------------------------------

for w in workers:

    prob += (
        lpSum(
            x[(w, t)]
            for t in tasks
        ) == 1
    )

# -----------------------------------
# Contraintes tâches
# -----------------------------------

for t in tasks:

    prob += (
        lpSum(
            x[(w, t)]
            for w in workers
        ) == 1
    )

# -----------------------------------
# Résolution
# -----------------------------------

prob.solve()

# -----------------------------------
# Résultats
# -----------------------------------

print("\n===================")
print("RÉSULTATS")
print("===================\n")

print("Status :",
      LpStatus[prob.status])

print("\nAffectations optimales :\n")

for w in workers:
    for t in tasks:

        if x[(w, t)].varValue == 1:

            print(
                f"{w} -> {t}"
            )

print(
    "\nCoût total minimal =",
    value(prob.objective)
)