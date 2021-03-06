import cv2
import os
import numpy as np

class Treinamento:
    def TreinamentoFace(self):
        eigenface = cv2.face.EigenFaceRecognizer_create()
        fisherface = cv2.face.FisherFaceRecognizer_create()
        lbph = cv2.face.LBPHFaceRecognizer_create()
        def getImagemid(self):
            caminhos = [os.path.join('fotos' ,f) for f in os.listdir('fotos')]
            faces = []
            ids =[]
            for caminhoImagem in caminhos:
                imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
                id= int(os.path.split(caminhoImagem)[-1].split('.')[1])
                ids.append(id)
                faces.append(imagemFace)
            return np.array(ids), faces
        ids, faces = getImagemid(self)

        print("Treinando...")
        eigenface.train(faces, ids)
        eigenface.write('classificadorEigenYale.yml')

        lbph.train(faces, ids)
        lbph.write('classificadorLBPHYale.yml')

        print("Treinamento realizado")




