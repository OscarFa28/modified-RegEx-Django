import heapq

class BinaryTreeNode:
    def __init__(self, value, freq):
        # Nodo para el árbol binario con valor y frecuencia
        self.value = value
        self.freq = freq
        self.left, self.right = None, None

    def __lt__(self, node):
        # Comparación de nodos basada en la frecuencia
        return self.freq < node.freq

    def __eq__(self, node):
        # Igualdad de nodos basada en la frecuencia
        return self.freq == node.freq


class FileCompression:
    def __init__(self):
        # Inicialización de variables
        self.path = ""
        self.__heap = []  # Montón para el árbol Huffman
        self.__binaryCodes = {}  # Diccionario de códigos binarios para cada carácter
        self.__removeBinaryCodes = {}  # Diccionario para decodificar los códigos binarios

    # Crear un diccionario de frecuencias para cada carácter en el texto
    def __frequencyDictionary(self, text):
        freqDict = {}  # Inicializa un diccionario para almacenar las frecuencias
        
        # Itera sobre cada carácter en el texto
        for char in text:
            freqDict[char] = freqDict.get(char, 0) + 1  # Incrementa la frecuencia del carácter en el diccionario
        
        return freqDict  # Retorna el diccionario de frecuencias de caracteres


    # Construir un montón (heap) basado en las frecuencias de los caracteres
    def __buildHeap(self, freqDict):
        for value in freqDict:
            freq = freqDict[value]  # Obtiene la frecuencia del carácter
            node = BinaryTreeNode(value, freq)  # Crea un nodo con el carácter y su frecuencia
            heapq.heappush(self.__heap, node)  # Agrega el nodo al heap


    # Construir el árbol Huffman combinando los nodos del heap
    def __buildTree(self):
        while len(self.__heap) > 1:
            # Extraer los dos nodos con frecuencias más bajas
            node1 = heapq.heappop(self.__heap)
            node2 = heapq.heappop(self.__heap)
            
            # Calcular la suma de frecuencias de los dos nodos extraídos
            freqSum = node1.freq + node2.freq
            
            # Crear un nuevo nodo con la suma de frecuencias
            newNode = BinaryTreeNode(None, freqSum)
            
            # Asignar los nodos extraídos como hijos del nuevo nodo
            newNode.left = node1
            newNode.right = node2
            
            # Agregar el nuevo nodo al heap
            heapq.heappush(self.__heap, newNode)


    # Crear los códigos binarios para cada carácter basado en el árbol Huffman
    def __buildBinaryCodesHelper(self, node, currBits):
        if node is None:
            return
        
        # Si es un nodo hoja (con un valor asignado)
        if node.value is not None:
            # Asigna el código binario para el carácter al diccionario de códigos
            self.__binaryCodes[node.value] = currBits
            # Asigna el carácter al código binario para decodificar más tarde
            self.__removeBinaryCodes[currBits] = node.value
            return
        
        # Recursivamente, construye los códigos binarios para los nodos izquierdo y derecho
        self.__buildBinaryCodesHelper(node.left, currBits + "0")  # Agrega '0' para el lado izquierdo
        self.__buildBinaryCodesHelper(node.right, currBits + "1")  # Agrega '1' para el lado derecho


    # Construir los códigos binarios
    def __buildBinaryCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildBinaryCodesHelper(root, "")

    # Codificar el texto original utilizando los códigos binarios
    def __getEncodedText(self, text):
        encodedText = ""
        for char in text:
            encodedText += self.__binaryCodes[char]
        return encodedText

    