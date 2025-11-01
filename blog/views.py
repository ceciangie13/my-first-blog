from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {}) #función render que reproduce (construye) nuestra plantilla blog/post_list.html.