class SistemaBerco:
    def __init__(self, bebe, mae, medico):
        self.bebe = bebe
        self.mae = mae
        self.medico = medico

    def set_bebe(self,bebe):
        self.bebe = bebe
    def set_mae(self,mae):
        self.mae = mae
    def set_medico(self,medico):
        self.medico = medico



    def Onlyint(texto):
        valor = ""
        while type(valor) != int:
            try:
                valor = int(input(texto))
            except:
                print('digite algo valido')
        return valor

    def oqueFara():
        valor = 0
        print(
            "Oque voce que fazer\n1)ver/adicionar bebes \n2)ver/adicionar mães\n3)ver/adicionar medicos\n4)Sair do sistema"
        )
        while valor < 1 or valor > 4:
            valor = SistemaBerco.Onlyint("==>")

        return valor

    def mostraBebes(self):
        print(self.bebe.nome[0])
    
    def mostraMedico(self):
        escolha = 0
        print(len(self.medico.nome))
        if len(self.medico.nome) == 0:
            print('Não a nenhum medico no sistema')
            
        for i in range (len(self.medico.nome)):
            print(f'{i+1}){self.medico.nome[i]}')
        print(f'{len(self.medico.nome)+1})Adicionar medico')    
        print(f'{len(self.medico.nome)+2})voltar')    
        
        while escolha <1 or escolha > len(self.medico.nome)+2:
            escolha = SistemaBerco.Onlyint("==>")
        escolha -=1
        return escolha
    
    def mostraMae(self):
        escolha = 0
        print(len(self.mae.nome))
        if len(self.mae.nome) == 0:
            print('Não a nenhuma mâe no sistema')
            
        for i in range (len(self.mae.nome)):
            print(f'{i+1}){self.mae.nome[i]}')
        print(f'{len(self.mae.nome)+1})Adicionar mae')    
        print(f'{len(self.mae.nome)+2})voltar')    
        
        while escolha <1 or escolha > len(self.medico.nome)+2:
            escolha = SistemaBerco.Onlyint("==>")
        escolha -=1
        return escolha


class bebe:
    def __init__(self, nome, data, peso, altura, mae, medico):
        self.nome = nome
        self.data = data
        self.peso = peso
        self.altura = altura
        self.mae = mae
        self.medico = medico


class mae:
    def __init__(self, nome, endereco, telefone, data):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.data = data
        
    def mostra_informação(self,escolha):
        print('nome:',self.nome[escolha])
        print('endereço:',self.endereco[escolha])
        print('telefone:',self.telefone[escolha])
        print('data de nascimento:',self.data[escolha])
        
        input('enter para continuar')
        
    def criaMae():
        nome = input("digite o nome da mãe:")
        endereco = input("digite o endereço da mãe:")
        telefone = input("digite o telefone da mãe:")
        data = input("digite a data da mãe:")

        return nome, endereco, telefone, data

class medico:
    def __init__(self, nome, telefone, CRM, especialidade):
        self.nome = nome
        self.telefone = telefone
        self.CRM = CRM
        self.especialidade = especialidade
        
    def mostra_informação(self,escolha):
        print('nome:',self.nome[escolha])
        print('telefone:',self.telefone[escolha])
        print('CRM:',self.CRM[escolha])
        print('especialidade:',self.especialidade[escolha])
        input('enter para continuar')
        
    def criaMedico():
        nome = input("digite o nome do medico:")
        telefone = input("digite o telefone do medico:")
        CRM = input("digite o CRM do medico:")
        especialidade = input("digite a especialidade do medico:")

        return nome, telefone, CRM, especialidade

