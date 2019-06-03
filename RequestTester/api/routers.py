from rest_framework import routers
from .viewsets import PersonViewsets

router = routers.DefaultRouter()
router.register(r'user', PersonViewsets),