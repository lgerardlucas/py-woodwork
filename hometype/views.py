from django.shortcuts import render

# Create your views here.
def new_hometype(request):
    context = {
        'title':'NEW'
    }
    return render(request, 'new_hometype.html', context)

