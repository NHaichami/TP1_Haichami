class CompteurPage:
    #Attribut de classe
    total_visites = 0

    #Constructeur
    def __init__(self, nom_page):
        self.nom_page = nom_page
        self.visites = 0
        CompteurPage.total_visites += 1

    def ajouter_visite(self):
        self.visites += 1
        CompteurPage.total_visites += 1

    def afficher_statistiques(self):
        return f"Page '{self.nom_page}': {self.visites} visites. Total global: {CompteurPage.total_visites}"


page1 = CompteurPage("Accueil")
page2 = CompteurPage("Contact")

page1.ajouter_visite()
page1.ajouter_visite()
page2.ajouter_visite()

print(page1.afficher_statistiques()) #Page 'Accueil': 2 visites. Total global: 5
print(page2.afficher_statistiques()) #Page 'Contact': 1 visites. Total global: 5
print(CompteurPage.total_visites) #Total global: 5