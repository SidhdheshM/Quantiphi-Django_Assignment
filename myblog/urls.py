from django.urls import path
#from . import views
from .views import HomePageView, PostDetailView, AddPostView

urlpatterns = [
    #path('',views.homepage, name="homepage"),
    path('', HomePageView.as_view(), name="homepage"),
    path('blogpost/<int:pk>', PostDetailView.as_view(), name="post_details"),
    path('addpost/', AddPostView.as_view(), name="addpost")
]
