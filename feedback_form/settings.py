# -*- coding: utf-8 -*-
from django.conf import settings

CONTACT_ADMINS_ONLY = getattr(settings, 'CONTACT_ADMINS_ONLY', True)

CONTACT_SEND_META_INFO = getattr(settings, 'CONTACT_SEND_META_INFO', False)
