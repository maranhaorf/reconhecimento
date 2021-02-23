import cv2
import numpy as np
import pymysql
import PySimpleGUI as sg
import pymsgbox

from treinamento import Treinamento


class Captura:
    def capturarFotos(self):
        classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        classificadorOlho = cv2.CascadeClassifier("haarcascade_eye.xml")
        camera = cv2.VideoCapture(0)
        amostra = 1
        numeroAmostras = 4

        sg.theme('Topanga')      # Add some color to the window

        # Very basic window.  Return values using auto numbered keys

        layout = [
            [sg.Text('Por Favor Preencha os Dados Abaixo')],
            [sg.Text('Digite seu identificador:', size=(20, 1)), sg.InputText()],
            [sg.Text('Digite seu Nome:', size=(20, 1)), sg.InputText()],

            [sg.Submit("Enviar"), sg.Cancel("Sair")]
        ]
        window = sg.Window('Tela de Cadastro', layout, location=(200, 200), size=(600, 600), keep_on_top=True)
        while (True):
            event, values = window.Read()
            if event in (None, 'Sair'):
                break
            if event == 'Enviar':
                id =values[0]
                nome = values[1]
                break

        window.close()

        largura ,altura = 220,220

        WindowName="Captura"
        view_window = cv2.namedWindow(WindowName,cv2.WINDOW_NORMAL)
        pymsgbox.alert('T para capturar a Foto ', 'Alerta!')
        while (True):
            conectado , imagem  = camera.read(3)
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor= 1.5,
                                                            minSize=(100,100))


            for (x ,y, l, a) in facesDetectadas:


                cv2.rectangle(imagem, (x, y), (x +l, y+ a) , (0,0,255),2)
                regiao = imagem[y: y +a, x:x +l]
                regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
                olhosDectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
                for (ox, oy, ol , oa) in olhosDectados:
                    cv2.rectangle(regiao,(ox,ol), (ox + ol, oy + oa), (0,255,0),2)
                    if cv2.waitKey(1) & 0xFF == ord('t'):

                     imagemFace = cv2.resize(imagemCinza[y:y +a,x:x + l], (largura, altura))
                     cv2.imwrite("fotos/pessoa." + str(id) + "." + str(amostra) + ".jpg",imagemFace)
                     fotos =("[foto" + str(amostra) )
                     conexao = pymysql.connect(db='banco', user='root', passwd='')
                     cursor = conexao.cursor()
                     query =("INSERT INTO login (id,nome, imagem) VALUES (%s,%s,%s)")
                     args = (id, nome, fotos)
                     cursor.execute(query, args)
                     conexao.commit()
                     conexao.close()
                     amostra +=1
                     pymsgbox.alert('Foto Capturada com Sucesso', 'SUCESSO!')

            if(amostra >= numeroAmostras +1):
                break


            cv2.imshow(WindowName, imagem)
            cv2.waitKey(1)



        camera.release
        cv2.destroyWindow(WindowName)




        t = Treinamento()
        t.TreinamentoFace()



