
from lexico import Lexico
from pilha import Pilha
'''

Analisador SLR - Simple LR parser
Gramática:
<P>           ::= DEC ID ABRE_PAR <LISTA_PARAM> FECHA_PAR ABRE_BLOCO <LISTA_BLOCO> FECHA_BLOCO;
<LISTA_PARAM> ::= VIRGULA <PARAM> | <PARAM><LISTA_PARAM> | î ;
<PARAM>       ::= TIPO ID;
<LISTA_BLOCO> ::= <BLOCO> <LISTA_BLOCO> | î;
<BLOCO>       ::= <ATR> | <SEL_IF>;
<ATR>         ::= ID ATRIBUICAO <VAR> PV;
<VAR>         ::= ID | CONST;
<SEL_IF>      ::= IF ABRE_PAR ID COMPARA ID FECHA_PAR ABRE_BLOCO <BLOCO> FECHA_BLOCO;
====================================================================================================
Conjunto de FIRST

FIRST(P) : {DEC}
FIRST(LISTA_PARAM) : {VIRGULA, TIPO, EPSILON}
FIRST(PARAM) : {TIPO}
FIRST(LISTA_BLOCO) : {ID, IF, EPSILON}
FIRST(BLOCO): {ID, IF}
FIRST(ATR): ID
FIRST(SEL_IF): {IF}
FIRST(VAR): {ID, CONST}
FIRST(SEL_IF): {IF}

=====================================================================================================
Conjunto de FOLLOWs - serão utilizados para decidir o momento da redução

FOLLOW(P): {$}
FOLLOW(LISTA_PARAM): {FECHA_PAR}
FOLLOW(PARAM): {FECHA_PAR, VIRGULA}
FOLLOW(LISTA_BLOCO): {FECHA_BLOCO}
FOLLOW(BLOCO): {ID, IF, FECHA_BLOCO}
FOLLOW(ATR):  {ID, IF, FECHA_BLOCO}
FOLLOW(SEL_IF):  {ID, IF, FECHA_BLOCO}
FOLLOW(VAR): {PV}

'''
class SLR:
    def __init__(self) -> None:
        self.afd = {
            0:{'DEC':'S2'},
            1:{'$':'ACC'},
            2:{'ID':'S3'},
            3:{'ABRE_PAR':'S4'},
            4:{'TIPO':'S5','VIRGULA':'S8'},
            5:{'ID':'S6'},
            6:{'FECHA_PAR':'R2','VIRGULA':'R2'}, # PARAM
            7:{'FECHA_PAR':'S10'},
            8:{'TIPO':'S5'},
            9:{'VIRGULA':'S8','FECHA_PAR':'R1'},
            10:{'ABRE_BLOCO':'S11'},
            11:{'IF':'S22','ID':'S16',},
            12:{'FECHA_BLOCO':'S31'},
            13:{'ID':'S16','IF':'S22','FECHA_BLOCO':'R1'},
            14:{},
            15:{},
            16:{'ATRIBUICAO':'S17'},
            17:{'ID':'S19','CONST':'S20'},
            18:{'PV':'S21'},
            19:{'PV':'R1'},
            20:{'PV':'R1'},
            21:{'ID':'R4'}
        }

        self.goto = {
            4:{'FECHA_PAR':7,'VIRGULA':9}, # 7 LISTA_PARAM # 9 PARAM
            11:{'ID':13,'FECHA_BLOCO':'S12'},#BLOCO
            17:{'PV':18} #VAR
            
        }