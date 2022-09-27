from django.urls import path
from . import views


urlpatterns = [

    # for generic view
    path('generic_student/', views.StudentGenericView.as_view()),

    # for class based view
    # path('', views.StudentView.as_view()),
    # path('register/', views.UserView.as_view()),

    # for function based view
    # path('', views.home, name='home'),
    # path('post/', views.post_data, name='post_data'),
    # path('read/<str:pk>/', views.read_data, name='read_data'),

    # path('update/<str:pk>/', views.update_data, name='update_data'),
    # path('delete/<str:pk>/', views.delete_data, name='delete_data'),

    # Books urls
    # path('books/', views.book_list, name='book_list'),
    # path('books/post/', views.book_post, name='book_post'),

]
