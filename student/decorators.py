from django.shortcuts import redirect
def login_required_with_autologout(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('student')  # Replace 'login' with the appropriate URL name for your login view

        return view_func(request, *args, **kwargs)

    return wrapped_view
