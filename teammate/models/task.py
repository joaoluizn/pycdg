#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_basic_model import AbstractBasicModel
from teammate.models.log_work import LogWork


class Task(AbstractBasicModel):
    """A task that a person executes in a software project"""
    estimation_time = models.FloatField(null=False, blank=False, verbose_name='Estimation Time (in hours)')
    log_work = models.ManyToOneRel(LogWork, on_delete=models.CASCADE, field_name="Log Work")
    # total_log_works: calculated field with sum of all log_works of this task

    class Meta:
        """Meta data for Task model"""
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
