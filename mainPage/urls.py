from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='mainPage'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="mainPage/robots.txt", content_type='text/plain')),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name="mainPage/sitemap.xml", content_type='text/xml')),
    #url(r'^resume\.pdf$', TemplateView.as_view(template_name="mainPage/other/AidenGourleyResume.pdf", content_type='application/pdf')),
    ]