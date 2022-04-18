import csv
import ViajeroFrecuente

if __name__=="__main__":
    lista=[]
    archivo=open("viajeros.csv")
    reader=csv.reader(archivo, delimiter=",")
    for fila in reader:
        lista.append(ViajeroFrecuente.ViajeroFrecuente(int(fila[0]), int(fila[1]), fila[2], fila[3], int(fila[4])))
    viajero=int(input("Ingrese un numero de viajero\n"))
    viaj=-1
    for i in lista:
        if (i.getnumerodeviajero()==viajero):
            viaj=i
    if (viaj!=-1):
        control=1
        while (control!=0):
            control=int(input("\n--------Menu---------\nIngrese la opcion:\n1- Consultar Millas\n2- Acumular Millas\n3- Canjear Millas\n0: Salir\n"))
            if (control==1):
                print("Millas: {}".format(viaj.CantidadTotalMillas()))
            if (control==2):
                a=int(input("Ingrese millas a acumular\n"))
                print("Millas totales: {}".format(viaj.AcumularMillas(a)))
            if (control==3):
                a=int(input("Ingrese millas a canjear\n"))
                print("Millas acumuladas que quedaron: {}".format(viaj.CanjearMillas(a)))
    else:
        print ("numero de viajero no existente \n")