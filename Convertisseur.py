class Convertisseur:
    # Attribut de classe : taux de change EUR vers DH
    taux_eur_dh = 10.9

    @staticmethod
    def vers_dh(euros: float) -> float:
        return euros * Convertisseur.taux_eur_dh

    @classmethod
    def changer_taux(cls, nouveau_taux: float):
        if nouveau_taux <= 0:
            raise ValueError("Le taux doit être positif.")
        cls.taux_eur_dh = nouveau_taux

    @classmethod
    def depuis_dh(cls, dirhams: float) -> float:
        return dirhams / cls.taux_eur_dh


# Appel sans instance
print(Convertisseur.vers_dh(100)) # 1090.0

# Modification du taux via méthode de classe
Convertisseur.changer_taux(11.0)
print(Convertisseur.depuis_dh(110)) # 10.0

# Création d'une instance
conv = Convertisseur()
print(conv.vers_dh(50)) # 550.0
