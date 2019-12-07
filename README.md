# HowTo

API que simula o comportamento do site WikiHow Django Rest Framework.

How To é um projeto que tem o intuito de criar tutoriais para tudo, desde escovar os dentes à como ficar rico. Projeto desenvolvido para avaliação da disciplina de programação para a internet 2, ministrada por Ely da Silva Miranda.

## Devs

<h3><a href="https://github.com/PauloVilarinho">Paulo Vilarinho</a></h3>

<h3><a href="https://github.com/xispituao">Natanael Silva</a></h3>

## Requisitos
 - Django==2.2.7
 - django-crispy-forms==1.8.1
 - django-filter==2.2.0
 - django-rest-swagger==2.1.2
 - djangorestframework==3.10.3
 - djangorestframework-jwt==1.11.0
 - djangorestframework-simplejwt==4.3.0


## Acompanhe a apresentação do desenvolvimento com o sistema rodando no seu computador.

Antes de iniciar a instalação certifique-se de que possui o python>=3.5 instalado no seu computador.

### Instalação da aplicação
 - Faça o clone ou o download do projeto do github no seu computador.
 - instale os requerimentos necessários para rodar a aplicação com o comando: pip install -r requirements.txt
 - realize as migrações com o comando: python manage.py migrate
 - crie um super usuário utilizando o comando: python manage.py createsuperuser
 - e finalmente inicialize o servidor com o comando: python manage.py runserver


## Modelagem do projeto
```json

Categorie {
  "title":"",
  "description":"",
}

User {
  "username":"",
  "password":"",
  "email":"",
}

Post {
  "title":"",
  "description":"",  
  "categorie":Categorie(),
  "owner":User(),
}

Part {
  "title":"",
  "post":Post(),
}

Step {
  "title":"",
  "description":"",  
  "part":Part(),
}

Comment {
  "text":"",
  "owner":User(),  
  "post":Post(),

}

```
