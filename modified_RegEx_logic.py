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
                
        print(text)        
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
    
text = "This for is a sample text for that you gooooold can use for testing your pattern matching code. It contains various for words gooooold and characters to search through the text."
pattern = "ing"

st = modified_RegEx()

print(st.read_first_function(input(), 'CAMBIO', text))




    