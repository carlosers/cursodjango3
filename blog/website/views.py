from django.shortcuts import render
#from django.http import HttpResponse

def hello_blog(request):

    lista = [
        'Django', 'Python', 'Git', 'Html',
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]

    data = {'nome': 'Curso de Django 3', 'lista_tecnologias':lista}

    #return HttpResponse("blog")
    return render(request,'index.html', data)
    #return render(request,'indexgeral.html')