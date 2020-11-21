from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'query', views.queryViewSet,basename='query')
router.register(r'botsocial', views.BotSocialConfigViewSet,basename='botsocial')
router.register(r'intents', views.IntentsViewSet,basename='intents')
router.register(r'skills', views.SkillsViewSet,basename='skills')
router.register(r'bots', views.BotsViewSet,basename='bots')
router.register(r'entity', views.EntityViewSet,basename='entity')

# Wire up our API using automatic URL routing.
# Additionally, I include login URLs for the browsable API.
# Browsable APSs are disabled due to additional parameters from DJoser JWT implementation
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]