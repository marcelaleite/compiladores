from lexico import Lexico

class Sintatico:
    '''
        Analisador sintático de descida recursiva para a seguinte gramática
        <P> ::= DEC ID ABRE_BLOCO <LISTA_BLOCO> FECHA_BLOCO
        <LISTA_BLOCO> ::= <BLOCO> <LISTA_BLOCO> | <BLOCO> 
        <BLOCO> ::= <ATR> | <SEL_IF>
        <ATR> ::= ID ATRIBUICAO <VAR>
        <VAR> ::= ID | CONST
        <SEL_IF> ::= IF ABRE_PAR ID COMPARA ID FECHA_PAR ABRE_BLOCO <BLOCO> FECHA_BLOCO 
        O analisador deve implementar um método para cada produção da gramática
        e executar de forma recursiva a partir do simbolo inicial da gramática
    '''

    def __init__(self, lexico: Lexico):
        self.contador = 0
        # self.backtrack = 0
        self.lexico = lexico

    def term(self,token):
        print("term("+self.lexico.lista_tokens[self.contador].token+"=="+token+")")
        ret =  self.lexico.lista_tokens[self.contador].token == token
        self.contador += 1
        return ret


    #<LISTA_BLOCO> ::= <BLOCO>
    def LISTA_BLOCO1(self):
        print("#<LISTA_BLOCO> ::= <BLOCO>")
        return self.BLOCO()

    #<LISTA_BLOCO> ::= <BLOCO> <LISTA_BLOCO>
    def LISTA_BLOCO2(self):
        print(" #<LISTA_BLOCO> ::= <BLOCO> <LISTA_BLOCO>")
        return self.BLOCO() and self.LISTA_BLOCO()

    #<LISTA_BLOCO> ::= <BLOCO> <LISTA_BLOCO> | <BLOCO> 
    def LISTA_BLOCO(self):
        print("#<LISTA_BLOCO> ::= <BLOCO> <LISTA_BLOCO> | <BLOCO> ")
        anterior = self.contador
        if self.LISTA_BLOCO1():
            return True
        else:
            self.contador = anterior
            return self.LISTA_BLOCO2()
   
    #<P> ::= DEC ID ABRE_BLOCO <LISTA_BLOCO> FECHA_BLOCO
    def P(self):
        print("#<P> ::= DEC ID ABRE_BLOCO <LISTA_BLOCO> FECHA_BLOCO")
        return self.term("DEC") and self.term("ID") and self.term("ABRE_BLOCO") and self.LISTA_BLOCO() and self.term("FECHA_BLOCO")

    #<ATR> ::= ID ATRIBUICAO <VAR>
    def ATR(self):
        print("#<ATR> ::= ID ATRIBUICAO <VAR>")
        return self.term("ID") and self.term("ATRIBUICAO") and self.VAR()

    #<BLOCO> ::= <ATR>
    def BLOCO1(self):
        print(" #<BLOCO> ::= <ATR>")
        return self.ATR()

     #<BLOCO> ::= <SEL_IF>
    def BLOCO2(self):
        print("#<BLOCO> ::= <SEL_IF>")
        return self.SEL_IF()

    #<BLOCO> ::= <ATR> | <SEL_IF>
    def BLOCO(self):
        print("#<BLOCO> ::= <ATR> | <SEL_IF>")
        anterior = self.contador
        if self.BLOCO1():
            return True
        else:
            self.contador = anterior
            return self.BLOCO2()
    
    #<VAR> ::= ID
    def VAR1(self):
        print(" #<VAR> ::= ID")
        return self.term("ID")

    #<VAR> ::= CONST
    def VAR2(self):
        print(" #<VAR> ::= CONST")
        return self.term("CONST")

    #<VAR> ::= ID | CONST
    def VAR(self):
        print("#<VAR> ::= ID | CONST")
        anterior = self.contador
        if self.VAR1():
            return True
        else:
            self.contador = anterior
            return self.VAR2()     
    
    #<SEL_IF> ::= IF ABRE_PAR ID COMPARA ID FECHA_PAR ABRE_BLOCO <BLOCO> FECHA_BLOCO 
    def SEL_IF(self):
        print("#<SEL_IF> ::= IF ABRE_PAR ID COMPARA ID FECHA_PAR ABRE_BLOCO <BLOCO> FECHA_BLOCO ")
        return self.term("IF") and self.term("ABRE_PAR") and self.term("ID") and self.term("COMPARA") and self.term("ID") and self.term("FECHA_PAR")  and self.term("ABRE_BLOCO") and self.LISTA_BLOCO() and self.term("FECHA_BLOCO")