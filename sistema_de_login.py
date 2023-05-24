# Cria um apelido para poder chamar o PySimpleGUI com praticidade.
import PySimpleGUI as sg

# Layout do sistema de login.
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
]

# Janela da tela do sistema de login.
window = sg.Window('Login',layout=layout)

# Loops de eventos.
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '123456'
        usuario_correto = 'João'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso!')
        else:
            window['mensagem'].update('Senha ou usuário incorreto!')
