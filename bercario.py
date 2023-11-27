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
                escolha = bb.mostraBebe(bebe)
                
                
                if (escolha == len(sistema.bebe.nome)):
                    
                    bb.criaBebe(sistema)
                    
                    
                elif (escolha == len(sistema.bebe.nome)+1):
                    pass
                else:
                    bb.mostra_informação(bebe,escolha) 
         
                
            case 2:
                escolha = m.mostraMae(mae)
                    
                if (escolha == len(sistema.mae.nome)):
                    nome,endereco,telefone,data = m.criaMae()
                    m.appendmae(mae,nome,endereco,telefone,data)
                    
                    
                elif (escolha == len(sistema.mae.nome)+1):
                    pass
                else:
                    m.mostra_informação(mae,escolha)
            case 3: 
                escolha = me.mostraMedico(medico)
                    
                if (escolha == len(sistema.medico.nome)):
                    
                    nome,telefone,crm,especialidade = me.criaMedico()
                    me.appendMedico(medico,nome,telefone,crm,especialidade)
                    
                elif (escolha == len(sistema.medico.nome)+1):
                    pass
                else:
                    me.mostra_informação(medico,escolha)
            case 4:
                break
            
if __name__ == '__main__':
    
    main()