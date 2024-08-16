from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages



# Create your views here.
def about_kayaking(request):
    return render(request,'about/about.html')

def contact_us(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been received successfully!')

            return redirect('contact_us')
        else:
            form = ContactForm()
               

    return render(request, 'about/contact_us.html', {'form': form}) 

def contact_success(request):
    return render(request, 'about/contact_success.html')