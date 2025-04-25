packages = [
    {"package_id": "PKG1", "priority": 2, "weight": 5.2},
    {"package_id": "PKG2", "priority": 1, "weight": 7.5},
    {"package_id": "PKG3", "priority": 2, "weight": 4.0},
    {"package_id": "PKG4", "priority": 1, "weight": 2.3},
    {"package_id": "PKG5", "priority": 3, "weight": 5.2}
]

#bubble sort technique
n = len(packages)
for i in range(n):
    for j in range(0, n - i - 1):
        p1 = packages[j]
        p2 = packages[j + 1]
        if (p1['priority'], p1['weight']) > (p2['priority'], p2['weight']):
            packages[j], packages[j + 1] = packages[j + 1], packages[j]

print("Sorted Conveyor Belt:")
for pkg in packages:
    print(pkg)
