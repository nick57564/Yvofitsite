import secrets
from django.shortcuts import render
from django.http import HttpResponse

def Home_view(request):
    # Check if the cookie_consent cookie exists
    cookie_consent = request.COOKIES.get('cookie_consent', None)
    if not cookie_consent:
        message = "No cookies are enabled yet."
    else:
        message = f"Cookie is set! Value: {cookie_consent}"

    # Render the response with the message
    return render(request, 'Home_view.html', {'message': message})


def set_random_cookie_view(request):
    # Check if the cookie_consent cookie already exists
    if request.COOKIES.get('cookie_consent'):
        return HttpResponse("Cookie already exists. No changes were made.")

    # Generate a random cookie value
    random_value = secrets.token_urlsafe(32)
    response = HttpResponse("Random 'all' cookie has been set!")
    # Set the cookie if it does not exist
    response.set_cookie("cookie_consent", f"all:{random_value}", max_age=86400 * 30)  # Cookie lasts for 30 days
    return response


def set_functional_cookie_view(request):
    # Check if the cookie_consent cookie already exists
    if request.COOKIES.get('cookie_consent'):
        return HttpResponse("Cookie already exists. No changes were made.")

    # Generate a random cookie value
    random_value = secrets.token_urlsafe(32)
    response = HttpResponse("Random 'functional' cookie has been set!")
    # Set the cookie if it does not exist
    response.set_cookie("cookie_consent", f"functional:{random_value}", max_age=86400 * 30)  # Cookie lasts for 30 days
    return response
