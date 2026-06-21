from django.shortcuts import render

def damawka_view(request):
    return render(request, 'index.html')