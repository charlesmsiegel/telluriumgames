from django.urls import include, path

from exalted import views

urls = [
    path(
        "solar/create/",
        views.characters.solars.SolarCreateView.as_view(),
        name="create_solar",
    ),
    path(
        "solar/update/<pk>/",
        views.characters.solars.SolarUpdateView.as_view(),
        name="update_solar",
    ),
    path(
        "solarcharm/create/",
        views.characters.solars.SolarCharmCreateView.as_view(),
        name="create_solarcharm",
    ),
    path(
        "solarcharm/update/<pk>/",
        views.characters.solars.SolarCharmUpdateView.as_view(),
        name="update_solarcharm",
    ),
    path(
        "solarcharm/<pk>/",
        views.characters.solars.SolarCharmDetailView.as_view(),
        name="solarcharm",
    ),
    path('ajax/load-ratings-1/', views.characters.solars.load_merit_1_ratings, name='ajax_load_merit_1'),
    path('ajax/load-ratings-2/', views.characters.solars.load_merit_2_ratings, name='ajax_load_merit_2'),
    path('ajax/load-ratings-3/', views.characters.solars.load_merit_3_ratings, name='ajax_load_merit_3'),
    path('ajax/load-ratings-4/', views.characters.solars.load_merit_4_ratings, name='ajax_load_merit_4'),
    path('ajax/load-ratings-5/', views.characters.solars.load_merit_5_ratings, name='ajax_load_merit_5'),
    path('ajax/load-ratings-6/', views.characters.solars.load_merit_6_ratings, name='ajax_load_merit_6'),
    path('ajax/load-ratings-7/', views.characters.solars.load_merit_7_ratings, name='ajax_load_merit_7'),
    path('ajax/load-ratings-8/', views.characters.solars.load_merit_8_ratings, name='ajax_load_merit_8'),
    path('ajax/load-ratings-9/', views.characters.solars.load_merit_9_ratings, name='ajax_load_merit_9'),
    path('ajax/load-ratings-10/', views.characters.solars.load_merit_10_ratings, name='ajax_load_merit_10'),
]
