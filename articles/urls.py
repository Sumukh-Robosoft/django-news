from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('delete_user<int:pk>',views.delete_user,name='delete_user'),
    path('add-article/',views.add_article,name='add_article' ),
    path('view-articles/',views.view_articles,name="view_articles"),
    path('article/<int:pk>',views.individual_article,name='article'),
    path('publish-article/<int:pk>',views.publish_article,name="publish"),
    path("edit-article/<int:pk>",views.edit_article,name='edit_article'),
    path("profile/",views.get_profile,name="profile")
]
