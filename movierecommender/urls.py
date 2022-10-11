from django.urls import path

from movierecommender import views

urlpatterns = [
    path(route='', view=views.movie_recommendation_view,  # type: ignore
         name='recommendations'),
]
