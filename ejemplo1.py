class vehiculo():

    def __init__(self,color, modelo, placa, nroasientos):
        self.color = color
        self.modelo = modelo
        self.placa = placa
        self.nroasientos = nroasientos

    def desplazarse(self):
        print("El vehiculo se esta desplazando")

    def subirpersona(self):
        print("La persona ha subido")

    def __str__(self):
        return "color: {}, modelo: {}, placa: {},nroasientos{}".format(self.color,
        self.modelo, self.placa,self.nroasientos)

vehiculo1 = vehiculo("Negro", "1997", "ADF123", 4)
vehiculo1.desplazarse()
vehiculo1.subirpersona()