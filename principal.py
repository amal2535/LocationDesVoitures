from PyQt5 import QtCore, QtGui, QtWidgets
from accueil import Ui_MainWindow
from gestvoitures import Ui_Dialog as gestvoituresDialog
from gestclients import Ui_Dialog as gestclientsDialog
from gestlocation import Ui_Dialog as gestlocationDialog
from ajout_voiture import Ui_Form as ajout_voitureForm
from gestsuppvoiture import Ui_Form as gestsuppvoitureForm
from gestmodifvoiture import Ui_Form as gestmodifvoitureForm
from recherchevoitures import Ui_Form as recherchevoituresForm
from suppv import Ui_Dialog as suppvDialog
from suppvmarque import Ui_Dialog as suppvmarqueDialog
from suppvage import Ui_Dialog as suppvageDialog
from modifierprixv import Ui_Dialog as modifierprixvDialog
from modifiercouleurv import Ui_Dialog as modifiercouleurvDialog
from rech_voiture_mat import Ui_Form as rech_voiture_matForm
from rech_voiture_marque import Ui_Form as rech_voiture_marqueForm
from rech_voiture_couleur import Ui_Form as rech_voiture_couleurForm
from rech_voiture_louees_2_dates import Ui_Form as rech_voiture_louees_2_datesForm
from rech_voiture_louees import Ui_Form as rech_voiture_loueesForm
from rech_voiture_diponibles import Ui_Form as rech_voiture_diponiblesForm

from ajout_client import Ui_Form as ajout_clientForm
from suppc import Ui_Dialog as suppcDialog
from gestmodifclients import Ui_Form as gestmodifclientsForm
from rech_client_cin import Ui_Form as rech_client_cinForm
from modifieradrclient import Ui_Dialog as modifieradrclientDialog
from modifiermailclient import Ui_Dialog as modifiermailclientDialog
from modifiernumclient import Ui_Dialog as modifiernumclientDialog
from rechercheclients import Ui_Form as rechercheclientsForm

from ajout_location import Ui_Form as ajout_locationForm
from suppl import Ui_Dialog as supplDialog
from gestmodiflocations import Ui_Form as gestmodiflocationsForm
from modifierdatelocation import Ui_Dialog as modifierdatelocationDialog
from modifierdureelocation import Ui_Dialog as modifierdureelocationDialog
from recherchelocations import Ui_Form as recherchelocationsForm
from rech_location_cin import Ui_Form as rech_location_cinForm
from rech_location_mat import Ui_Form as rech_location_matForm
from rech_location_date import Ui_Form as rech_location_dateForm
from rech_location_duree import Ui_Form as rech_location_dureeForm
from rech_location_2dates import Ui_Form as rech_location_2datesForm
from contrat import Ui_Form as contratForm
from facture import Ui_Form as factureForm
from apropos import Ui_Dialog as aproposDialog


import sys


#slots

def afficheGestv():
    gestvoitures.show()
def afficheGestc():
    gestclients.show()
def afficheGestl():
    gestlocation.show()
def afficheav():
    ajout_voiture.show()
def afficheac():
    ajout_client.show()
def afficheal():
    ajout_location.show()  
def affichesv():
    gestsuppvoiture.show()
def affichemv():
    gestmodifvoiture.show()
def afficherv():
    recherchevoitures.show()
def affichesvdonnee():
    suppv.show()
def affichesvmarque():
    suppvmarque.show()
def affichesvage():
    suppvage.show()
def affichemodifprix():
    modifierprixv.show()
def affichemodifclr():
    modifiercouleurv.show()    
#rechercher voiture
def affichervmat():
    rech_voiture_mat.show()
def affichervclr():
    rech_voiture_couleur.show()
def affichervmar():
    rech_voiture_marque.show()
def afficherv2d():
    rech_voiture_louees_2_dates.show()
def affichevlouee():
    rech_voiture_louees.show()
def affichevdispo():
    rech_voiture_diponibles.show()   
def affichesc():
    suppc.show()     
def affichemc():
    gestmodifclients.show()
