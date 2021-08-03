# from django.urls import path
# from django.views.generic import TemplateView
#
# app_name = 'articleapp'
#
# urlpatterns = [
#     path('list/', TemplateView.as_view(templatesname='article/list.html'), name='list')
# ]

from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')
]

