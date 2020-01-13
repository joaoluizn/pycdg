#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_basic_model import AbstractBasicModel
from teammate.models.software_version import SoftwareVersion


class Software(AbstractBasicModel):
    """A Software referred to a software project"""
    software_version = models.ManyToOneRel(SoftwareVersion, on_delete=models.CASCADE, field_name='Software Version')

    # full_estimation_time = calculated field with sum of all estimation_time of this Software
    # full_log_work = calculated field with sum of all log_works of this Software
    # full_task = calculated field with list of all the tasks of this Software
    # full_function_requirement = calculated field with list of all the function requirements of this Software

    class Meta:
        """Meta data for Software model"""
        verbose_name = 'software'
        verbose_name_plural = 'software'
