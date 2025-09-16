class Temperature:
    """Représente une température et permet des conversions."""
    ZERO_ABSOLU_C = -273.15

    def __init__(self, celsius: float):
        # TODO: Utiliser le setter pour initialiser la valeur
        if celsius<=Temperature.ZERO_ABSOLU_C:
            raise ValueError("La température est en dessous du zéro absolu")
        self._celsius = celsius # Initialisation de celsius

    @property
    def celsius(self) -> float:
        # TODO: Getter pour _celsius
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        # TODO: Setter avec validation
        if value<=Temperature.ZERO_ABSOLU_C:
            raise ValueError("La température ne peut pas être inférieure au zéro absolu.")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        # TODO: Propriété en lecture seule
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self) -> float:
        # TODO: Propriété en lecture seule
        return self._celsius + 273.15

# --- Tests à valider ---
t = Temperature(20)
assert t.celsius == 20
assert t.fahrenheit == 68
assert t.kelvin == 293.15

t.celsius = -10
assert t.celsius == -10
assert t.kelvin == 263.15

# Test de la validation
try:
    t_invalide = Temperature(-300)
except ValueError as e:
    print(f"Exception attrapée avec succès : {e}")

try:
    t.celsius = -400
except ValueError as e:
    print(f"Exception attrapée avec succès : {e}")

print("Tests de l'exercice 3 passés avec succès !")