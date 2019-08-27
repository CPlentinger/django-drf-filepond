from django.apps import AppConfig

import logging

LOG = logging.getLogger(__name__)


class DjangoDrfFilepondConfig(AppConfig):
    name = 'django_drf_filepond'
    verbose_name = 'FilePond Server-side API'
