from PyQt5 import uic, QtWidgets
import sqlite3

def chama_segunda_tela():
#PEGANDO DADOS DA TELA
    primeira_tela.info.setText(" ")
    nome_usuario = primeira_tela.usuario.text()
    senha = primeira_tela.senha.text()

#CONECTANDO AO BANCO E PESQUIZANDO
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login ='{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        banco.close()
    except:
        print("erro ao validar login")

    if senha == senha_bd[0][0]:
        primeira_tela.close()
        segunda_tela.show()
    else:
        primeira_tela.info.setText("Dados de login incorretos!")

def logout():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()



def cadastrar():
    nome = tela_cadastro.cadNome.text()
    login = tela_cadastro.cadLogin.text()
    senha = tela_cadastro.cadSenha.text()
    c_senha = tela_cadastro.cadConfSenha.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "')")

            banco.commit()
            banco.close()
            tela_cadastro.cadLblInfo.setText("Usuario cadastrado com sucesso")

            nome.setText(" ")
            login.setText(" ")
            senha.setText(" ")
            c_senha.setText(" ")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
    else:
        tela_cadastro.cadLblInfo.setText("As senhas digitadas estão diferentes")


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("tela1.ui")
segunda_tela = uic.loadUi("tela2.ui")
tela_cadastro = uic.loadUi("cadastro.ui")
primeira_tela.login.clicked.connect(chama_segunda_tela)
primeira_tela.btnHomeCadastrar.clicked.connect(abre_tela_cadastro)
segunda_tela.logout.clicked.connect(logout)
primeira_tela.senha.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.cadBtnCadastrar.clicked.connect(cadastrar)



primeira_tela.show()
app.exec()