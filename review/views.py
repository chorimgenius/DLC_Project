from rest_framework.views import APIview
from rest_framework import status, 
from rest_framework.response import Response


# Create your views here.
class Review():
    def get(self, request, music_id):
        Reviews = Review.obkects.all()
        serializer = Reiveiw(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, music_id):
        pass

    def put(self, request, music_id):
        pass

    def delete(self, request, music_id):
        pass