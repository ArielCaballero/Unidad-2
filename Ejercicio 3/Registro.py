class Registro:
    def __init__(self, Temperatura, Humedad, Presion):
        if (type(Temperatura)==float)&(type(Humedad)==int)&(type(Presion)==float):
            self.__temperatura=Temperatura
            self.__humedad= Humedad
            self.__presion= Presion
    def gettemperatura(self):
        return(self.__temperatura)
    def gethumedad(self):
        return(self.__humedad)
    def getpresion(self):
        return(self.__presion)
    def __str__(self):
        return ("{:11}  {:7}  {:7}".format(self.__temperatura,self.__humedad,self.__presion))
