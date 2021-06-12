

import re


###########################################################
#     Lexer(str: sourcecode) -> dict  
###########################################################
class Lexer:

    def __init__(self,code):
        self.code = code
        self.code_sp = code.split('\n')
        self.code_class = code.split('class')
        self.AboutClass = {}                    #It stores all the details abt of class in json format or dict.
        self.classnameReg = r'\b((?:public class|class|private class)\s*\w+)'  #Regex for class withot extends.
        self.classnameReg1 = r'\b((?:public class|class|private class)\s*\w+\s+extends\s*\w+)' #Regex for class with extend.
        self.methodsReg = r"\b((?:void|int|long|String|float)\s+\w+\s*\(\)).?" #Regex for Methos.
        self.variablesReg = r"\b((?:int|Long|String|float)\s*\w+)" #Regex for Variables which defined in single line.
        self.variablesReg1 = r"\b((?:int|Long|String|float)\s*\w+(?:\,\w+){1,})" #Regec for variables which are defined in manner (int i,n).
        self.Class()
        self.methods()
        self.variables()

    
    def Class(self):
       
        line1 = re.findall(self.classnameReg,self.code) #Finds all the lines which matches with regex without extend
        line2 = re.findall(self.classnameReg1,self.code) #Finds all the lines which matches with regex with extend
        line = line1+line2 #Grouping both the list together
        
        for line_lst in line: 

            line_lst = line_lst.split()
            # First Lets check the Access Modifiers of the class
            Modifier =  [line_lst[i] for i in range(len(line_lst)) if line_lst[i] == "private" or line_lst[i] == 'protected']
            classAccess = Modifier[0] if Modifier else 'public'
            # Removing Modifiers.
            line_lst = [i for i in line_lst if i not in ["public","class","private",'protected']]
            # After removing Modifiers first word in list will be the class name.
            classname = line_lst[0]
            # Now Lets check whether the class is Base class or Inherited one.
            #print(line_lst)
            extend_class = [line_lst[i+1] for i in range(len(line_lst)) if line_lst[i] == 'extends']
            
            inherit =  extend_class[0] if extend_class else 'Base'
            self.AboutClass[classname] = {'classname' : classname,'modifier' : classAccess,"Inherited":inherit,"class Variables":[],"class methods":[]}
        return 

        
  


    def methods(self):
        classes = self.AboutClass.keys() # Lets store all the keys of self.AboutClass dict.

        for code in self.code_class: 
            if code.strip().split()[0] in classes: # Lets check the first line starting word is in classes list.
                classname = code.strip().split()[0] # we get class name.
                methods = re.findall(self.methodsReg,code) # lets find all the methods inside class.
                self.AboutClass[classname]['class methods'].extend(methods) # lets store that in self.AboutClass dict.
        return
    
    def variables(self):
        classes = self.AboutClass.keys() # lets store all the keys of self.AboutClass dict
        for code in self.code_class:
            if code.strip().split()[0] in classes: # Lets check the first line starting word is in classes list.
                classname = code.strip().split()[0] # we get class name.
                variables = re.findall(self.variablesReg,code) # Finds all the matches with regex
                variables1 = re.findall(self.variablesReg1,code)
                
                # This used to get all group initilized variables like int i,n;
                if variables1:
                    for var in variables1:
                        var = var.split(",")
                        dataType = var[0].split()[0]
                    variables1 = [dataType+" "+i for i in var[1:]]
                ######################################################
                self.AboutClass[classname]['class Variables'].extend(variables+variables1)
        return

    
    def display(self):
        import json
        print(json.dumps(self.AboutClass,indent=4))

    def classDict(self):
        return self.AboutClass


