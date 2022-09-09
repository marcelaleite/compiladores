class Token:
    def __init__(self, token, lexema, posini, posfim):
        self.token = token
        self.lexema = lexema
        self.posini = posini
        self.posfim = posfim

    def __str__(self) -> str:
        return '<'+self.token + ','+self.lexema+'>'