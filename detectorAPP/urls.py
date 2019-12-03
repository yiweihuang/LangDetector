from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from detectorAPP import views

urlpatterns = [
    url(r'^api/v1/langdetect$', views.DetectorAppLang.as_view(), name='detector-app-lang'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
