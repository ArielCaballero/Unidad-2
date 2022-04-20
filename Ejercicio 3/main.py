import csv
import Registro as Registro
import ListaRegistros as ListaRegistros

if __name__=="__main__":
    Lista=ListaRegistros
    archivo=open("temperaturas.csv")
    reader=csv.reader(archivo, delimiter=",")
    for fila in reader:
        registrotemporal=Registro(fila[2], fila[3], fila[4])
        Lista.AgregarRegistro(registrotemporal, fila[0], fila[1])
    print(Lista[0][0])
    control=int(input("--------Menu------\nSelecciones una opcion:\n1-Mostrar para cada variable el mayor y menor valor\n2: Temperatura Promedio\n3:Listar por dia\n0- Salir\n"))
    while control!=0:
        if control==1:
            print("Mayor Temperatura: {}\n Menor Temperatura: {}\n Mayor Humedad: {}\n Menor Humedad: {}\n Mayor Presion {}\n Menor Presion\n".format(Lista.MayorTemperatura(),Lista.MenorTemperatura(),Lista.MayorHumedad(), Lista.MenorHumedad(), Lista.MayorPresion(), Lista.MenorPresion()))
        if control==2:
            Lista.PromedioMensual()
        if control==3:
            dia=input("Ingrese un dia\n")
            Lista.MostrarDatospordia(dia)
        control=int(input("--------Menu------\nSelecciones una opcion:\n1-Mostrar para cada variable el mayor y menor valor\n2: Temperatura Promedio\n3:Listar por dia\n0- Salir\n"))