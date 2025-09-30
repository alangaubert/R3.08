class Heure:
    """Représente une heure de la journée (h, m, s)."""
    
    def __init__(self, h: int, m: int, s: int):
        # TODO: Initialiser et valider les attributs
        if not (0 <= h < 24):
            raise ValueError("Heure doit être entre 0 et 23")
        if not (0 <= m < 60):
            raise ValueError("Minute doit être entre 0 et 59")
        if not (0 <= s < 60):
            raise ValueError("Seconde doit être entre 0 et 59")
        self.h = h  # Initialisation de l'heure
        self.m = m  # Initialisation des minutes
        self.s = s  # Initialisation des secondes

    @classmethod
    def from_secondes(cls, total_secondes: int) -> "Heure":
        # TODO: Calculer h, m, s et retourner une nouvelle instance `cls(...)`
        total_secondes = total_secondes % 86400  # Nombre de secondes dans une journée
        h = total_secondes // 3600
        m = (total_secondes % 3600) // 60
        s = total_secondes % 60
        return cls(h, m, s)
    
    def __repr__(self) -> str:
        # TODO Implémentez `__repr__` pour un affichage clair (ex: `Heure(14, 30, 05)`).
        return f"Heure({self.h}, {self.m}, {self.s})"

    def __str__(self) -> str:
        # TODO 4. Implémentez `__str__` pour un affichage plus lisible (ex: `14:30:05`).
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Heure):
            return NotImplemented
        # TODO: Comparer self et other Implémentez `__eq__(self, other)` pour comparer deux instances de `Heure`. Elles sont égales si leurs heures, minutes et secondes sont identiques.
        if self.h == other.h and self.m == other.m and self.s == other.s:
            return True
        return False

# --- Tests à valider ---
h1 = Heure(1, 1, 1)
print(f"repr(h1): {repr(h1)}")
print(f"str(h1): {str(h1)}")

# Test du classmethod
total_secs = 3661 # 1 heure, 1 minute, 1 seconde
h2 = Heure.from_secondes(total_secs)
assert h2.h == 1 and h2.m == 1 and h2.s == 1

# Test de l'égalité
h3 = Heure(1, 1, 1)
assert h1 == h2
assert h1 == h3
assert h2 != Heure(1, 1, 2)

print("Tests de l'exercice 4 passés avec succès !")