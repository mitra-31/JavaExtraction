'''


sourceCode = []  # Appending the source code to the sourceCode variable.


print("Enter/Paste your code.Ctrl+d (or) Ctrl+Z ( windows ) to save it.")    # when we hit Ctrl+z it will invoke except and it stops taking input from user. 
while True:
  try:
    sourceCode.append(input(">> ").strip())
  except EOFError:
    break


sourceCode = "\n".join(sourceCode)


#Object of Lexer class
result = Lexer(sourceCode).classDict()



####################################################################
# result -> dict
# print(result)
# classname:{'classname':classname,"modifier":modifier,"Inherited":classname'or'Base,'class variables':vars,"class methods":methods}
# To get specific classnames->methods => print(result['classname']['class methods']) this prints specfic class methods
#####################################################################

for key,value in result.items():
  print(f'{key}:{value}')
  print()
#PlantumlTxt.writeUml(sourceCode).run()

#print(dir(sourceCode))
'''

import eel
import json
import datetime
from tokens import Lexer
from PlantumlTxt import writeUml
eel.init('web')

@eel.expose
def val(code):
  #print(datetime.datetime.now())
  result = content(code)
  results = json.dumps(result)
  classnames = list(result.keys())
  print("Retrived Successfully")
  #print(reu
  return results,classnames


def content(code):
  sourceCode = [x.strip() for x in code.split('\n')]
  SourceCode = "\n".join(sourceCode)
  return Lexer(SourceCode).classDict()

@eel.expose
def ret_uml(code):
  writeUml(content(code)).run()
  return


eel.start("index.html",size=(1020,660))

