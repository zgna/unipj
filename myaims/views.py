from django.shortcuts import render

def myaims(request):
    return render(request, 'blog/myaims.html', {})
