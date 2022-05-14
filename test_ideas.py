from statistics import mean

G={'E': 18.0, 'D': 17.0, 'C': 19.0, 'B': 15.0, 'A': 0}

a = mean(G[k] for k in G)

print(a)
