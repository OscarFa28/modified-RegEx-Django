import math




class HeapNode:
    def __init__(self, key, value=None):
        self.key = key          # Clave del nodo
        self.value = value      # Valor asociado al nodo (opcional)

class Heap:
    def __init__(self):
        self.heap = []           # Inicializar la lista que contendrá el heap
        self.size = 0            # Inicializar el tamaño del heap
    
    def parent(self, idx):
        return idx // 2          # Calcula el índice del padre de un nodo

    def left_child(self, idx):
        return idx * 2          # Calcula el índice del hijo izquierdo de un nodo
    
    def right_child(self, idx):
        return idx * 2 + 1      # Calcula el índice del hijo derecho de un nodo
    
    def heapify(self, idx):
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)

        largest_idx = idx

        # Compara el nodo con sus hijos y encuentra el índice del mayor
        if left_idx <= self.size and self.heap[left_idx].key > self.heap[idx].key:
            largest_idx = left_idx

        if right_idx <= self.size and self.heap[right_idx].key > self.heap[largest_idx].key:
            largest_idx = right_idx

        if largest_idx != idx:
            # Intercambia el nodo actual con el nodo mayor
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            self.heapify(largest_idx)

    def build_heap(self, elements):
        self.heap = elements
        self.size = len(elements)
        self.heap.insert(0, HeapNode(-math.inf))  # Inserta un nodo "infinito" en la posición 0

        # Aplica heapify a los nodos desde la mitad hacia atrás para construir el heap
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)
    
    def heap_max(self):
        if self.size == 0:
            return None  # El heap está vacío
        return self.heap[1]  # Retorna el nodo con el valor máximo

    def heap_extract_max(self):
        if self.size == 0:
            return None  # El heap está vacío

        max_node = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify(1)  # Restaura la propiedad del heap

        return max_node
        
    def heap_increase_key(self, indice, new_node):
        if new_node.key <= self.heap[indice].key:
            return None  # La nueva clave no es mayor que la actual

        self.heap[indice] = new_node

        while indice > 1:
            padre = self.parent(indice)

            if self.heap[indice].key < self.heap[padre].key:
                # Intercambia el nodo con su padre si la clave es menor
                self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
                indice = padre
            else:
                break

    
    def heap_extract_min(self):
        if self.size == 0:
            return None  # El heap está vacío

        min_node = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify_min(1)  # Restaura la propiedad del heap

        return min_node

    def heapify_min(self, idx):
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)

        smallest_idx = idx

        # Compara el nodo con sus hijos y encuentra el índice del menor
        if left_idx <= self.size and self.heap[left_idx].key < self.heap[idx].key:
            smallest_idx = left_idx

        if right_idx <= self.size and self.heap[right_idx].key < self.heap[smallest_idx].key:
            smallest_idx = right_idx

        if smallest_idx != idx:
            # Intercambia el nodo actual con el nodo menor
            self.heap[idx], self.heap[smallest_idx] = self.heap[smallest_idx], self.heap[idx]
            self.heapify_min(smallest_idx)

    def heap_insert(self, value):
        if self.size >= len(self.heap) - 1:
            self.heap.append(HeapNode(-math.inf, value))
        else:
            self.size += 1
            self.heap[self.size] = HeapNode(-math.inf, value)

        self.heap_increase_key(self.size, value)

    def get_size(self):
        return self.size

    def print_heap(self):
        for node in self.heap[1:]:
            print("Key:", node.key, "Value:", node.value)

