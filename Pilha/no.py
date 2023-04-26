class No:
    def __init__(self, valor) -> None:
        self._valor = valor 
        self.__prox = None

    @property
    def valor(self):
         return self._valor
       
     
    @valor.setter
    def valor(self, newValor):
       self._valor = newValor
   