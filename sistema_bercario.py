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

  
    
    


class bebe:
    def __init__(self, nome, data, peso, altura, mae, medico):
        self.nome = nome
        self.data = data
        self.peso = peso
        self.altura = altura
        self.mae = mae
        self.medico = medico
        
    def mostraBebe(self):
        
            escolha = 0
            if len(self.nome) == 0:
                print('Não a nenhum bebe no sistema')
            
            for i in range (len(self.nome)):
                print(f'{i+1}){self.nome[i]}')
            print(f'{len(self.nome)+1})Adicionar bebe:')    
            print(f'{len(self.nome)+2})voltar')    
            
            while escolha <1 or escolha > len(self.nome)+2:
                escolha = SistemaBerco.Onlyint("==>")
            escolha -=1
            return escolha
        
    def appendBebe(self,nome,data,peso,altura,mãe,medic):
        self.nome.append(nome)
        self.data.append(data)
        self.peso.append(peso)
        self.altura.append(altura)
        self.mae.append(mãe)
        self.medico.append(medic)
        
    def criaBebe(self):
        escolha = 0
        nome_bebe = input("digite o nome do bebe:")
        data_bebe = input("digite a data de nascimento do bebe:")
        peso = input("digite o peso do bebe:")
        altura = input("digite a altura do bebe:")
        
        if len(self.mae.nome) == 0:
            print('Não a nenhuma mãe no sistema, adicione ela')
        else:
            print('selecione a mãe do bebe,caso não esteve no sistema adicione ela')
        for i in range (len(self.mae.nome)):
            print(f'{i+1}){self.mae.nome[i]}')
        print(f'{len(self.mae.nome)+1})Adicionar mãe:')    
        
        while escolha <1 or escolha > len(self.mae.nome)+1:
            escolha = SistemaBerco.Onlyint("==>")
        escolha -=1
        if escolha == len(self.mae.nome):
            nome,endereco,telefone,data = mae.criaMae()
            mae.appendmae(self.mae,nome,endereco,telefone,data) 
        
        mãe = self.mae.nome[escolha]

        escolha = 0
        
        
        if len(self.medico.nome) == 0:
            print('Não a nenhum medico no sistema, adicione o medico no sistema')
        else:
            ('selecione o medico do bebe,caso não esteve no sistema adicione o')
        for i in range (len(self.medico.nome)):
            print(f'{i+1}){self.medico.nome[i]}')
        print(f'{len(self.medico.nome)+1})Adicionar medico')     
        
        while escolha <1 or escolha > len(self.medico.nome)+1:
            escolha = SistemaBerco.Onlyint("==>")
        escolha -=1
        if (escolha == len(self.medico.nome)):
                    
            nome,telefone,crm,especialidade = medico.criaMedico()
            medico.appendMedico(self.medico,nome,telefone,crm,especialidade)
        medic = self.medico.nome[escolha]

        bebe.appendBebe(self.bebe,nome_bebe,data_bebe,peso,altura,mãe,medic)

    def mostra_informação(self,escolha):
        print('nome:',self.nome[escolha])
        print('data de nascimento:',self.data[escolha])
        print('peso:',self.peso[escolha])
        print('mãe:',self.mae[escolha])
        print('medico:',self.medico[escolha])
        
        input('enter para continuar')



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
        
    def mostraMae(self):
        escolha = 0
        print(len(self.nome))
        if len(self.nome) == 0:
            print('Não a nenhuma mâe no sistema')
            
        for i in range (len(self.nome)):
            print(f'{i+1}){self.nome[i]}')
        print(f'{len(self.nome)+1})Adicionar mãe:')    
        print(f'{len(self.nome)+2})voltar')    
        
        while escolha <1 or escolha > len(self.nome)+2:
            escolha = SistemaBerco.Onlyint("==>")
        escolha -=1
        return escolha
    
    def criaMae():
        nome = input("digite o nome da mãe:")
        endereco = input("digite o endereço da mãe:")
        telefone = input("digite o telefone da mãe:")
        data = input("digite a data da mãe:")

        return nome, endereco, telefone, data

    def appendmae(self,nome,endereco,telefone,data):
        self.nome.append(nome)
        self.endereco.append(endereco)
        self.telefone.append(telefone)
        self.data.append(data)

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
    
    def appendMedico(self,nome, telefone, CRM, especialidade):
        
        self.nome.append(nome)
        self.telefone.append(telefone)
        self.CRM.append(CRM)
        self.especialidade.append(especialidade)        

    def mostraMedico(self):
        escolha = 0
        print(len(self.nome))
        if len(self.nome) == 0:
            print('Não a nenhum medico no sistema')
            
        for i in range (len(self.nome)):
            print(f'{i+1}){self.nome[i]}')
        print(f'{len(self.nome)+1})Adicionar medico')    
        print(f'{len(self.nome)+2})voltar')    
        
        while escolha <1 or escolha > len(self.nome)+2:
            escolha = SistemaBerco.Onlyint("==>")
        escolha -=1
        return escolha  
