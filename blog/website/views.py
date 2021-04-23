from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

def hello_blog(request):

    lista = [
        'Django', 'Python', 'Git', 'Html',
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]

    #list_posts = Post.objects.filter()
    list_posts = Post.objects.all() # pega todos os posts do bd

    data = {
        'nome': 'Curso de Django 3', 
        'lista_tecnologias':lista, 
        'posts': list_posts
    }


    #return HttpResponse("blog")
    return render(request,'index.html', data)
    #return render(request,'indexgeral.html')