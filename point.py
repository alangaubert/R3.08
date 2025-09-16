import math

class Point2D:
    """Représente un point dans un plan 2D."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x  
        self.y = y  # Initialiser les coordonnées
        pass

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})" # Retourne une représentation du point
    

    def deplacer(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy     # Ajout de x et y à dx et dy
        pass

    def distance(self, autre_point: "Point2D") -> float:
        return math.sqrt((autre_point.x - self.x) ** 2 + (autre_point.y - self.y) ** 2) # Calculer la distance entre deux points

# --- Tests à valider ---
p1 = Point2D(1, 2)
p2 = Point2D(4, 6)

print(f"Point 1 : {p1}")
print(f"Point 2 : {p2}")

# Test de la distance
dist = p1.distance(p2)
print(f"Distance entre p1 et p2 : {dist}")
assert math.isclose(dist, 5.0), "La distance devrait être 5.0"

# Test du déplacement
p1.deplacer(1, -1)
print(f"Point 1 après déplacement : {p1}")
assert p1.x == 2 and p1.y == 1, "Le point devrait être à (2, 1)"

print("Tests de l'exercice 1 passés avec succès !")