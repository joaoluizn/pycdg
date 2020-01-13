#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_basic_model import AbstractBasicModel
from teammate.models.function_requirement import FunctionRequirement


class SoftwareVersion(AbstractBasicModel):
    """A Software Version referred to a software project"""
    function_requirement = models.ManyToOneRel(FunctionRequirement,
                                               on_delete=models.CASCADE,
                                               field_name="Function Requirement")
    # full_estimation_time = calculated field with sum of all estimation_time of this Software Version
    # full_log_work = calculated field with sum of all log_works of this Software Version
    # full_tasks = calculated field with sum of all tasks of this Software Version

    class Meta:
        """Meta data for Software Version model"""
        verbose_name = 'software version'
        verbose_name_plural = 'software versions'
