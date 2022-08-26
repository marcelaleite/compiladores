from lexico import Lexico
from sintatico import Sintatico

entrada = input('informe uma entrada: ')
lex = Lexico(entrada)

print("Entrada: "+entrada)
sin = Sintatico(lex) 
if sin.P():
    print("Linguagem aceita.")
else:
    print("Erro sintático.")




