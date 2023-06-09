from pilha import Pilha

pilha = Pilha()

print(f"Tamanho da pilha: {pilha.get_size()}")
print(f"Pilha vazia? {pilha.is_empty()}")

pilha.push("Valor 1") # 4 3 2 1
pilha.push("Valor 2")
pilha.push("Valor 3")
pilha.push("Valor 4")

print(f"Topo da pilha: {pilha.peek()}")
print(f"Tamanho da pilha: {pilha.get_size()}")
print(f"Removendo item da pilha: {pilha.pop()}")
print(f"Tamanho da pilha: {pilha.get_size()}")
print(f"Pilha vazia? {pilha.is_empty()}")

pilha.list_items()
print(pilha)

print(f"Removendo item da pilha: {pilha.pop()}")
print(f"Removendo item da pilha: {pilha.pop()}")
print(f"Removendo item da pilha: {pilha.pop()}")
print(f"Removendo item da pilha: {pilha.pop()}") 