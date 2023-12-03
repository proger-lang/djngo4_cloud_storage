from django.urls import path
from shop1.views import index, index_id

app_name = "shop1"

urlpatterns = [
    path('', index),
    path('<m_id>/', index_id, name="detail"),
]


