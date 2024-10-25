from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDeleteView, ProjectCreateView, UserProjectsView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDeleteView.as_view(), name='client-retrieve-update-delete'),
    path('clients/<int:pk>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]
