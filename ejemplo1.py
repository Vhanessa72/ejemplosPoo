class Vehiculo():

    def __init__(self,color, modelo, placa, nro_asientos):
        self.color = color
        self.modelo = modelo
        self.placa = placa
        self.nroasientos = nro_asientos

    def desplazarse(self):
        print("El vehiculo se esta desplazando")

    def subirpersona(self):
        print("La persona ha subido")

    def __str__(self):
        return "color: {}, modelo: {}, placa: {},nro_asientos{}".format(self.color,
        self.modelo, self.placa,self.nro_asientos)

vehiculo_1 = Vehiculo("Negro", "1997", "ADF123", 4)
vehiculo_1.desplazarse()
vehiculo_1.subirpersona()