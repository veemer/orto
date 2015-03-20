# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models


class ThisWeekManager(models.Manager):

    def get_queryset(self):

        qs = super(ThisWeekManager, self).get_queryset()

        today = timezone.now()

        start_week = today - timezone.timedelta(today.weekday())
        end_week = start_week + timezone.timedelta(7)

        return qs.filter(record__next_visit_date__range=[start_week, end_week])
