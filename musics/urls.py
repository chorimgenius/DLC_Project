from django.urls import path
from musics import views

urlpatterns = [
    path('', views.MusicListView.as_view(), name='Music_view'),
    path('<int:music_id>/', views.MusicDetailView.as_view(), name='MusicDetailView'),
    path('<int:music_id>/like/', views.Likeview.as_view(), name='MusicLikeView'),
]
