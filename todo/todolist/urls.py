from django.conf.urls import url, include
from . import views

# To load url link {% url "todolist:index" %}
app_name = "todolist"   

# Route link, need to register with project/urls
urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^add/$', views.add_task, name="add")
]