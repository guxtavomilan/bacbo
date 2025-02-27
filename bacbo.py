        
import random as rd
import matplotlib.pyplot as plt

banca = 0
bi = 0
lista_vencedor = []
x = 0
y= 0


def logica(banca, bi, lista_vencedor, x, y):

    plt.ion()  # Ativa o modo interativo do Matplotlib
    fig, ax = plt.subplots()
    line_r, = ax.plot([], [], 'or', label="Vermelho")  # Vermelho
    line_b, = ax.plot([], [], 'ob', label="Azul")  # Azul
    line_g, = ax.plot([], [], 'og', label="Empate")  # Empate
    
    ax.set_xlabel("Alteração de resultado")
    ax.set_ylabel("Acúmulo de vitórias")
    ax.set_title("Gráfico Acumulativo de Resultados")
    ax.grid(True)
    plt.legend()

    x_data, y_data_r, y_data_b, y_data_g = [], [], [], []

    while banca > 0 and banca < (bi*2): #limite minimo e maximo da banca, condição de parada
    
        joga = input("quer entrar?(SIM ou NÃO)") #se sim, continua o jogo
        if joga.lower() == ("sim") or joga.lower() == ("s"): #.lower() transforma tudo em letra minuscula, para aceitar diferentes respostas que significam a mesma coisa

            v = float(input("aposta no vermelho: "))
            a = float(input("aposta no azul: "))
            e = float(input("aposta no empate: "))
            
            aposta = a + v + e

            if aposta > banca: #limitar aposta máxima ao valor da banca
                print("erro, saldo insuficiente")
                break

            banca = banca - aposta
            print("APOSTA DE: ", a + v + e, "saldo atualizado para:", banca)

            #VERMELHO
            
            d1v = rd.choice([1,2,3,4,5,6]) #dado vermelho 1
            d2v = rd.choice([1,2,3,4,5,6]) #dado vermelho 2
            
            dv = d1v + d2v

            print("DADOS VERMELHOS: ", d1v, d2v, dv) #soma dos dados vermelhos
            #dv = int(input("soma do vermelho = ")) #para testar

            #AZUL
            
            d1a = rd.choice([1,2,3,4,5,6]) #dado azul 1
            d2a = rd.choice([1,2,3,4,5,6]) #dado azul 2
            
            da = d1a + d2a

            print("DADOS AZUIS: ", d1a, d2a, da) #soma dos dados vermelhos
            #da = int(input("soma do azul = ")) #para testar


            #de acordo com o sorteio, define novo valor para cada aposta

            if da < dv:
                vencedor = "vermelho"
                v = v + v
                a = 0
                e = 0

            elif dv < da:
                vencedor = "azul"
                a = a + a
                v = 0
                e = 0

            else:
                vencedor = "empate"
                a = a - (0.1*a) #perde só 10% da aposta
                v = v - (0.1*v) #perde só 10% da aposta

                #valor de cada empate
                if dv + da == 4 or dv + da == 24:
                    e = e * 88
                    print(" 88X ")
                elif dv + da == 6 or dv + da == 22:
                    e = e * 25
                    print(" 25X ")
                elif dv + da == 8 or dv + da == 20:
                    e = e * 10
                    print(" 10X ")
                elif dv + da == 10 or dv + da == 18:
                    e = e * 6
                    print(" 06X ")
                else:
                    e = e * 4
                    print(" 04X ")

            print(vencedor, "vencedor")
            lista_vencedor.append(vencedor) #armazena para o histórico das rodadas
            print(lista_vencedor)

            anterior = len(lista_vencedor) - 1 #coleta a posição do vencedor anterior na lista
            anterior = len(lista_vencedor) - 2 if len(lista_vencedor) > 1 else None
            
            if anterior is not None and (lista_vencedor[anterior] == vencedor) or (vencedor == "empate"):
                y += 1
            else:
                x += 1
                y = 1

            x_data.append(x)
            
            if vencedor == "vermelho":
                y_data_r.append(y)
                y_data_b.append(None)
                y_data_g.append(None)
                line_r.set_data(x_data, [y if y is not None else 0 for y in y_data_r])
            elif vencedor == "azul":
                y_data_r.append(None)
                y_data_b.append(y)
                y_data_g.append(None)
                line_b.set_data(x_data, [y if y is not None else 0 for y in y_data_b])
            else:
                y_data_r.append(None)
                y_data_b.append(None)
                y_data_g.append(y)
                line_g.set_data(x_data, [y if y is not None else 0 for y in y_data_g])


             # Atualiza os dados das linhas no gráfico
            
            
            
            
            ax.relim()
            ax.autoscale_view()
            plt.draw()
            plt.pause(0.1)  # Pequena pausa para atualizar a interface gráfica       
     
        elif joga.lower() == ("não") or joga.lower() == ("n"):
            break
        else:
            print("caractere não identificado.")

    
    return(banca)