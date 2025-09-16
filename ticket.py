class Ticket:
    """Un ticket avec un identifiant unique auto-incrémenté."""
    
    # TODO: Créer un attribut de classe pour le compteur
    compteur = 0 # Attribut de classe pour compter les tickets
    
    def __init__(self):
        # TODO: Assigner l'ID à l'instance et incrémenter le compteur
        self.id = Ticket.compteur  # Assigner l'ID actuel au ticket
        Ticket.compteur += 1       # Incrémenter le compteur pour le prochain ticket
        pass

    def __repr__(self) -> str:
        # TODO: Retourner la représentation du ticket
        return f"Ticket(id={self.id})" # Retourne une représentation du ticket

# --- Tests à valider ---
ticket1 = Ticket()
ticket2 = Ticket()
ticket3 = Ticket()

print(ticket1)
print(ticket2)
print(ticket3)

assert ticket1.id == 0
assert ticket2.id == 1
assert ticket3.id == 2
assert Ticket.compteur == 3, "Le compteur de classe devrait être à 3"

print("Tests de l'exercice 2 passés avec succès !")