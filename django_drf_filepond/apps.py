from django.apps import AppConfig

import os
import logging
import django_drf_filepond.drf_filepond_settings as local_settings

LOG = logging.getLogger(__name__)

class DjangoDrfFilepondConfig(AppConfig):
    name = 'django_drf_filepond'
    verbose_name = 'FilePond Server-side API'
