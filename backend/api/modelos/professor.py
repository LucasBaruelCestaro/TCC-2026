

class professor_modelo:
    def __init__(self):
        self.__id_hash = None #string
        self.__registro_professor = None #string
        self.__nome_professor = None #string
        self.__email_professor = None #string

    @property
    def id_hash(self):
        return self.__id_hash

    @id_hash.setter
    def id_hash(self, value):
        if value is None:
            raise ValueError("Id nulo")

        if not isinstance(value, str):
            raise TypeError("Id deve ser uma string")

        value = value.strip()
        self.__id = value


    @property
    def registro_professor(self):
        return self.__registro_professor

    @registro_professor.setter
    def registro_professor(self, value):
        if value is None:
            raise ValueError("Registro do professor nulo")

        if not isinstance(value, str):
            raise TypeError("Registro do professor deve ser uma string")

        value = value.strip()
        self.__registro_professor = value


    @property
    def nome_professor(self):
        return self.__nome_professor

    @nome_professor.setter
    def nome_professor(self, value):
        if value is None:
            raise ValueError("Nome do professor nulo")

        if not isinstance(value, str):
            raise TypeError("Nome do professor deve ser uma string")

        value = value.strip()
        self.__nome_professor = value


    @property
    def email_professor(self):
        return self.__email_professor

    @email_professor.setter
    def email_professor(self, value):
        if value is None:
            raise ValueError("Email do professor nulo")

        if not isinstance(value, str):
            raise TypeError("Email do professor deve ser uma string")

        value = value.strip()
        self.__email_professor = value