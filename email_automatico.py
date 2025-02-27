
import win32com.client as win32

nome = ""
idade = ""
email = ""
login = ""
status = ""
chave = ""
pronomes =""
verifica = False

def envia(pronomes, nome, idade, email, login, status, chave, verifica):

    corpo_ele = f'''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Confirmação de Cadastro</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f9f9f9;
            }}
            .header {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                font-size: 0.9em;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Bem-vindo, {nome}!</h1>
            </div>
            <p>Olá, {nome}!</p>
            <p>Estamos felizes em confirmar seu cadastro em nossa plataforma. Aqui estão os detalhes:</p>
            <ul>
                <li><strong>Nome:</strong> {nome}</li>
                <li><strong>Idade:</strong> {idade}</li>
                <li><strong>Email:</strong> {email}</li>
                <li><strong>Login:</strong> {login}</li>
                <li><strong>Status:</strong> {status}</li>
            </ul>
            <p>Para confirmar seu cadastro, por favor, utilize o seguinte código:</p>
            <h2>{chave}</h2>
            <p>Se você não se cadastrou em nossa plataforma, por favor, ignore este e-mail.</p>
            <p>Atenciosamente,<br>Equipe de Suporte</p>
            <div class="footer">
                <p>&copy; 2025 Nossa Plataforma. Todos os direitos reservados.</p>
            </div>
        </div>
    </body>
    </html>
    '''

    corpo_ela = f'''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Confirmação de Cadastro</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f9f9f9;
            }}
            .header {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                font-size: 0.9em;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Bem-vinda, {nome}!</h1>
            </div>
            <p>Olá, {nome}!</p>
            <p>Estamos felizes em confirmar seu cadastro em nossa plataforma. Aqui estão os detalhes:</p>
            <ul>
                <li><strong>Nome:</strong> {nome}</li>
                <li><strong>Idade:</strong> {idade}</li>
                <li><strong>Email:</strong> {email}</li>
                <li><strong>Login:</strong> {login}</li>
                <li><strong>Status:</strong> {status}</li>
            </ul>
            <p>Para confirmar seu cadastro, por favor, utilize o seguinte código:</p>
            <h2>{chave}</h2>
            <p>Se você não se cadastrou em nossa plataforma, por favor, ignore este e-mail.</p>
            <p>Atenciosamente,<br>Equipe de Suporte</p>
            <div class="footer">
                <p>&copy; 2025 Nossa Plataforma. Todos os direitos reservados.</p>
            </div>
        </div>
    </body>
    </html>
    '''

    corpo_elo = f'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmação de Cadastro</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #777;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Bem-vinde, {nome}!</h1>
        </div>
        <p>Olá, {nome}!</p>
        <p>Estamos felizes em confirmar seu cadastro em nossa plataforma. Aqui estão os detalhes:</p>
        <ul>
            <li><strong>Nome:</strong> {nome}</li>
            <li><strong>Idade:</strong> {idade}</li>
            <li><strong>Email:</strong> {email}</li>
            <li><strong>Login:</strong> {login}</li>
            <li><strong>Status:</strong> {status}</li>
        </ul>
        <p>Para confirmar seu cadastro, por favor, utilize o seguinte código:</p>
        <h2>{chave}</h2>
        <p>Se você não se cadastrou em nossa plataforma, por favor, ignore este e-mail.</p>
        <p>Atenciosamente,<br>Equipe de Suporte</p>
        <div class="footer">
            <p>&copy; 2025 Nossa Plataforma. Todos os direitos reservados.</p>
        </div>
    </div>
