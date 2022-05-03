from django.urls import path

from wod import views

# Create your URLs here
urlpatterns = [
    path("characters/", views.IndexView.as_view(), name="characters_index"),
    path("characters/<pk>/", views.CharacterDetailView.as_view(), name="character"),
    path("characters/mage/create/", views.MageCreateView.as_view(), name="create_mage"),
    path("characters/mage/<pk>/update/", views.MageUpdate.as_view(), name="update_mage"),
    path("ajax/load_faction_details/", views.load_factions, name='ajax_load_factions'),
    path("ajax/load_subfaction_details/", views.load_subfactions, name='ajax_load_subfactions')
]
