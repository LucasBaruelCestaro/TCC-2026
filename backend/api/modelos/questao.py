import professor

class questao_modelo:
    def __init__(self):

        self.__id_questao = None
        self.__professor = None   #id do professor que cadastrou a questão no sistema
        self.__assunto = None
        self.__disciplina = None
        self.__palavras_chave = None
        self.__tipo_questao = None   #se é objetiva ou dissertativa
        self.__dificuldade = None 
        self.__autor = None   #Ex: Professor, Universidades, etc.
        self.__alternativas = None
        self.__alternativa_correta = None 

    #GET/SET ID DA QUESTÃO
    @property
    def id_questao(self):
        return self.__id_questao
    
    @id_questao.setter
    def id_questao(self,value):
        if value is None:
            raise ValueError("ID questão nulo")
        
        if not isinstance(value, int):
            raise TypeError("ID questão deve ser int")
        
        if value <= 0:
            raise ValueError("Id deve ser um número maior que zero")
        
        self.__id_questao = value

    
    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, value):
        if not isinstance(value, professor):
            raise ValueError("Professor deve ser uma instância válida")
        self.__professor = value

    #GET/SET ASSUNTO
    @property
    def assunto(self):
        return self.__assunto
    
    @assunto.setter
    def assunto(self,value):
        if value is None:
            raise ValueError("Assunto nulo")
        
        if not isinstance(value, str):
            raise TypeError("Assunto deve ser uma string")
        value = value.strip().title()
        
        if len(value) < 2:
            raise ValueError("Assunto deve ter mais de 2 caracteres")
        
        if value.isnumeric:
            raise ValueError("Assunto não pode conter apenas números")
        self.__assunto = value

    
    #GET/SET DISCIPLINA
    @property
    def disciplina(self):
        return self.__disciplina
    
    @disciplina.setter
    def disciplina(self,value):
        if value is None:
            raise ValueError("Disciplina(as) nula")
        
        if not isinstance(value, list):
            raise TypeError("Diciplina(as) devem ser uma lista")

        value = [disciplina.strip().lower() for disciplina in value]

        for disciplina in value:
            if not isinstance(disciplina, str):
                raise TypeError("Cada disciplina deve ser uma string")

            if len(disciplina) < 2:
                raise ValueError("Disciplina muito curta")
            
            if disciplina.isnumeric():
                raise ValueError("Disciplina deve conter letras")
        
        self.__disciplina = value

    #GET/SET PALAVRAS-CHAVE
    @property
    def palavras_chave(self):
        return self.__palavras_chave
    
    @palavras_chave.setter
    def palavras_chave(self,value):
        if value is None:
            raise ValueError("Palavra(as) chave nula")
        
        if not isinstance(value, list):
            raise TypeError("Palavras-chave devem ser uma lista")
        
        value = [palavra.strip().lower() for palavra in value]

        for palavra in value:
            if not isinstance(palavra, str):
                raise TypeError("Cada palavra-chave deve ser uma string")

            if len(palavra) < 3:
                raise ValueError("Palavra-chave muito curta")
            
            if palavra.isnumeric():
                raise ValueError("Palavra-chave deve conter letras")
        
        self.__palavras_chave = value

    #GET/SET TIPO DA QUESTÃO
    @property
    def tipo_questao(self):
        return self.__tipo_questao
    
    @tipo_questao.setter
    def tipo_questao(self,value):
        if value is None:
            raise ValueError("Tipo da questão nulo")
        
        if not isinstance(value,str):
            raise TypeError("Tipo da questão deve ser string")
        
        value = value.strip().title()

        if value not in ["Objetiva","Dissertativa"]:
            raise ValueError('Tipo da questão inválido')
        
        self.__tipo_questao = value

    #GET/SET DIFICULDADE
    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, value):
        if value is None:
            raise ValueError("Dificuldade nula")
        
        if not isinstance(value, str):
            raise TypeError("Dificuldade deve ser str")
        
        value = value.strip().title()

        if value not in ["Fácil","Médio","Difícil"]:
            raise ValueError ("Dificuldade inválida")
        
        self.__dificuldade = value


    #GET/SET AUTOR
    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, value):
        if value is None:
            raise ValueError("Autor nulo")
        
        if not isinstance(value, str):
            raise TypeError("Autor deve ser str")
        
        value = value.strip()

        if len(value) < 3:
            raise ValueError("Autor deve conter mais de 3 caracteres")
        
        if value.isnumeric:
            raise ValueError("Autor não pode conter apenas números")
        
        self.__autor = value


    #GET/SET ALTERNATIVAS
    @property
    def alternativas(self):
        return self.__alternativas

    @alternativas.setter
    def alternativas(self, value):
        if self.tipo_questao == "Objetiva":
            if value is None:
                raise ValueError("Alternativas nula")
            
            if not isinstance(value, list):
                raise TypeError("Alternativas deve ser list")
            
            value = [alternativa.strip() for alternativa in value]

        self.__alternativas = value


    #GET/SET ALTERNATIVA CORRETA
    @property
    def alternativa_correta(self):
        return self.__correta

    @alternativa_correta.setter
    def correta(self, value):
        if value is None:
            raise ValueError("Correta nula")
        
        if not isinstance(value, str):
            raise TypeError("Correta deve ser str")
        value = value.strip()
        
        self.__correta = value
            
        
                