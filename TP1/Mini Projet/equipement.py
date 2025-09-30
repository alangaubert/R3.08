class EquipementReseau:
    compteur_id = 0
    def __init__(self, hostname: str, ip_address: str):
        self.hostname = hostname
        self.ip_address = ip_address
        self.id = EquipementReseau.compteur_id
        EquipementReseau.compteur_id += 1
        self.statut = 'inactif'

    def __repr__(self):
        return f"Equipement(id={self.id}, hostname='{self.hostname}', ip='{self.ip_address}', statut='{self.statut}')"

    def activer(self):
        self.statut = "actif"

    def desactiver(self):
        self.statut = "inactif"

    @property
    def est_actif(self):
       return self.statut == 'actif'  #Pas bon à refaire