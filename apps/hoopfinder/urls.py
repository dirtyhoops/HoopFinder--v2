from django.conf.urls import url

from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),  
    url(r'^home$', views.home),  
    url(r'^courts$', views.courts),
    url(r'^map$', views.map),
    url(r'^users$', views.users),
    url(r'^user_dashboard$', views.userdashboard),
    url(r'^registration$', views.registration),
    url(r'^register$', views.register),
    url(r'^login_post$', views.login_post),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^new_court$', views.new_court),
    url(r'^add_court$', views.add_court),
    url(r'^review_court$', views.review_court),
    url(r'^checkin$', views.checkin),
    url(r'^courts/(?P<id>\d+)$', views.show_court),
    url(r'^user/(?P<user_id>\d+)$', views.user_page),
    url(r'^add_user_review$', views.add_user_review),
    url(r'^delete_review/(?P<id>\d+)$', views.delete_review),
    url(r'^delete_court/(?P<id>\d+)$', views.delete_court)
]  