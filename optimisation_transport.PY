from pulp import *

# -----------------------------------
# Lecture des données
# -----------------------------------

# Nombre d'usines
n_usines = int(input("Nombre d'usines : "))

# Nombre d'entrepôts
n_entrepots = int(input("Nombre d'entrepôts : "))

# Création des listes
usines = [f"U{i+1}" for i in range(n_usines)]
entrepots = [f"E{j+1}" for j in range(n_entrepots)]

# -----------------------------------
# Capacités des usines
# -----------------------------------

capacites = {}

print("\n--- Capacités des usines ---")
for u in usines:
    capacites[u] = float(input(f"Capacité de {u} : "))

# -----------------------------------
# Demandes des entrepôts
# -----------------------------------

demandes = {}

print("\n--- Demandes des entrepôts ---")
for e in entrepots:
    demandes[e] = float(input(f"Demande de {e} : "))

# -----------------------------------
# Coûts de transport
# -----------------------------------

couts = {}

print("\n--- Coûts de transport ---")

for u in usines:
    for e in entrepots:
        cout = float(input(f"Coût {u} -> {e} : "))
        couts[(u, e)] = cout

# -----------------------------------
# Création du problème
# -----------------------------------

prob = LpProblem("Transport_Problem", LpMinimize)

# -----------------------------------
# Variables de décision
# -----------------------------------

x = LpVariable.dicts(
    "x",
    [(u, e) for u in usines for e in entrepots],
    lowBound=0,
    cat='Continuous'
)

# -----------------------------------
# Fonction objectif
# -----------------------------------

prob += lpSum(
    couts[(u, e)] * x[(u, e)]
    for u in usines
    for e in entrepots
)

# -----------------------------------
# Contraintes des usines
# -----------------------------------

for u in usines:
    prob += (
        lpSum(x[(u, e)] for e in entrepots)
        <= capacites[u]
    )

# -----------------------------------
# Contraintes des entrepôts
# -----------------------------------

for e in entrepots:
    prob += (
        lpSum(x[(u, e)] for u in usines)
        == demandes[e]
    )

# -----------------------------------
# Résolution
# -----------------------------------

prob.solve()

# -----------------------------------
# Affichage des résultats
# -----------------------------------

print("\n============================")
print("RÉSULTATS")
print("============================\n")

print("Status :", LpStatus[prob.status])

print("\nQuantités transportées :\n")

for u in usines:
    for e in entrepots:
        print(
            f"{u} -> {e} = {x[(u, e)].varValue}"
        )

print("\nCoût total minimal =",
      value(prob.objective))                                                                                                                                                                                                                                                                                                                                                                                                                                                                  