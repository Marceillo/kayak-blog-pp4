from django.shortcuts import render


def handler404(request, exception):
    """
    **Functionality**:
    Return renders a custom 404 error page when link is not found.
    """
    # 404 error handler
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """
    **Functionality**:
    Return renders a custom 500 server error occurs.
    """
    # 500 error handler
    return render(request, 'errors/500.html', status=500)
