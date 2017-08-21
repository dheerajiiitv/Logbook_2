from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^view/$',views.past_entry,name='past_entry'),
    url(r'^add/$',views.new_entry,name='new_entry'),
    url(r'^add_student',views.add_student,name='add_student'),
    ]
