from django.shortcuts import ( get_object_or_404, render, redirect )

def get_lang(request):
    lang_code = 'es'
    
    if request.method == "POST":
        if 'lang_code' in request.COOKIES:
            lang_code = request.COOKIES['lang_code']
    else:
        lang_ = 'Spanish'
        lang_code = 'es'
        render = redirect('es:inicio')
        render.set_cookie('lang_code', lang_code)
        render.set_cookie('lang_', lang_)
    return lang_code