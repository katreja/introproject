from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
# Create your views here.
class HomeView(TemplateView):
    # karena inherite dari templateview maka perlu template_name
    template_name = 'home.html'

    #Method get untuk menampilkan halaman
    def get(self, request):
        first_name = "jhon"
        today = datetime.datetime.today()
        return render(request, self.template_name, {'name':first_name, 'today':today})

class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        team = ['wahyudi', 'adit', 'danu', 'alex']
        return render(request, self.template_name, {'my_team': team})

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        today = datetime.datetime.today().strftime("%A, %B %2, %Y")
        return render(request, self.template_name, {'today':today})

