from django.shortcuts import render,HttpResponse

# Create your views here.

def hello_django(request):
    return  HttpResponse("<h1>Hello World</h1>")

def play(request , sarki_kodu):
    sarkilar = {
        u"S01" : (u"Eminem",u"Monster"),
        u"S02" : (u"Adele", u"Bilmem ne şarkısı"),
        u"S03" : (u"Şarkıcı" , u"Şarkı")
    }

    if sarki_kodu in sarkilar.keys():
        html = u"Şarkıcı .. : {}\nŞarkı Adı .. : {}".format(
            sarkilar[sarki_kodu][0] , sarkilar[sarki_kodu][1]
        )
    else:
        html = u"Şarkı bulunamadı"

    return HttpResponse(html)