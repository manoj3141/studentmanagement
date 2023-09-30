from stu_manage import views
from django.urls import path
from django.contrib.auth import views as v

urlpatterns=[path('',views.home,name='home'),
             path('view',views.table,name='table')
             ,path('update/<int:id>',views.update,name='update'),
             path('delete/<int:id>',views.delete,name='delete')
             ,path('path',views.show,name='show')
             ,path('signup',views.reg,name='singup'),
             path('login/',views.user_log,name='login')
             ,path('logout',views.user_logout,name='logout')
             ,path('date',views.showDate,name='showdate')
             ,path('wish',views.wish,name='wish')
             ,path('showstd',views.showstd,name='showstd')
             ]