# -*- coding:utf-8 -*-

class Pilha:
    def __init__(self):
        self.__pilha = []
        #self.topo = None
        #self.tamanho = 0

    def is_empty(self):
        return True if len(self.__pilha) == 0 else False

    def push(self, valor):
        self.__pilha.append(valor)

    def pop(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
            valor = self.__pilha.pop()
            return valor

    def peek(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
            valor = self.__pilha[-1]
            return valor

    def list_items(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
            print("Relação de itens na pilha:\n")
            pilha_invertida = self.__pilha.reverse() 
            for item in self.__pilha:
                print(item)
            print("Base da Pilha")
        
    def get_size(self):
        return len(self.__pilha)