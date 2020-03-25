# Face detection demo (Flask app) - Detector Facial Demo (aplicativo em Flask)

[EN] This Flask application let's the user upload a image and detects how many (if any) faces are there in the picture. he is a simple app but its just the beginning.
My next steps is: enhance the design and create new cases. probably using the webcam.

[Pt-br] Esta aplicação em Flask proporciona o usuário o envio de imagens, sendo estas utilizadas para encontrar um ou mais rostos na imagem. Esta é uma aplicação simples mas é só o começo.
Meus próximso passos são: Melhorar o design e criar novos casos. Provavelmente utilizando a webcam.

##### Installation: - Instalação: 

`pip install opencv-contrib-python`

`pip install Flask`

`pip install gunicorn`

`pip install numpy`

[EN] if u need use pip install "library" --user

[Pt-br] Se precisar utilize pip install "biblioteca" --user

##### Add the following buildpack: - Adicione o seguinte pacote: 

https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-apt

[EN] and include a list of apt package names to be installed the `Aptfile`

[Pt-br] e inclua a lista de nomes dos pacotes para serem instalados no 'aptfile'

## Docker

Docker container based on: https://hub.docker.com/r/shosoar/alpine-python-opencv/

To build the docker image and run locally:

`cd face_detection_flask`

`docker build -t face_detection_flask .`

`docker run -it -p 3000:80 face_detection_flask`