def affichemadrc():
    modifieradrclient.show()
def affichemmailc():
    modifiermailclient.show()
def affichemnumc():
    modifiernumclient.show()
def afficherrcinc():
    rech_client_cin.show()   
def afficherc():
    rech_client_cin.show()
    
def affichesl():
    suppl.show()
def afficheml():
    gestmodiflocations.show()    
def affichemdate():
    modifierdatelocation.show()    
def affichemduree():
    modifierdureelocation.show()
def afficherl():
    recherchelocations.show()
def afficherrcinl():
    rech_location_cin.show() 
def afficherrmatl():
    rech_location_mat.show()
def afficherrdatel():
    rech_location_date.show()
def afficherrdureel():
    rech_location_duree.show()
def afficherloc2dates():
    rech_location_2dates.show()

def affichercontrat():
    contrat.show()
def afficherfacture():
    facture.show()
def afficherapropos():
    apropos.show()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#PARTIE GESTION DES VOITURES

#Création de la boite de dialogue gestvoitures
gestvoitures= QtWidgets.QDialog()
uigestvoitures = gestvoituresDialog()
uigestvoitures.setupUi(gestvoitures)
#Création de la boite de dialogue gestclients
gestclients= QtWidgets.QDialog()
uigestclients = gestclientsDialog()
uigestclients.setupUi(gestclients)
#Création de la boite de dialogue gestlocation
gestlocation= QtWidgets.QDialog()
uigestlocation = gestlocationDialog()
uigestlocation.setupUi(gestlocation)

#creation de form ajout_voiture
ajout_voiture= QtWidgets.QWidget()
uiajout_voiture = ajout_voitureForm()
uiajout_voiture.setupUi(ajout_voiture)

#creation de form gestsuppvoiture
gestsuppvoiture= QtWidgets.QWidget()
uigestsuppvoiture = gestsuppvoitureForm()
uigestsuppvoiture.setupUi(gestsuppvoiture)
#creation de form gestmodifvoiture
gestmodifvoiture= QtWidgets.QWidget()
uigestmodifvoiture = gestmodifvoitureForm()
uigestmodifvoiture.setupUi(gestmodifvoiture)
#creation de form recherchevoitures
recherchevoitures= QtWidgets.QWidget()
uirecherchevoitures = recherchevoituresForm()
uirecherchevoitures.setupUi(recherchevoitures)
#Création de la boite de dialogue suppv
suppv= QtWidgets.QDialog()
uisuppv = suppvDialog()
uisuppv.setupUi(suppv)
#Création de la boite de dialogue suppvmarque
suppvmarque= QtWidgets.QDialog()
uisuppvmarque = suppvmarqueDialog()
uisuppvmarque.setupUi(suppvmarque)
#Création de la boite de dialogue suppvage
suppvage= QtWidgets.QDialog()
uisuppvage = suppvageDialog()
uisuppvage.setupUi(suppvage)
#Création de la boite de dialogue modifierprixv
modifierprixv= QtWidgets.QDialog()
uimodifierprixv = modifierprixvDialog()
uimodifierprixv.setupUi(modifierprixv)
#Création de la boite de dialogue modifiercouleurv
modifiercouleurv= QtWidgets.QDialog()
uimodifiercouleurv = modifiercouleurvDialog()
uimodifiercouleurv.setupUi(modifiercouleurv)
#creation de form rech_voiture_mat
rech_voiture_mat= QtWidgets.QWidget()
uirech_voiture_mat = rech_voiture_matForm()
uirech_voiture_mat.setupUi(rech_voiture_mat)
#creation de form rech_voiture_marque
rech_voiture_marque= QtWidgets.QWidget()
uirech_voiture_marque = rech_voiture_marqueForm()
uirech_voiture_marque.setupUi(rech_voiture_marque)
#creation de form rech_voiture_couleur
rech_voiture_couleur= QtWidgets.QWidget()
uirech_voiture_couleur = rech_voiture_couleurForm()
uirech_voiture_couleur.setupUi(rech_voiture_couleur)
#creation de form rech_voiture_louees_2_dates
rech_voiture_louees_2_dates= QtWidgets.QWidget()
uirech_voiture_louees_2_dates = rech_voiture_louees_2_datesForm()
uirech_voiture_louees_2_dates.setupUi(rech_voiture_louees_2_dates)
#creation de form rech_voiture_louees
rech_voiture_louees= QtWidgets.QWidget()
uirech_voiture_louees = rech_voiture_loueesForm()
uirech_voiture_louees.setupUi(rech_voiture_louees)
#creation de form rech_voiture_diponibles
rech_voiture_diponibles= QtWidgets.QWidget()
uirech_voiture_diponibles= rech_voiture_diponiblesForm()
uirech_voiture_diponibles.setupUi(rech_voiture_diponibles)