</body>
</html>
'''   

    outlook = win32.Dispatch('outlook.application') #integração com outlook
    enviaremail = outlook.CreateItem(0) #cria uma nova mensagem via email

    enviaremail.To = f"{email}" #destino, mais de um deve ser separado por ; variaveis entre {}
    enviaremail.Subject = f"TESTE {nome}" 

    if pronomes.lower() == "ele/dele":
        html_body = corpo_ele
        p = "O"
    elif pronomes.lower() == "ela/dela":
        html_body = corpo_ela
        p = "A"
    else:
        html_body = corpo_elo
        p = "E"

    enviaremail.HTMLBody = html_body
    enviaremail.Send()

    print("CONFIRME SEU EMAIL")
    print("email de confirmação enviado")

    confirma = input("digite a chave de confirmação: ")

    if confirma == chave:
        print("BEM-VIND"+p, nome )
        verifica = True
    else:
        print("ERRO!",nome, "cadastre-se novamente.")


def teste():
        
    html_body = """\

    <html>
    <head>
        <style>
            /* Estilos gerais do corpo do e-mail */
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4; /* Cor de fundo */
                padding: 20px; /* Espaçamento interno */
            }
            
            /* Container central que envolve o conteúdo */
            .container {
                background-color: #ffffff; /* Fundo branco */
                padding: 30px;
                border-radius: 10px; /* Bordas arredondadas */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Sombra para destaque */
                max-width: 500px; /* Largura máxima do container */
                margin: auto;
                text-align: center; /* Centraliza o conteúdo */
            }
            
            /* Estilo da logo (imagem no topo) */
            .logo {
                width: 150px; /* Define o tamanho da imagem */
                margin-bottom: 20px; /* Espaçamento abaixo da logo */
            }
            
            /* Estilo do título principal */
            .title {
                color: #333; /* Cor escura para contraste */
                font-size: 22px;
                font-weight: bold;
            }
            
            /* Estilo da mensagem de boas-vindas */
            .message {
                color: #555;
                font-size: 16px;
                margin-top: 10px;
                margin-bottom: 20px;
            }
            
            /* Botão de confirmação */
            .button {
                background-color: #007bff; /* Azul padrão */
                color: white;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 5px;
                display: inline-block;
                font-size: 16px;
                font-weight: bold;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Sombra leve */
            }
            
            /* Efeito hover no botão */
            .button:hover {
                background-color: #0056b3; /* Tom mais escuro ao passar o mouse */
            }
            
            /* Rodapé do e-mail */
            .footer {
                font-size: 12px;
                color: #777;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Logo do e-mail, pode ser substituída pela logo real da empresa -->
            <img src="https://via.placeholder.com/150" alt="Logo" class="logo">
            
            <!-- Título do e-mail -->
            <p class="title">Confirmação de Cadastro</p>
            
            <!-- Mensagem para o usuário -->
            <p class="message">Obrigado por se cadastrar! Para concluir seu registro, clique no botão abaixo.</p>
            
            <!-- Botão de ação -->
            <a href="#" class="button">Confirmar Cadastro</a>
            
            <!-- Rodapé do e-mail -->
            <p class="footer">Se você não realizou este cadastro, ignore este e-mail.</p>
        </div>
    </body>
    </html>

    """

    return(html_body)

#def email():

    html_body = """
<html>
<head>
    <style>
        /* Estilos gerais do corpo do e-mail */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        
        /* Container central */
        .container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            max-width: 500px;
            margin: auto;
            text-align: center;
        }
        
        /* Cabeçalho do e-mail */
        .header {
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        
        .logo {
            width: 120px;
        }
        
        /* Título do e-mail */
        .title {
            color: #333;
            font-size: 24px;
            font-weight: bold;
        }
        
        /* Texto do corpo */
        .message {
            color: #555;
            font-size: 16px;
            margin-top: 10px;
            margin-bottom: 20px;
        }
        
        /* Código de verificação */
        .code {
            font-size: 22px;
            font-weight: bold;
            color: #ffffff;
            background-color: #007bff;
            padding: 12px 20px;
            border-radius: 5px;
            display: inline-block;
            margin-bottom: 20px;
        }
        
        /* Rodapé do e-mail */
        .footer {
            font-size: 12px;
            color: #777;
            margin-top: 20px;
            border-top: 1px solid #ddd;
            padding-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Cabeçalho -->
        <div class="header">
            <img src="https://via.placeholder.com/120" alt="Logo" class="logo">
        </div>
        
        <!-- Título -->
        <p class="title">Verifique sua conta</p>
        
        <!-- Mensagem -->
        <p class="message">Use o código abaixo para confirmar seu cadastro e ativar sua conta.</p>
        
        <!-- Código de verificação -->
        <p class="code">{chave}</p>
        
        <p class="message">Caso você não tenha solicitado este código, ignore este e-mail.</p>
        
        <!-- Rodapé -->
        <p class="footer">© 2025 Nome da Empresa. Todos os direitos reservados.</p>
    </div>
</body>
</html>

"""
    return(html_body)