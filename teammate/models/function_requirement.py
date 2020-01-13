#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_basic_model import AbstractBasicModel
from teammate.models.task import Task


class FunctionRequirement(AbstractBasicModel):
    """A Function Requirement referred to a software project"""
    task = models.ManyToOneRel(Task, on_delete=models.CASCADE, field_name="Task")
    # full_estimation_time = calculated field with sum of all estimation_time of this Software Version
    # full_log_work = calculated field with sum of all log_works of this Software Version

    class Meta:
        """Meta data for Function Requirement model"""
        verbose_name = 'function requirement'
        verbose_name_plural = 'function requirements'
