class ropero():

    def __init__(self, color, alto, ancho, nrocajones, precio):
        self.color = color
        self.alto = alto
        self.ancho = ancho
        self.nrocajones = nrocajones
        self.precio = precio

    def comprar(self):
        print("El ropero ha sido comprado")

    def vender(self):
        print("El ropero ha sido vendido")

    def regalar(self):
        print("El ropero ha sido regalado")

    def __str__(self):
        return "color: {}, alto: {}, ancho: {},nrocajones {},precio{}".format(self.color,
        self.alto, self.ancho,self.nrocajones, self.precio)

ropero1 = ropero("Blanco", "10 metros", "8 metros", 4 , "200 Bs")
ropero1.comprar()
ropero1.vender()
ropero1.regalar()