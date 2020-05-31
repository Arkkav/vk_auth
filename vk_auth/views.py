from django.shortcuts import redirect


def redirect_blog(request):
    return redirect('/auth_app/', permanent=False)