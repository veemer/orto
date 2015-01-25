# -*- coding: utf-8 -*-

from django.forms.models import modelformset_factory
from records.models import Attachment

AttachmentFormset = modelformset_factory(Attachment, extra=5, exclude=['record', 'doctor'])