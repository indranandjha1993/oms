from argparse import Namespace
from django.urls import include, path
from .v1_0_0 import urls as api_v0_0_1
from .views import StableApiVersion

urlpatterns = [
    path('', StableApiVersion),
    path('v0.0.1/', include(api_v0_0_1)),
]