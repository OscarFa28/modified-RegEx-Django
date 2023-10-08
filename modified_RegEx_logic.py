class modified_RegEx():
    
    def __init__(self):
        self.shifts = []
        self.dictionary = {}
        self.size_of_pattern = 0
        self.size_of_text = 0
        self.query = None
        self.new = None
        self.search_and_replace = None
        self.g_flag = None
        self.i_flag = None
        
    def bmh(self, text, pattern): # regresa todas las incidencias del patrón en el texto
        self.size_of_text = len(text)
        self.size_of_pattern = len(pattern)
        self.build_bmt(pattern)
        for i in range(self.size_of_text - self.size_of_pattern + 1):
            
            
            k = self.size_of_pattern - 1
            temp = i + k
            for k in range(k, -1, -1):
                if pattern[k] != text[temp]:
                    i += (self.dictionary[text[temp]]) - 1
                    break
                elif k == 0:
                    self.shifts.append(i)
                temp -= 1
                
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
         
    def read_first_function(self, query, new):
        self.query = query  
        self.new = new    
        
        if self.query.startswith("fr "):
            self.search_and_replace = True
        
        elif self.query.startswith("f "):
            self.search_and_replace = False

        else:
            return "query no válida"
        
        return self.read_flags()

        
    def read_flags(self):
        if self.query[len(self.query)-1] == 'i' and self.query[len(self.query)-2] == ' ':
            if self.query[len(self.query)-2] == 'g' and self.query[len(self.query)-3] == ' ':
                #flag: i and g
                self.i_flag = True
                self.g_flag = True
                
            else:
                #flag: i
                self.i_flag = True
                self.g_flag = False
                
        if self.query[len(self.query)-1] == 'g':
            if self.query[len(self.query)-2] == 'i' and self.query[len(self.query)-3] == ' ':
                #flag: i and g
                self.i_flag = True
                self.g_flag = True
                
            else:
                #flag: g
                self.i_flag = False
                self.g_flag = True

        else:
            self.i_flag = False
            self.g_flag = False
            
        return self.process()
       
    
    def process(self):
        pass
    
text = "This is a sample text that you can use for testing your pattern matching code. It contains various words and characters to search through the text."
pattern = "ing"

st = modified_RegEx()

print(st.read_first_function(input()))


shifts = st.bmh(text, pattern) 

print(shifts)
print("Coincidences: "+str(len(shifts)))

    