import math

class modified_RegEx():
    
    def __init__(self):
        self.shifts = []
        self.dictionary = {}
        self.size_of_pattern = 0
        self.size_of_pattern_2 = 0
        self.size_of_text = 0
        self.query = None
        self.new = None
        self.search_and_replace = None
        self.g_flag = None
        self.i_flag = None
        self.text = None
        
    def bmh(self, text, pattern): 
        self.size_of_text = len(text)
        self.size_of_pattern = len(pattern)
        self.build_bmt(pattern)
        
        found = False
        for i in range(self.size_of_text - self.size_of_pattern + 1):
            if i >= (self.size_of_text - self.size_of_pattern + 1):
                break
            
            k = self.size_of_pattern - 1
            temp = i + k
            for k in range(k, -1, -1):
                
                if pattern[k] != text[temp] and pattern[k] != '*':
                    i += (self.dictionary[text[temp]]) - 1
                    break
                elif k == 0:
                    self.shifts.append(i)
                    found = True
                    if self.search_and_replace:
                        text = text[:i] + self.new + text[i + self.size_of_pattern:]
                        i += len(self.new)
                        self.size_of_text = len(text)
                    
                temp -= 1
             
            if found and not self.g_flag :
                break 
               
        self.text = text              
        return self.shifts
    
    
    def bmh_or(self, text, pattern, pattern_2): 
        self.size_of_text = len(text)
        self.size_of_pattern = len(pattern)
        self.size_of_pattern_2 = len(pattern_2)
        self.build_bmt(pattern)
        found_1 = math.inf
        found_2 = math.inf
        
        found = False
        for i in range(self.size_of_text - self.size_of_pattern + 1):
            if i >= (self.size_of_text - self.size_of_pattern + 1):
                break
            
            k = self.size_of_pattern - 1
            temp = i + k
            for k in range(k, -1, -1):
                
                if pattern[k] != text[temp] and pattern[k] != '*':
                    i += (self.dictionary[text[temp]]) - 1
                    break
                elif k == 0:
                    self.shifts.append(i)
                    found = True
                    found_1 = i
                    if self.search_and_replace and self.g_flag:
                        text = text[:i] + self.new + text[i + self.size_of_pattern:]
                        i += len(self.new)
                        self.size_of_text = len(text)
                    
                temp -= 1
             
            if found and not self.g_flag :
                break 
            
            
        found = False
        i = 0    
        for i in range(self.size_of_text - self.size_of_pattern_2 + 1):
            if i >= (self.size_of_text - self.size_of_pattern_2 + 1):
                break
            
            k = self.size_of_pattern_2 - 1
            temp = i + k
            for k in range(k, -1, -1):
                
                if pattern_2[k] != text[temp] and pattern_2[k] != '*':
                    i += (self.dictionary[text[temp]]) - 1
                    break
                elif k == 0:
                    self.shifts.append(i)
                    found = True
                    found_2 = i
                    if self.search_and_replace and self.g_flag:
                        text = text[:i] + self.new + text[i + self.size_of_pattern_2:]
                        i += len(self.new)
                        self.size_of_text = len(text)
                    
                temp -= 1
             
            if found and not self.g_flag :
                break    
                
                   
        if found_1 < found_2:
            s = found_1
            pattern_small = self.size_of_pattern
        else:
            s = found_2
            pattern_small = self.size_of_pattern_2
        
        if self.search_and_replace and not self.g_flag:
                        text = text[:s] + self.new + text[s + pattern_small:]
                        s += len(self.new)
                        self.size_of_text = len(text)  
                        self.shifts.clear()  
                        self.shifts.append(s)   
                        
        elif not self.search_and_replace:
            self.shifts.clear()  
            self.shifts.append(s)       
                           
        self.shifts.sort()  
        self.text = text           
        return self.shifts

    def build_bmt(self, pattern):
        i = self.size_of_pattern - 1
        for i in range(i, -1, -1):
            if pattern[i] == self.size_of_pattern -1:
                self.dictionary[pattern[i]] = self.size_of_pattern
            elif pattern[i] not in self.dictionary:
                self.dictionary[pattern[i]] = self.size_of_pattern - i

        
        for j in range(127):
            if chr(j) not in self.dictionary:
                self.dictionary[chr(j)] = len(pattern)
                
    def build_bmt_or(self, first_pattern, second_pattern):
        i = len(first_pattern) - 1
        k = len(second_pattern) - 1
        for i in range(i, -1, -1):
            if i == len(first_pattern) -1:
                self.dictionary[first_pattern[i]] = len(first_pattern)
            elif first_pattern[i] not in self.dictionary:
                self.dictionary[first_pattern[i]] = len(first_pattern) - i

        for k in range(k, -1, -1):
            if k == len(second_pattern) - 1 and second_pattern[k] in self.dictionary and self.dictionary[second_pattern[k]] > len(second_pattern):
                self.dictionary[second_pattern[k]] = len(second_pattern)
            elif second_pattern[k] not in self.dictionary or self.dictionary[second_pattern[k]] > len(second_pattern) - k:
                self.dictionary[second_pattern[k]] = len(second_pattern) - k

        if len(second_pattern) < len(first_pattern):
            small_pattern = second_pattern
            
        else:
            small_pattern = first_pattern
                
        for j in range(127):
            if chr(j) not in self.dictionary:
                self.dictionary[chr(j)] = len(small_pattern)            
         
    def read_first_function(self, query, new, text):
        self.query = query  
        self.new = new    
        self.text = text
        if self.query.startswith("fr "):
            self.search_and_replace = True
            self.query = self.query[3:]
        
        elif self.query.startswith("f "):
            self.search_and_replace = False
            self.query = self.query[2:]

        else:
            return "query no válida"
        
        return self.read_flags()

        
    def read_flags(self):
        if self.query[len(self.query)-1] == 'i' and self.query[len(self.query)-2] == ' ':
            if self.query[len(self.query)-3] == 'g' and self.query[len(self.query)-4] == ' ':
                #flag: i and g
                self.i_flag = True
                self.g_flag = True
                self.query = self.query[:len(self.query)-4]
                
            else:
                #flag: i
                self.i_flag = True
                self.g_flag = False
                self.query = self.query[:len(self.query)-2]
                
        elif self.query[len(self.query)-1] == 'g':
            if self.query[len(self.query)-3] == 'i' and self.query[len(self.query)-4] == ' ':
                #flag: i and g
                self.i_flag = True
                self.g_flag = True
                self.query = self.query[:len(self.query)-4]
                
            else:
                #flag: g
                self.i_flag = False
                self.g_flag = True
                self.query = self.query[:len(self.query)-2]

        else:
            self.i_flag = False
            self.g_flag = False
            
        return self.process()
       
    
    def process(self):
        #operador or
        if '|' in self.query:
            j = len(self.query)-1
            while j > -1:
                if self.query[j] == '|':
                    first_pattern = self.query[:j-1]
                    second_pattern = self.query[j+2:]
                j -= 1
            self.build_bmt_or(first_pattern, second_pattern)   
            return self.bmh_or(self.text, first_pattern, second_pattern) 
            
        
        #operador de repetición
        if '{' in self.query and '}' in self.query:
            i = 0  # Inicializa el índice i
            while i < len(self.query):
                if self.query[i] == '{':
                    letter = self.query[i-1]
                    repeat = int(self.query[i + 1])
                    repeat_letters = ''
                    
                    for j in range(repeat-1):
                        repeat_letters += letter
                        
                    self.query = self.query[:i] + repeat_letters + self.query[i+3:]
                i += 1
                  
            self.build_bmt(self.query) 
            return self.bmh(self.text, self.query)    
        
        else:
            self.build_bmt(self.query) 
            return self.bmh(self.text, self.query)       
    
    
    def return_text(self):
        return self.text


file_name = r'C:\Users\of_de\OneDrive\Documentos\3er Semestre\Estructura de datos y algoritmos 2\Parcial_2\proyecto\example_text.txt'
with open(file_name, 'r') as archivo:
    text = archivo.read()

st = modified_RegEx()

print(st.read_first_function(input(), 'UNAV', text))
modified_text = st.return_text()

with open(file_name, 'w') as archivo:
    archivo.write(modified_text)

    