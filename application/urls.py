from django.urls import path
from .views import MainView, news, RecordingView, DiscussionView, PollsView, products, fun, color, AnimalView, timeClient



urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('fun/<str:text>', fun, name='fun'),
    path('color', color, name='color'),
    path('news', news, name='newssite'),
    path('recording', RecordingView.as_view(), name='recording'),
    path('discussion', DiscussionView.as_view(), name='discussion'),
    path('polls/', PollsView.as_view(), name='polls'),
    path('products/<int:id>', products, name='products'),
    path('animal/', AnimalView.as_view(), name='animal'),
    path('clinicClients/', timeClient, name='search'),
]