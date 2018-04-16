from django.views import generic
class HomePage(generic.TemplateView):
    template_name = 'index.html'
class TestPage(generic.TemplateView):
    template_name ='test.html'
class ThanksPage(generic.TemplateView):
    template_name = 'thanks.html'
