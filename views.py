from django.shortcuts import render   # ✅ ADD THIS

from django.http import HttpResponse

def cv(request):
    return render(render,"cv.html")