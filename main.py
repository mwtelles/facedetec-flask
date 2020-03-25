import os
from flask import Flask, render_template, request
import cv2
import numpy as np
import base64

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def start_page():
    print("Start")
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']

    # Save file - Salvar arquivo
    #filename = 'static/' + file.filename 
    #file.save(filename)

    # Read image - Ler a imagem
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
    # Detect faces - Detectar rostos
    faces = detect_faces(image)

    if len(faces) == 0:
        faceDetected = False
        num_faces = 0
        to_send = ''
    else:
        faceDetected = True
        num_faces = len(faces)
        
        # Draw a rectangle - Desenhar o retangulo
        for item in faces:
            draw_rectangle(image, item['rect'])
        
        # Save - Salvar
        #cv2.imwrite(filename, image)
        
        # In memory - Armazenar
        image_content = cv2.imencode('.jpg', image)[1].tostring()
        encoded_image = base64.encodestring(image_content)
        to_send = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')

    return render_template('index.html', faceDetected=faceDetected, num_faces=num_faces, image_to_show=to_send, init=True)

# ----------------------------------------------------------------------------------
# Detect faces using OpenCV - Detectar rostos utilizando OpenCV
# ----------------------------------------------------------------------------------  
def detect_faces(img):
    '''Detect face in an image'''
    
    faces_list = []

    # Convert the test image to gray scale (opencv face detector expects gray images) - Transformar a imgem para grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load OpenCV face detector (LBP is faster) - Carregar o OpenCV face detector
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    # Detect multiscale images (some images may be closer to camera than others) - Detectar a aproximação/redução da imagem
    # result is a list of faces - resultado é a quantidade de rostos
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    # If not face detected, return empty list  - caso não exista rostos retornar vazio
    if  len(faces) == 0:
        return faces_list
    
    for i in range(0, len(faces)):
        (x, y, w, h) = faces[i]
        face_dict = {}
        face_dict['face'] = gray[y:y + w, x:x + h]
        face_dict['rect'] = faces[i]
        faces_list.append(face_dict)

    # Return the face image area and the face rectangle 
    return faces_list
# ----------------------------------------------------------------------------------
# Draw rectangle on image - Desenhar o retangulo na imagem
# according to given (x, y) coordinates and given width and heigh - apartir da orientação x e y da imagem (coordenadas enviadas de largura e altura)
# ----------------------------------------------------------------------------------
def draw_rectangle(img, rect):
    '''Draw a rectangle on the image - Desenhar o retangulo no rosto'''
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

if __name__ == "__main__":
    # Only for debugging while developing - Utilizado no debug para desenvolvimento
    app.run(host='127.0.0.1', debug=True, port=5000)