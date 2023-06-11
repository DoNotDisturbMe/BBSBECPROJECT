from django.contrib.auth import logout
from datetime import timezone
class AutoLogoutMiddleware:
    def __init__(self, get_response, timeout_minutes=1):
        self.get_response = get_response
        self.timeout_minutes = timeout_minutes

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')

            if last_activity and (timezone.now() - last_activity).seconds // 60 >= self.timeout_minutes:
                logout(request)
                del request.session['last_activity']

            request.session['last_activity'] = timezone.now(),

        response = self.get_response(request)
        return response
