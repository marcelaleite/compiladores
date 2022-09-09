from lexico import Lexico
from sintaticoDescendenteRecursivo import SintaticoDescendenteRecursivo
from sintaticoDescendentePreditivo import SintaticoDescendentePreditivo

entrada = input('informe uma entrada: ')
lex = Lexico(entrada+"$")

# print("Entrada: "+entrada)
# sin = SintaticoDescendenteRecursivo(lex) 
# if sin.P():
#     print("Linguagem aceita.")
# else:
#     print("Erro sintático.")


s = SintaticoDescendentePreditivo(lex)
# print(s.M['P']['DEC'])
# x = s.M['P']['DEC'];
# print(x)
s.sintatico()
