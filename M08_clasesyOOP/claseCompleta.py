class modulo7():
    def __init__(self, numero, lista):
        self.numero = numero
        self.lista = lista

    def Primo(self):
        if self.numero < 2:
            return False
        for i in range(2, self.numero):
            if self.numero % i == 0:
                return False
        return True
    
    def valor_modal(self):
        lista_unicos = []
        lista_repeticiones = []
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def Celsius_a_FK(self):
        if self.que=="grados" and self.aque=="farenheit":
            f=(self.valor*9/5)+32
            return f
        if self.que=="grados" and self.aque=="kelvin":
            k=self.valor+273.15
            return k
        

    def factorial(self):
        resultado=0
        if type(self.numero) != int:
            return None
        else:
            resultado+=self.numero*modulo7.factorial(self.numero-1)
            return resultado
