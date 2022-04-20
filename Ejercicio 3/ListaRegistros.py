class ListaRegistros:
    def __init__(self):
        self.__Registros=[]
    def AgregarRegistro(self, registro,dia, hora):
        if (type(registro)==Registro):
            self.__Registros[dia-1][hora].append(registro)
    def MostrarDatospordia(self, dia):
        print("Hora  Temperatura  Humedad  Presion  \n")
        for hora in self.__Registros[dia]:
            print("{}  {}\n".format(hora.index(), self.__Registros[dia][hora]))
    def MenorTemperatura(self):
        menor=self.__Registros[0][0].gettemperatura()
        for dia in self.__Registros:
            for hora in self.__Registros[dia]:
                if (menor<=self.__Registros[dia][hora].gettemperatura()):
                    menor=self.__Registros[dia][hora].gettemperatura()
        return (menor)
    def MenorHumedad(self):
        menor=self.__Registros[0][0].gethumedad()
        for dia in self.__Registros:
            for hora in self.__Registros[dia]:
                if (menor<=self.__Registros[dia][hora].gethumedad()):
                    menor=self.__Registros[dia][hora].gethumedad()
        return (menor)
    def MenorPresion(self):
        menor=self.__Registros[0][0].getpresion()
        for dia in self.__Registros:
            for hora in self.__Registros[dia]:
                if (menor<=self.__Registros[dia][hora].getpresion()):
                    menor=self.__Registros[dia][hora].getpresion()
        return (menor)
    def MayorPresion(self):
        mayor=self.__Registros[0][0].getpresion()
        for dia in self.__Registros:
            for hora in self.__Registros[dia]:
                if (mayor>=self.__Registros[dia][hora].getpresion()):
                    mayor=self.__Registros[dia][hora].getpresion()
        return (mayor)
    def MayorHumedad(self):
        mayor=self.__Registros[0][0].gethumedad()
        for dia in self.__Registros:
            for hora in self.__Registros[dia]:
                if (mayor>=self.__Registros[dia][hora].gethumedad()):
                    mayor=self.__Registros[dia][hora].gethumedad()
        return (mayor)
    def MayorTemperatura(self):
        mayor=self.__Registros[0][0].gettemperatura()
        for dia in self.__Registros:
            for hora in self.__Registros[dia]:
                if (mayor>=self.__Registros[dia][hora].gettemperatura()):
                    mayor=self.__Registros[dia][hora].gettemperatura()
        return (mayor)
    def Promedioporhora(self, hora):
        contador=0
        sumador=0
        for i in range(len(self.__Registros)):
            sumador+=self.__Registros[i][hora].gettemperatura()
            contador+=1
        return (contador/sumador)
    def PromedioMensual(self):
        print ("Promedios Mensuales de Temperaura por hora\n")
        for hora in range(len(self.__Registros[1])):
            print("{}: {}".format(hora, self.__Registros.Promedioporhora(hora)))