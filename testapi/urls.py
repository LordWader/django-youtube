from django.conf.urls import url
from django.urls import path
from testapi import views as v
from rest_framework.authtoken import views

urlpatterns = [
    path("api/words", v.items_list),
    path("api/words/<int:pk>", v.item_detail),
    path("api/words/<int:pk>/videos", v.video_results),
    url(r'^get-user-auth-token/', views.obtain_auth_token, name='get_user_auth_token')
]
