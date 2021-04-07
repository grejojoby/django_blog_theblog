from theblog.models import Category
from django.urls import path
# from . import views
from .views import AddCommentView, AddPostView, DeletePostView, HomeView, ArticleDetailView, UpdatePostView, AddCategoryView , CategoryView, LikeView
urlpatterns = [
    # path('',views.home, name="home"),
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/',CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
