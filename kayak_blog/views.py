from django.shortcuts import render

"""
**Functionality**:
Return renders a custom 404 error page when link is not found.
"""
def handler404(request, exception):
    # 404 error handler
    return render(request, 'errors/404.html', status=404)

"""
**Functionality**:
Return renders a custom 500 server error occurs.
"""
def handler500(request):
    # 500 error handler
    return render(request, 'errors/500.html', status=500)