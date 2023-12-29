from django.urls import path, include
from django.views.generic import TemplateView
from .views import HomeView, post_single
app_name = 'blog'
urlpatterns = [

    #直接导航到html 不需要backend code
    path('base/', TemplateView.as_view(template_name = "base/base.html")),
    path('', HomeView.as_view(), name="homepage"),
    path('<slug:post>/',post_single, name='post_single')
    # path('base', ),
]

 
