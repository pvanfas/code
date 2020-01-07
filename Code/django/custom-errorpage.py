In order to display our custom pages instead of web server's pages, we will override the Django's handlerxxx views.

In your views.py

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
    
    
Now just specify these in your urls.py as below.



handler404 = myapp.views.handler404
handler500 = myapp.views.handler500


In settings.py

You need to add your hostname in ALLOWED_HOSTS like:

ALLOWED_HOSTS = ['testsite.com', 'localhost']
