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
            return valor.get_valor()

    def peek(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
           return self.topo.get_valor()
        
    def list_items(self):
        if self.is_empty():
            raise Exception("Sorry, pilha vazia!")
        else:
            a = ''
            c = self.topo
            while(c):
                a += str(c.get_valor()) + '\n'
                c = c.__prox
            return a
        
    def __str__(self) -> str:
        return self.list_items()
    
    def get_size(self):
        return self.tamanho