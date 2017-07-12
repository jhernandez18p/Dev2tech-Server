from django.shortcuts import render

# Create your views here.


def my_custom_page_not_found_view(request):
    template = 'frontend/pages/404.html'
    context = {}
    return render(request, template, context)


def my_custom_error_view(request):
    template = 'frontend/pages/500.html'
    context = {}
    return render(request, template, context)


def my_custom_permission_denied_view(request):
    template = 'frontend/pages/403.html'
    context = {}
    return render(request, template, context)


def my_custom_bad_request_view(request):
    template = 'frontend/pages/400.html'
    context = {}
    return render(request, template, context)

