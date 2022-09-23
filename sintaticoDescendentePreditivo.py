from posixpath import lexists
from lexico import Lexico
from pilha import Pilha

'''
        O analisador descendente preditivo utiliza a mesma gramática LL que o recursivo
        porém, em vez de backtrack (voltar caso escolha a produção errada), o analisador 
        toma a decisão de qual produção escolher olhando o próximo token a frente,
        por isso, a gramática de analisador é conhecida como LL(k), sendo k o número de tokens 
        a frente avaliados, geralmente k = 1
        Gramática:
        ---------------------------------------------------------------------------------------------------------
        <P>            ::= DEC ID ABRE_PAR <LISTA_PARAM> FECHA_PAR ABRE_BLOCO <LISTA_BLOCO> FECHA_BLOCO
        <LISTA_PARAM>  ::= <PARAM> <LISTA_PARAM2>
        <LISTA_PARAM2> ::= VIRGULA <LISTA_PARAM> | EPSILON
        <PARAM>        ::= TIPO ID
        <LISTA_BLOCO>  ::= <BLOCO> <LISTA_BLOCO> | EPSILON 
        <BLOCO>        ::= <ATR> | <SEL_IF>
        <ATR>          ::= ID ATRIBUICAO <VAR>
        <VAR>          ::= ID | CONST
        <SEL_IF>       ::= IF ABRE_PAR ID COMPARA ID FECHA_PAR ABRE_BLOCO <BLOCO> FECHA_BLOCO 
        Neste analisador será implementada uma matriz M de transições que vai determinar a ação do analisador
        Para isso é necessário definir os conjuntos first e follows para cada terminal e não terminal da linguagem

        Conjuntos de FIRSTs:
        --------------------------------------------------------------------------------------------------------
        First de cada terminal é ele mesmo
        First de cada não terminal é o primeiro token que aparece em cada uma de suas produções
        FIRST(P) = {DEC}
        FIRST(LISTA_PARAM) = {TIPO, EPSILON}
        FIRST(PARAM)  = {TIPO}
        FIRST(LISTA_PARAM2) = {VIRGULA, EPSILON}
        FIRST(LISTA_BLOCO) = FIRST(BLOCO) = FIRST(ATR) + FIRST(SEL_IF) {id,if,EPSILON}
        FIRST(BLOCO) = FIRST(ATR) + FIRST(SEL_IF) {id,if}
        FIRST(ATR) = {id}
        FIRST(VAR) = {id,const}
        FIRST(SEL_IF) = {if}

        Conjunto de FOLLOWs:
        --------------------------------------------------------------------------------------------------------
        Follow de um não terminal é o primeiro terminal que aparece imediatamente após ele
        $ (indica fim do arquivo) está contido no conjunto de follows do símbolo inicial
        FOLLOW(P) = {$}
        FOLLOW(LISTA_PARAM) = {FP}
        FOLLOW(LISTA_PARAM2)= {FP}
        FOLLOW(PARAM) =  {VIRGULA,FP}
        FOLLOW(LISTA_BLOCO) = {}}
        FOLLOW(BLOCO) = FIRST(LISTA_BLOCO) =  {id,if,}}
        FOLLOW(ATR) = FOLLOW(BLOCO) = {id,if,}}
        FOLLOW(SEL_IF) = FOLLOW(BLOCO) = {id,if,}}
        FOLLOW(VAR) = FOLLOW(ATR) = {id,if,}}
'''
        

class SintaticoDescendentePreditivo:

    def __init__(self, lex: Lexico):
        self.NAO_TERM = ['P','LISTA_PARAM','LISTA_PARAM2','PARAM','LISTA_BLOCO','BLOCO','ATR','VAR','SEL_IF']
        self.lexico = lex
        #matriz M        
        self.M = {
            # NÃO TERMINAL : {FIRST: [PRODUÇÃO - CADA ITEM É COLOCADO COMO UM ELEMENTO DO VETOR]}
            "P":{"DEC":['DEC','ID','ABRE_PAR','LISTA_PARAM','FECHA_PAR','ABRE_BLOCO','LISTA_BLOCO','FECHA_BLOCO']},
            "LISTA_PARAM":{"TIPO":["PARAM","LISTA_PARAM2"]},    
            "LISTA_PARAM2":{"VIRGULA":["VIRGULA","LISTA_PARAM"],"FECHA_PAR":[]}, # FP É FOLLOW DE LISTA_PARAM2
            "PARAM":{"TIPO":["TIPO","ID"]},
            "LISTA_BLOCO":{"ID":["BLOCO","LISTA_BLOCO"],"IF":["BLOCO","LISTA_BLOCO"],"FECHA_BLOCO":[]},
            "BLOCO":{"ID":["ATR"],"IF":["SEL_IF"]},
            "ATR":{"ID":["ID","ATRIBUICAO","VAR"]},
            "SEL_IF":{"IF":["IF","ABRE_PAR","ID","COMPARA","ID","FECHA_PAR","ABRE_BLOCO","BLOCO","FECHA_BLOCO"]},
            "VAR":{"ID":["ID"],"CONST":["CONST"]}
        }

    def sintatico(self):
        x = self.lexico.next_token() # lê o primeiro token da lista de tokens do léxico
        pilha = Pilha()
        pilha.empilha("$") # insere marcador de final de pilha na pilha
        pilha.empilha("P") # coloca o símbolo inicial da gramática no topo da pilha

        while x is not None: # enquanto tem tokens para ler ...
            try:
                print("Topo da pilha: "+pilha.topo() + ", Tk: "+x.token)
                if (pilha.topo() not in self.NAO_TERM):  # verifica se o topo da pilha é um terminal
                    if pilha.topo() == x.token:            # verifica se o topo é igual a entrada
                        print("## desempilha("+pilha.topo()+")")
                        pilha.desempilha()               # desempilha o terminal
                        x = self.lexico.next_token()     # avança o ponteiro da entrada
                        print("## Avança o ponteiro da entrada: "+str(x))
                    else:
                        raise Exception('Token inválido.')
                else: # se é um não terminal
                    print("# busca produção: self.M["+pilha.topo()+"]["+x.token+"]")
                    producao = self.M[pilha.topo()][x.token]   # busca produção na tabela M
                    print("desempilha o topo:"+pilha.topo())
                    pilha.desempilha()                 # desempilha o topo
                    for it in reversed(producao):      # empilha a produção
                        pilha.empilha(it)
                    print('Pilha:'+str(pilha))
            except Exception as e:
                print("Erro sintático. Topo Pilha: "+pilha.topo()+". Token: "+x.token+'. Erro: '+str(e))
                print('Pilha: '+str(pilha))
                break

        if pilha.topo() == "$":
            print('Linguagem aceita') 
        else:
            print('Linguagem não aceita')
