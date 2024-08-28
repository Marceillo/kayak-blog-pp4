from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def about_kayaking(request):
    """
    Returns the about kayaking page and
    display relevant information.
    """

    return render(request, 'about/about.html')


def contact_us(request):
    """
    Contact form submissions allow a user to send a message.
    -if the request method is POST process the sunmit data.
    -if the form is valid it saves the data and displays a success message
     or error message if the submission failed or successful.
    - Redirecting to the kayak page.
    **Template:**
    about/contact_us.html
    about/contact_success.html
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

    return render(request, 'about/contact_us.html', {'form': form})


def contact_success(request):
    return render(request, 'about/contact_success.html')
