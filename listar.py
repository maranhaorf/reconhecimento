import PySimpleGUI as sg
import pymysql


conexao = pymysql.connect(db='banco', user='root', passwd='')
cursor = conexao.cursor()
query = ("select count(id) as numero, estado,quantidade,agrotoxico from  agro_pop")
cursor.execute(query)
valor=[]
myresult = cursor.fetchall()
for x in myresult:
    numero = x[0]
    estado = x[1]
    agrotoxico = x[3]
    quantidade = x[2]

    valor.append([estado,agrotoxico,quantidade])


sg.theme('Dark Brown 1')

header = ['Estado', 'Agrotoxico','Quantidade']

column_to_be_centered = [  [sg.Text('Agrotoxico')],
            [sg.Table(values=valor,key='_table1_',headings=header, num_rows=3)],
            [ sg.Cancel()],]
layout = [[sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
          [sg.Text('', pad=(0, 0), key='-EXPAND2-'),  # the thing that expands from left
           sg.Column(column_to_be_centered, vertical_alignment='center', justification='center', k='-C-')]]

window = sg.Window('listar', layout, resizable=True,finalize=True)
window['-C-'].expand(True, True, True)
window['-EXPAND-'].expand(True, True, True)
window['-EXPAND2-'].expand(True, False, True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()