from django.urls import path, include
from review import views

urlpatterns = [
    path('<int:music_id>/review/',views.ReviewView.as_view(),name='review_view' ), #리뷰 작성, 보기
    path('<int:music_id>/review/<int:review_id>/',views.DetailReview.as_view(),name='DetailReview'), #리뷰 수정, 삭제
]