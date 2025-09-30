from equipement import EquipementReseau

class GestionnaireParc:
    def __init__(self, nom_parc: str):
        self.nom_parc = nom_parc
        self.equipements = []

    def ajouter_equipement(self, equipement: EquipementReseau):
        if not isinstance(equipement, EquipementReseau):
            print(f"Erreur: Ajout d'un objet qui n'est pas un EquipementReseau.")
            return
        self.equipements.append(equipement)
    
    def lister_equipements(self):
        if self.equipements == []:
            print("equipements est vide")
        else:
            print(f"equipements du parc {self.nom_parc}:")
            for i in self.equipements:
                print(f" - {i}")

    def rechercher_par_hostname(self, hostname: str):
        for eq in self.equipements:
            if eq.hostname == hostname:
                return eq
        return None

    def statistiques(self):
        total = len(self.equipements)
        actifs = sum(1 for eq in self.equipements if eq.est_actif)
        inactifs = total - actifs
        print(f"Total: {total}, Actifs: {actifs}, Inactifs: {inactifs}")