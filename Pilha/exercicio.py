# -*- coding:utf-8 -*-

from no import No

class Pilha:
    def __init__(self):

        self.topo = None
        self.tamanho = 0

    def is_empty(self):
        return True if self.tamanho <= 0 else False

    def push(self, valor):
        no = No(valor)
        no.__prox = self.topo
        self.topo = no
        self.tamanho += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
            valor = self.topo
            self.topo = self.topo.__prox
            self.tamanho -= 1
            return valor._valor

    def peek(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
            return self.topo._valor

    """ def list_items(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
            print("Relação de itens na pilha:\n")
           # pilha_invertida = self.__pilha.reverse() 
            for item in self.__pilha:
                print(item)
            print("Base da Pilha") """
        
    def get_size(self):
        return self.tamanho