from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.common import no_append_slash
from django.utils.decorators import method_decorator

@login_required(login_url="/accounts/login/", redirect_field_name="/")
def dashboard(request):
    return render(request, 'index.html')