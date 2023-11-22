from sistema_bercario import SistemaBerco as sb
from sistema_bercario import bebe as bb
from sistema_bercario import medico as me
from sistema_bercario import mae as m


def main():
    
    medico = me([],[],[],[])
    mae = m ([],[],[],[])
    bebe = bb ([],[],[],[],[],[])
    sistema = sb(bebe,mae,medico)
    
    
    
    while True:
        escolha = sb.oqueFara()
        match escolha:
            case 1:
                sb.mostraBebes()
            case 2:
                escolha = sb.mostraMae(sistema)
                    
                if (escolha == len(sistema.mae.nome)):
                    nome,endereco,telefone,data = m.criaMae()
                    mae.nome.append(nome)
                    mae.endereco.append(endereco)
                    mae.telefone.append(telefone)
                    mae.data.append(data)
                elif (escolha == len(sistema.mae.nome)+1):
                    pass
                else:
                    m.mostra_informação(mae,escolha)
            case 3: 
                escolha = sb.mostraMedico(sistema)
                    
                if (escolha == len(sistema.medico.nome)):
                    nome,telefone, crm,especialidade = me.criaMedico()
                    medico.nome.append(nome)
                    medico.telefone.append(telefone)
                    medico.CRM.append(crm)
                    medico.especialidade.append(especialidade)
                elif (escolha == len(sistema.medico.nome)+1):
                    pass
                else:
                    me.mostra_informação(medico,escolha)
            case 4:
                break

        
        


        
    
    
if __name__ == '__main__':
    
    main()