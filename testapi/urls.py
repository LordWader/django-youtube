from django.urls import path
from testapi import views

urlpatterns = [
    path("api/words", views.items_list),
    path("api/words/<int:pk>", views.item_detail),
    path("api/words/<int:pk>/videos", views.video_results)
]
