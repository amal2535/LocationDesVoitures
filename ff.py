if (cin.isdigit()) and (cin[0]=='1' or cin[0]=='0') and len(cin)==8:
            cp+=1
        else:
            showDialog(self,"CIN Invalide")
        if np(nom):
            cp+=1
        else:
            showDialog(self,"Nom Invalide")
            
        if matricule(mat):
            cp+=1
        else:
            showDialog(self,"Prenom Invalide")
        
        if (duree(duree)):
            cp+=1
        else:
            showDialog(self,"Adresse mail Invalide")
            
        
        
        if (len(adr))>5:
            cp+=1
        else:
            showDialog(self,"Adresse Invalide")
            
        
        if (tel.isdigit()and (len(tel)==8) and ((orange(tel)) or (Telec(tel)) or (ooredoo(tel)) or (ellisa(tel)))):
            cp+=1
        else:
            showDialog(self,"Numero de Telephone Invalide")
        
        if (duree(duree)):
            cp+=1
        else:
            showDialog(self,"Adresse mail Invalide")
        
        if(cp>=1):
                ecrire(cin)
                L=[cin,nom,prenom,age,mail,adr,tel]
                remplir_csv(L)
                showSuccess(self,"Successful")
        else:
                showDialog(self,"Restart")