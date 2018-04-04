from django.shortcuts import render
from django.http import HttpResponse
from .models import UrlModel
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def mainPage(request):
    if request.method == "GET":
        urlList = UrlModel.objects.all()
        group = ''
        for url in urlList:
            link = "localhost:1234/" + str(url.id)
            group = (group + '<b>URL</b>: '
            '<a href=' + url.longUrl + '>' + url.longUrl + '</a>'
            ' <b>URL corta</b>: '
            '<a href=' + url.longUrl + '>' + link + '</a><br>')
        return HttpResponse(
        '<html>'
            '<body>'
                '<h2>Acortar URLs:</h2>'
                '<form action="/" method="post">'
                    '<input type="text" name="URL" value="Introduce la URL">'
                    '<input type="submit" value="Acortar">'
                '</form>'
                '<h2>Lista de URLs acortadas:</h2>' +
                group +
            '</body>'
        '</html>', status=200)
    elif request.method == "POST":
        url = request.POST['URL']
        print("HOLA")
        if url != '':
            if not url.startswith('http://') and not url.startswith('https://'):
                url = "http://" + url
            try:
                shortUrl = UrlModel.objects.get(longUrl = url).id
                link = "localhost:1234/" + str(shortUrl)
            except UrlModel.DoesNotExist:
                shortUrl = UrlModel(longUrl = url)
                shortUrl.save()
                shortUrl = shortUrl.id
                link = "localhost:1234/" + str(shortUrl)
            return HttpResponse(
            '<html>'
                '<body>'
                    '<h2>Correspondencia:</h2>'
                    '<b>URL</b>: ' +
                    '<a href=' + url + '>' + url + '</a>'
                    ' <b>URL Corta</b>: '
                    '<a href=' + url + '>' + link + '</a>'
                '</body>'
            '</html>', status=200)
        else:
            return HttpResponse("404: Not Found", status=404)
    else:
        return HttpResponse("404: Not Found", status=404)

def redirection(request, shortUrl):
    try:
        longUrl = UrlModel.objects.get(id = shortUrl).longUrl
        return HttpResponse(
        '<html>'
            '<head><meta http-equiv="Refresh" content=' + "3;url=" + longUrl + '></head>'
            '<body><h2>Te estamos redirigiendo...</h2></body>'
        '</html>', status=302)
    except UrlModel.DoesNotExist:
        return HttpResponse("404: Not Found", status=404)
