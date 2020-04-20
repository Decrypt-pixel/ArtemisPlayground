from django.urls import path, include
from . import views  #import everything from views module
from django.conf import settings
from django.conf.urls.static import static

#iserrano0
app_name = 'share'
urlpatterns = [
    path('',views.index, name='index'),
    #iserrano2
    # authentication: signup, login, logout
    path('create', views.create, name='create'),
    path("loguser", views.login_user, name="loguser"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    #iserrano2
    #dashboard & publish_problem
    path("dashboard", views.dashboard, name='dashboard'),
    path('publish_problem', views.publish_problem, name='publish_problem'),
    #iserrano3
    path('problem/<int:problem_id>/show_my_problem', views.show_my_problem, name='show_my_problem'),
    path('script/<int:script_id>/show_my_script', views.show_my_script, name='show_my_script'),
    path('problem/<int:problem_id>/show_problem', views.show_problem, name='show_problem'),
    path('script/<int:script_id>/show_script', views.show_script, name='show_script'),

    # s3Integration
    # path('show_media', views.show_media, name='show_media'),
    path('upload', views.upload, name='upload'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

