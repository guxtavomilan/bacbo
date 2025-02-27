
import pandas as pd


def carregar_df():

   df = pd.read_csv(r"C:\\programacao\\bacbo\\automatizador_de_email\\usuarios2.csv")
   return df

#login = input("login: ")
login = ""
#senha = input("senha: ")
senha =""

def cadastrar_usuarios(df, login, senha):
    
    confirma_senha = input("confirme sua senha: ")

    if senha != confirma_senha:
        print("Erro: as senhas não coincidem!")
    else:
        nome = input("nome: ")
        idade = input("idade: ")
        pronomes = input("pronomes: ")
        email = input("email: ")
        status = input("status: ")

        #adiciona ao df
        novo_usuario = pd.DataFrame([[login, senha, nome, idade, pronomes, email, status]], columns=df.columns) #cira um dataframe com os dados do usuario
        df = pd.concat([df, novo_usuario], ignore_index=True) #joga no final da tabela
          
        #print("usuário cadastrado com sucesso!")
        
        return df


   

def entrada_usuario(df):
    
    login = input("login: ")
    
    login_confere = df[df['Login'] == login] #encontra o login e armazena a linha em login_confere
    print(login_confere)

    senha = input("senha: ")

    if not login_confere.empty: #se login_confere não for vazio
      senha_confere = login_confere['Senha'].iloc[0] == senha #iloc coleta o valor armazenado em senha para a linha em que o login foi encontrado, deoois compara com a senha
    else:
      senha_confere = False
      print("login não encontrado")

    if senha_confere == True:
      nome = login_confere['Nome'].iloc[0]
      print("BEM-VINDO DE VOLTA,", nome,"!")
      entrou = True

    else:
      print("senha incorreta")
      entrou = False
    return entrou