#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin

from teammate.admin_models.membership_admin import MembershipAdminStackedInline
from teammate.models.abstract_basic_model import CREATED_AT
from teammate.models.abstract_basic_model import UPDATED_AT
from teammate.models.abstract_person import STR
from teammate.models.abstract_person import FIRST_NAME
from teammate.models.abstract_person import LAST_NAME
from teammate.models.abstract_person import BIRTH_DATE


class TeammateModelAdmin(admin.ModelAdmin):
    """Defines how a teammate appears at its admin page"""
    readonly_fields = (CREATED_AT, UPDATED_AT)
    list_display = (STR, BIRTH_DATE, CREATED_AT, UPDATED_AT)
    list_filter = (FIRST_NAME, LAST_NAME, BIRTH_DATE, CREATED_AT, UPDATED_AT)
    search_fields = list_filter
    inlines = [MembershipAdminStackedInline]
