from django.urls import path, include
from review import views

urlpatterns = [
    path('<int:music_id>/review/',views.Review(),name='review_view' ), #리뷰 작성, 보기
    path('<int:music_id>/review/<int:review_id>/',views.Review() ), #리뷰 수정
    path('<int:music_id>/review/<int:review_id>/',views.Review() ), #리뷰 삭제
]
#수정, 삭제 url을 따로 써줘야하는지? 메소드로 써주면 되는지? 의문