from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def about_kayaking(request):
    """
    Returns the about kayaking page and
    display relevant information.
    """

    return render(request, 'about/about.html')


def contact_kayaker(request):
    """
    Allows a user to get in touch with the blog.
    Using a form the user send a message with their details.
    about/contact_kayaker.html template used.
    """
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been received successfully!')

            return redirect('about_kayaking')
        else:
            messages.error(request, 'Error submitting your message.')
            # form = ContactForm()

    return render(request, 'about/contact_kayaker.html', {'form': form})


def contact_success(request):
    return render(request, 'about/contact_success.html')
