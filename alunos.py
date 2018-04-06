class Aluno:
    def __init__(self, nome = '', email='', ra='',celular='',desconto=0.0):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__desconto = desconto
        self.__disciplinas = []
    
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email

    def getRa(self):
        return self.__ra
    def setRa(self, ra):
        self.__ra = ra

    def getCelular(self):
        return self.__celular
    def setCelular(self, celular):
        self.__celular = celular

    def getDesconto(self):
        return self.__desconto
    def setDesconto(self, desconto):
        self.__desconto = desconto

    def getDisciplinas(self):
        temp = []
        for name in self.__disciplinas:
            temp.append(name.getName())
        return temp

    def adicionaDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
    
    
    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])



   
    def aumentaDesconto(self, desconto):
        self.__desconto__ += desconto
        
    def diminuiDesconto(self, desconto):
        self.__desconto__ -= desconto
    
   
    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += d.getCargaHoraria()
        return soma_carga
    
    def retornaValorMensalidade(self):
        valorPago = 0
        for d in self.__disciplinas:
            valorPago += d.getMensalidade()
        return valorPago - (valorPago * (self.__desconto/100))