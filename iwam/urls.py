from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.ScriptList.as_view(), name='script_list'),
    path('scripts/<int:pk>', views.ScriptDetail.as_view(), 
    name='script_detail'),

    path('comments', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]