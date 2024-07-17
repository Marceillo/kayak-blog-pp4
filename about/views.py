from django.shortcuts import render



# Create your views here.
def about_kayaking(request):
    return render(request,'about/about.html')