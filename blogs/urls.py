from django.urls import path, include

from blogs import views
from blogs.views import PostDetailView

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='blog-detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    # path('blog/', BlogList.as_view(), name='blog-list'),
    path('', views.blog, name='blog-list'),
    # path('<slug:slug>/', views.detail, name='blog-detail'),
    path('category/<str:id>/', views.category_page, name='cate-page'),
    path('search', views.search, name='search')

]
