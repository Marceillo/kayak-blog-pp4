from django.shortcuts import render, redirect
from .forms import ContactForm



# Create your views here.
def about_kayaking(request):
    return render(request,'about/about.html')

def contact_us (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('about:contact_success')
            
        else:
            form = ContactForm()
            return rendar(request, 'about/contact_success.html', {'form': form})

def contact_success(request):
    return render(request, 'about/contact_success.html') 
            