#PARTIE GESTIONS DES CLIENTS:

#creation de form ajout_client
ajout_client= QtWidgets.QWidget()
uiajout_client = ajout_clientForm()
uiajout_client.setupUi(ajout_client)
#Création de la boite de dialogue suppc
suppc= QtWidgets.QDialog()
uisuppc = suppcDialog()
uisuppc.setupUi(suppc)
#creation de form gestmodifclients
gestmodifclients= QtWidgets.QWidget()
uigestmodifclients = gestmodifclientsForm()
uigestmodifclients.setupUi(gestmodifclients)
#creation de dialog modifieradrclient
modifieradrclient= QtWidgets.QDialog()
uimodifieradrclient = modifieradrclientDialog()
uimodifieradrclient.setupUi(modifieradrclient)
#creation de dialog modifiermailclient
modifiermailclient= QtWidgets.QDialog()
uimodifiermailclient = modifiermailclientDialog()
uimodifiermailclient.setupUi(modifiermailclient)
#creation de dialog modifiernumclient
modifiernumclient= QtWidgets.QDialog()
uimodifiernumclient = modifiernumclientDialog()
uimodifiernumclient.setupUi(modifiernumclient)
#creation de form rechercheclients
rechercheclients= QtWidgets.QWidget()
uirechercheclients= rechercheclientsForm()
uirechercheclients.setupUi(rechercheclients)
#creation de form rech_client_cin
rech_client_cin= QtWidgets.QWidget()
uirech_client_cin = rech_client_cinForm()
uirech_client_cin.setupUi(rech_client_cin)


#PARTIE GESTION DES LOCATIONS:

#creation de form ajout_location
ajout_location= QtWidgets.QWidget()
uiajout_location = ajout_locationForm()
uiajout_location.setupUi(ajout_location)
#creation de form suppl
suppl= QtWidgets.QDialog()
uisuppl = supplDialog()
uisuppl.setupUi(suppl)
#creation de form gestmodiflocations
gestmodiflocations= QtWidgets.QWidget()
uigestmodiflocations= gestmodiflocationsForm()
uigestmodiflocations.setupUi(gestmodiflocations)
#creation de dialog modifierdatelocation
modifierdatelocation= QtWidgets.QDialog()
uimodifierdatelocation = modifierdatelocationDialog()
uimodifierdatelocation.setupUi(modifierdatelocation)
#creation de dialog modifierdureelocation
modifierdureelocation= QtWidgets.QDialog()
uimodifierdureelocation = modifierdureelocationDialog()
uimodifierdureelocation.setupUi(modifierdureelocation)
#creation de form recherchelocations
recherchelocations= QtWidgets.QWidget()
uirecherchelocations = recherchelocationsForm()
uirecherchelocations.setupUi(recherchelocations)
#creation de form rech_location_mat
rech_location_mat= QtWidgets.QWidget()
uirech_location_mat = rech_location_matForm()
uirech_location_mat.setupUi(rech_location_mat)
#creation de form rech_location_cin
rech_location_cin= QtWidgets.QWidget()
uirech_location_cin = rech_location_cinForm()
uirech_location_cin.setupUi(rech_location_cin)
#creation de form rech_location_date
rech_location_date= QtWidgets.QWidget()
uirech_location_date = rech_location_dateForm()
uirech_location_date.setupUi(rech_location_date)
#creation de form rech_location_duree
rech_location_duree= QtWidgets.QWidget()
uirech_location_duree = rech_location_dureeForm()
uirech_location_duree.setupUi(rech_location_duree)
#creation de form rech_location_2dates
rech_location_2dates= QtWidgets.QWidget()
uirech_location_2dates = rech_location_2datesForm()
uirech_location_2dates.setupUi(rech_location_2dates)


