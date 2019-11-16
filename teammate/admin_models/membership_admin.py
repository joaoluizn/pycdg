#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponseRedirect

from teammate.models.abstract_basic_model import CREATED_AT
from teammate.models.abstract_basic_model import UPDATED_AT
from teammate.models.membership import Membership
from teammate.models.membership import TEAMMATE
from teammate.models.membership import JOINED_AT
from teammate.models.membership import MEMBERSHIP_TYPE
from teammate.models.membership import DISJOINED_AT


class MembershipAdminStackedInline(admin.StackedInline):
    """Defines how a membership appears at teammate's admin page"""
    model = Membership
    fields = (JOINED_AT, MEMBERSHIP_TYPE, DISJOINED_AT)
    max_num = 1
    verbose_name_plural = 'membership'
    can_delete = False


class MembershipModelAdmin(admin.ModelAdmin):
    """Defines how a membership appears at its admin page"""
    readonly_fields = (TEAMMATE, CREATED_AT, UPDATED_AT)
    list_display = (TEAMMATE, JOINED_AT, MEMBERSHIP_TYPE, DISJOINED_AT, CREATED_AT, UPDATED_AT)
    list_filter = (TEAMMATE, JOINED_AT, MEMBERSHIP_TYPE, DISJOINED_AT, CREATED_AT, UPDATED_AT)
    search_fields = list_filter

    actions = None

    def _delete_view(self, request, object_id, extra_context):
        try:
            out = super()._delete_view(request, object_id, extra_context)
        except Exception as err:
            msg = err.args[0]
            messages.warning(request, msg)
            out = HttpResponseRedirect(os.path.dirname(os.path.dirname(request.path)))

        return out

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True
