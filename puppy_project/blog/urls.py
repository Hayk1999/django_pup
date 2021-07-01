from django.urls import path
from .views import PupListView, AddPupView, UpdatePuppyView, DeletePuppyView, DetailPuppyView

urlpatterns = [ path('', PupListView.as_view(), name='home'), path('pup/<int:pk>/', DetailPuppyView.as_view(), name='detail_pup'), path('pup/new/', AddPupView.as_view(), name='add_pup'), path('pup/<int:pk>/edit', UpdatePuppyView.as_view(), name='change_pup'), path('pup/<int:pk>/delete/', DeletePuppyView.as_view(), name='delete_pup'), ]


