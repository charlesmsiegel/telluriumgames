from django.urls import include, path

from wod import views

urls = [
    path("create/item/", views.ItemCreateView.as_view(), name="create_item"),
]
