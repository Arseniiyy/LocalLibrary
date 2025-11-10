from django.urls import path, re_path,include
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'), 
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'book/(?P<pk>[-\w]+)/renew/$',views.renew_book_libration,name='renew-book-libration')
]
