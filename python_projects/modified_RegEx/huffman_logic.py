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





    # Añadir relleno al texto codificado para asegurar su longitud en múltiplos de 8
    def __getPaddedEncodedText(self, encodedText):
        paddedAmount = 8 - (len(encodedText) % 8)  # Calcula la cantidad de bits a agregar

        # Agrega ceros al texto codificado para hacer su longitud un múltiplo de 8
        for _ in range(paddedAmount):
            encodedText += "0"
        
        # Representa la cantidad de bits agregados en formato binario de 8 bits
        paddedInfo = "{0:08b}".format(paddedAmount)
        
        # Combina la información del relleno con el texto codificado
        paddedEncodedText = paddedInfo + encodedText
        
        return paddedEncodedText  # Retorna el texto codificado con el relleno añadido


    # Convertir el texto con ceros y unos en una lista de enteros
    def __getIntList(self, paddedEncodedText):
        intList = []
        
        # Itera sobre el texto codificado en bloques de 8 bits (1 byte)
        for i in range(0, len(paddedEncodedText), 8):
            byte = paddedEncodedText[i:i + 8]  # Toma un bloque de 8 bits
            
            # Convierte el bloque de bits a un entero y lo agrega a la lista
            intList.append(int(byte, 2))
        
        return intList  # Retorna la lista de enteros correspondientes al texto codificado


    # Comprimir un archivo
    def compress(self, file):
        text = file.read().decode('utf-8')  # Leer el archivo y obtener su contenido como texto
        return self.huffman_compress(text)  # Llamar a la función huffman_compress

    # Función principal para comprimir utilizando el algoritmo de Huffman
    def huffman_compress(self, text):
        freqDict = self.__frequencyDictionary(text)
        self.__buildHeap(freqDict)
        self.__buildTree()
        self.__buildBinaryCodes()
        encodedText = self.__getEncodedText(text)
        paddedEncodedText = self.__getPaddedEncodedText(encodedText)
        intList = self.__getIntList(paddedEncodedText)
        return intList

    # Remover el relleno del texto
    def __removePadding(self, text):
        paddedInfo = text[:8]  # Obtiene los primeros 8 bits que representan la información del relleno
        paddedAmount = int(paddedInfo, 2)  # Convierte la información del relleno a un número entero
        
        # Remueve los bits de relleno del final del texto para obtener el texto original
        text = text[8:]  # Descarta la información del relleno
        actualText = text[:-1 * paddedAmount]  # Remueve los bits de relleno basados en la información obtenida
        
        return actualText  # Retorna el texto original sin el relleno agregado


    # Decodificar el texto a partir de los códigos binarios
    def __decodeText(self, text):
        # Decodifica el texto utilizando los códigos binarios almacenados
        decodedText = ""  # Inicializa el texto decodificado
        currBits = ""  # Inicializa los bits actuales a vacío
        
        # Itera a través de los bits del texto codificado
        for bit in text:
            currBits += bit  # Agrega el bit actual al conjunto de bits actuales
            
            # Verifica si los bits actuales tienen una correspondencia en los códigos binarios
            if self.__removeBinaryCodes.get(currBits) is not None:
                # Si se encuentra una correspondencia, obtén el carácter correspondiente
                char = self.__removeBinaryCodes[currBits]
                decodedText += str(char)  # Agrega el carácter decodificado al texto resultante
                currBits = ""  # Reinicia los bits actuales para la próxima secuencia de bits
        
        return decodedText  # Retorna el texto decodificado


    # Descomprimir un archivo
    def decompress(self, uploaded_file):
        bitString = ""  # Inicializa una cadena de bits vacía
        byte = uploaded_file.read(1)  # Lee un byte del archivo
        
        # Lee byte por byte del archivo y convierte cada byte en su representación binaria de 8 bits
        while byte:
            byte = ord(byte)  # Convierte el byte a su valor entero
            bits = bin(byte)[2:].rjust(8, "0")  # Convierte el entero a su representación binaria
            bitString += bits  # Agrega los bits al string de bits
            byte = uploaded_file.read(1)  # Lee el próximo byte del archivo
        
        # Elimina el relleno y decodifica el texto comprimido
        actualText = self.__removePadding(bitString)  # Elimina el relleno del texto comprimido
        decompressedText = self.__decodeText(actualText)  # Decodifica el texto comprimido
        return decompressedText  # Retorna el texto descomprimido