#CONTRAT
#creation de form contrat
contrat= QtWidgets.QWidget()
uicontrat= contratForm()
uicontrat.setupUi(contrat)
#FACTURE
#creation de form facture
facture= QtWidgets.QWidget()
uifacture= factureForm()
uifacture.setupUi(facture)
#APROPOS
#creation de dialog apropos
apropos= QtWidgets.QDialog()
uiapropos = aproposDialog()
uiapropos.setupUi(apropos)











MainWindow.show()

#Les signaux
ui.pushButton.clicked.connect(afficheGestv)
ui.pushButton_3.clicked.connect(afficheGestc)
ui.pushButton_2.clicked.connect(afficheGestl)
ui.pushButton_4.clicked.connect(affichercontrat)
ui.pushButton_5.clicked.connect(afficherfacture)
ui.commandLinkButton_3.clicked.connect(afficherapropos)



uigestvoitures.pushButton_4.clicked.connect(afficheav)
uigestvoitures.pushButton_7.clicked.connect(affichesv)
uigestvoitures.pushButton_6.clicked.connect(affichemv)
uigestvoitures.pushButton_5.clicked.connect(afficherv)
#suppression v
uigestsuppvoiture.pushButton.clicked.connect(affichesvdonnee)
uigestsuppvoiture.pushButton_3.clicked.connect(affichesvmarque)
uigestsuppvoiture.pushButton_2.clicked.connect(affichesvage)
#modification v
uigestmodifvoiture.pushButton_4.clicked.connect(affichemodifprix)
uigestmodifvoiture.pushButton_3.clicked.connect(affichemodifclr)
#recherche v
uirecherchevoitures.pushButton_6.clicked.connect(affichervmat)
uirecherchevoitures.pushButton_4.clicked.connect(affichervclr)
uirecherchevoitures.pushButton_5.clicked.connect(affichervmar)
uirecherchevoitures.pushButton.clicked.connect(afficherv2d)
uirecherchevoitures.pushButton_3.clicked.connect(affichevlouee)
uirecherchevoitures.pushButton_2.clicked.connect(affichevdispo)
#client
uigestclients.pushButton_4.clicked.connect(afficheac)
uigestclients.pushButton_6.clicked.connect(affichesc)
uigestclients.pushButton_5.clicked.connect(affichemc)
uigestclients.pushButton_7.clicked.connect(afficherc)
#modif clients
uigestmodifclients.pushButton.clicked.connect(affichemadrc)
uigestmodifclients.pushButton_2.clicked.connect(affichemmailc)
uigestmodifclients.pushButton_3.clicked.connect(affichemnumc)
#☻recherche clients
uirechercheclients.pushButton_2.clicked.connect(afficherrcinc)
#LOCATION:
#ajout_loc/supp/modif
uigestlocation.pushButton_2.clicked.connect(afficheal)
uigestlocation.pushButton_6.clicked.connect(affichesl)
uigestlocation.pushButton_5.clicked.connect(afficheml)
uigestlocation.pushButton_7.clicked.connect(afficherl)
#modif location
uigestmodiflocations.pushButton.clicked.connect(affichemdate)
uigestmodiflocations.pushButton_2.clicked.connect(affichemduree)
#recherche loc
uirecherchelocations.pushButton_2.clicked.connect(afficherrmatl)
uirecherchelocations.pushButton_3.clicked.connect(afficherrcinl)
uirecherchelocations.pushButton_4.clicked.connect(afficherrdatel)
uirecherchelocations.pushButton_5.clicked.connect(afficherrdureel)
uirecherchelocations.pushButton_6.clicked.connect(afficherloc2dates)


sys.exit(app.exec_())
