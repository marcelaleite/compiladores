# compiladores
 

    sintaticoDescendentePreditivo:
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
        <LISTA_BLOCO>  ::= <BLOCO> <LISTA_BLOCO> | <BLOCO> 
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
        FIRST(LISTA_PARAM) = {TIPO}
        FIRST(PARAM)  = {TIPO}
        FIRST(LISTA_PARAM2) = {VIRGULA, EPSILON}
        FIRST(LISTA_BLOCO) = FIRST(BLOCO) = FIRST(ATR) + FIRST(SEL_IF) {id,if}
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
      
