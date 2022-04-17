from ClaseEmail import email
import csv

if __name__ =="__main__":
   print ("Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta, dominio y tipo de dominio\n")
   a=input("nombre\n")
   b=input("dominio\n")
   c=input("tipodominio\n")
   d=input("contraseña\n")
   usuario1=email(a,b,c,d)
   print ("Estimado {} te enviaremos tus mensajes a la dirección {}.\n".format(usuario1.getidc(), usuario1.retornaemail()))
   usuario1.cambircontrasena()
   usuario2=email()
   a=input("correo\n")
   usuario2.crearcuenta(a)
   archivo=open("emails.csv")
   reader=csv.reader(archivo, delimiter=",")
   listausuarios=[]
   for mail in reader:
        usuario=email()
        usuario.crearcuenta(mail[0])
        listausuarios.append(usuario)
   identificador=input("Ingrese identificador \n")
   k=0
   contador=0
   while (k<len(listausuarios))&(contador<2):
        if((listausuarios[k].getidc())==identificador):
            contador=contador+1
        k=k+1
   if (contador<2):
        print ("No se encontro el identificador repetido \n")
   else:
        print("Identificador repetido. \n")
   archivo.close()
