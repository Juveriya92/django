from django.urls import path
from .views import Dashboard,StoryDetail,UpdateStory,DeleteStory,CreateStory
from . import views

urlpatterns = [
    path('',views.HomePage,name='home'),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('dashboard/',Dashboard.as_view(),name="dashboard"),
    path('story/<int:pk>',StoryDetail.as_view(),name="storydetail"),
    path('addstory/',CreateStory.as_view(),name="addstory"),
    path('story/update/<int:pk>',UpdateStory.as_view(),name="update"),
    path('story/delete/<int:pk>',DeleteStory.as_view(),name="delete"),
    path('story/userstories',views.UserStories,name="user_posts"),
]