from django.urls import path

urlpatterns = [
    path('<int:music_id>/review/', ), #리뷰 작성
    path('<int:music_id>/review/<int:review_id>/', ), #리뷰 수정
    path('<int:music_id>/review/<int:review_id>/', ), #리뷰 삭제
]
