from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class HomeView(View):
    """This View controls the main landing page for the site"""

    def get(self, request):
        context = {"user": request.user}
        return render(request, "core/index.html", context=context)
