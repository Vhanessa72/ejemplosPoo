class Ropero():

    def __init__(self, color, alto, ancho, nro_cajones, precio):
        self.color = color
        self.alto = alto
        self.ancho = ancho
        self.nrocajones = nro_cajones
        self.precio = precio

    def comprar(self):
        print("El ropero ha sido comprado")

    def vender(self):
        print("El ropero ha sido vendido")

    def regalar(self):
        print("El ropero ha sido regalado")

    def __str__(self):
        return "color: {}, alto: {}, ancho: {},nro_cajones {},precio{}".format(self.color,
        self.alto, self.ancho,self.nro_cajones, self.precio)

ropero_1 = Ropero("Blanco", "10 metros", "8 metros", 4 , "200 Bs")
ropero_1.comprar()
ropero_1.vender()
ropero_1.regalar()