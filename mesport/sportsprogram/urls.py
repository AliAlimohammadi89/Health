from django.urls import path, re_path
from . import views

app_name = 'sportsprogram'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('list', views.BookListView.as_view(), name='bookList'),
    #
    # # path('detail/<int:pk>/', views.BookDetailView.as_view(), name='bookDetail'),
    # re_path(r'^detail/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='bookDetail'),
    re_path(r'^get/$', views.ApiListPersonInfo.as_view(), name='ApiListPersonInfo'),
    # re_path(r'^get/Ex$', views.ApiListExercise.as_view(), name='ApiListExercise'),
    re_path(r'^login$', views.Login.as_view(), name='Login'),
    # re_path(r'^Splash/$', views.Splahe.as_view(), name='Splash'),
    path('Splash', views.Splahe.as_view(), name='Splash'),
    path('Exercise', views.Exercise.as_view(), name='Exercise'),
]
