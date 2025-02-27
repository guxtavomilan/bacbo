import win32com.client as win32
import pandas as pd
import matplotlib.pyplot as plt
import autenticador as aut
import email_automatico as email_send
import gera_chave
import bacbo

df = pd.read_csv(r"C:\\programacao\\automatizador_de_email\\usuarios2.csv")
print(df['Login'])



#df = aut.cadastrar_usuarios(df, login, senha)
verifica = False
entrou = False


while entrou == False:

    usuario = input("ENTRAR ou CADASTRAR? ")

    if usuario.lower() == "cadastrar" or usuario.lower() == "c": #CADASTRO
        
        while verifica == False:

            login = input("login: ")
            senha = input("senha ")
            df = aut.cadastrar_usuarios(df, login, senha) #cadastra e adiciona em df
            encontralinha = df[df['Login'] == login] #encontra o login e armazena a linha em login_confere

            chave = gera_chave.aleatoria()
            print(chave)

            email = encontralinha['E-mail'].iloc[0]
            pronomes = encontralinha['Pronomes'].iloc[0]
            nome = encontralinha['Nome'].iloc[0]
            status = encontralinha['Status'].iloc[0]
            nome = encontralinha['Nome'].iloc[0]
            idade = encontralinha['Data de Nascimento'].iloc[0]

            verifica = email_send.envia(pronomes, nome, idade, email, login, status, chave, verifica)
            
            
    elif usuario.lower() == "entrar" or usuario.lower() == "e": #CADASTRO
        
        entrou = aut.entrada_usuario(df)

    else:
        print("desculpe, não entendi, vocÊ quer:")


bi = 5000.00
banca = bi # valor da banca inicial
lista_vencedor = []
x = 0
y = 0
print("sua banca é:", banca)

banca = bacbo.logica(banca, bi, lista_vencedor, x, y)
print("Obrigado por jogar!")
print("saldo final: ", banca)

plt.show()