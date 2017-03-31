from django.conf.urls import url, include
from . import views

# To load url link {% url "todolist:index" %}
app_name = "todolist"   

# Route link, need to register with project/urls
urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^add/$', views.add_task, name="add"),
	url(r'^done/$', views.done_task, name = "done"),
	url(r'^delete/(?P<task_id>\d+)/$', views.delete_task, name = "delete" )
]