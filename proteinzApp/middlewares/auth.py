from django.shortcuts import redirect, render

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        returnUrl = request.META['PATH_INFO'] 
        print("returnUrl")
        if not request.session.get('customer_name'):
            return redirect (f'login?return_url={returnUrl}')
        response = get_response(request)
        return response

    return middleware