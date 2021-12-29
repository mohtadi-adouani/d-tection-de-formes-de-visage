import cv2
from tkinter import *
from tkinter.filedialog import *

#variables globales
lien_photo = ""
nombre_Visages = 0



## Fonction qui va detecter les visages
## et afficher les carres sur les visages
def reconaissance_visage(image):
    global nombre_Visages
    global lien_photo
    lien_photo = image
    
    #importation de photo
    img = cv2.imread(image)
    
    #Importation des modeles
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

    #changement de la couleur de la photo en gris pour un meilleur traitement 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    #detection des visages
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #mise a jour du nombre de visages
    nombre_Visages = len(faces)
    print("Nombre de visaeg detecte",len(faces))
    
    
    #traceage des rectangles sur 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    #affichage et attente pour quitter 
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


##Importe une image et 
## affiche les logs
def importer_image(fenetre):
    filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.jpg'),('all files','.*')])
    reconaissance_visage(filepath)
    label = Label(fenetre, text="Pour la photo "+lien_photo+" || Nombre de visages : "+str(nombre_Visages))
    label.pack()
    



#fenetre
fenetre = Tk()
fenetre.geometry("600x600")
fenetre.title('Reconaissance de visages')
fenetre.configure(background='grey')


#bouton qui va faire appel a la fonction
b1 = Button(fenetre, text ="Importer une image",command=lambda : importer_image(fenetre)).pack()

fenetre.mainloop()

