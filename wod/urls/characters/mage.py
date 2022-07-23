from django.urls import include, path

from wod import views

urls = [
    path("ajax/load_faction_details/", views.load_factions, name="ajax_load_factions"),
    path(
        "ajax/load_subfaction_details/",
        views.load_subfactions,
        name="ajax_load_subfactions",
    ),
    path(
        "ajax/load-character-types/",
        views.load_character_types,
        name="ajax_load_character_types",
    ),
    path("create/cabal/", views.CabalCreateView.as_view(), name="create_cabal"),
    path("create/mage/", views.MageCreateView.as_view(), name="create_mage"),
    path("create/rote/", views.RoteCreateView.as_view(), name="create_rote"),
    path("instruments/<pk>/", views.InstrumentDetailView.as_view(), name="instrument"),
    path(
        "magefactions/<pk>/", views.MageFactionDetailView.as_view(), name="magefaction"
    ),
    path("paradigms/<pk>/", views.ParadigmDetailView.as_view(), name="paradigm"),
    path("practices/<pk>/", views.PracticeDetailView.as_view(), name="practice"),
    path("resonances/<pk>/", views.ResonanceDetailView.as_view(), name="resonance"),
    path("rotes/update/<pk>/", views.RoteUpdateView.as_view(), name="update_rote"),
    path("rotes/<pk>/", views.RoteDetailView.as_view(), name="rote"),
]
