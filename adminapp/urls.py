from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'


urlpatterns = [
    # path('', adminapp.index, name='index'),
    path('', adminapp.ShopUserList.as_view(), name='index'),
    path('user/create/', adminapp.ShopUserCreate.as_view(), name='user_create'),
    path('user/delete/<int:user_pk>/', adminapp.ShopUserDelete.as_view(), name='user_delete'),
    path('user/update/<int:user_pk>/', adminapp.ShopUserUpdate.as_view(), name='user_update'),
    # path('user/update/<int:user_pk>/', adminapp.user_update, name='user_update'),
    path('categories/', adminapp.categories, name='categories'),
]
