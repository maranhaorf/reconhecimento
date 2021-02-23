import cv2
import pymysql
import pymsgbox

class Reconhecendo:
    def reconhecedorRosto(self):
        detectorFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        reconhecedor = cv2.face.EigenFaceRecognizer_create()
        reconhecedor.read('classificadorEigenYale.yml')
        largura,altura = 220,220
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        camera = cv2.VideoCapture(3)

        conexao = pymysql.connect(db='banco', user='root', passwd='')
        cursor = conexao.cursor()
        query =("Select id,nome from Login")
        cursor.execute(query)

        myresult = cursor.fetchall()

        for x in myresult:

         idbanco =x[0]
         nomebanco=x[1]
        conexao.close()
        while (True):
            conectado, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            faceDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor= 1.5, minSize=(30,30))


            for (x ,y, l, a) in faceDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y +a,x:x + l], (largura, altura))
                cv2.rectangle(imagem,(x ,y), (x+l,y + a), (0,0,255),2)
                id, confianca = reconhecedor.predict(imagemFace)
                nome =''

                if id == idbanco:
                    nome = nomebanco
                    valorboleano = 1

                else:
                    nome = 'Nao existe'
                cv2.putText(imagem, nome, (x, y + (a + 30)), font, 2, (0, 0, 255))
                nomecomparar = 'Nao existe'

                cv2.imshow("Face",imagem)
                if (valorboleano):
                    import listar
                    break

                if cv2.waitKey(1) == ord('q'):
                    break




        camera.release()
        cv2.destroyAllWindows()
