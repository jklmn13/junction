# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Junction Stuff
from junction.base.admin import AuditAdmin

from . import models


class ConferenceAdmin(AuditAdmin):
    list_display = ('name', 'slug', 'start_date', 'end_date', 'status') + AuditAdmin.list_display
    prepopulated_fields = {'slug': ('name',), }


class ConferenceModeratorAdmin(AuditAdmin):
    list_display = ('conference', 'moderator', 'active') + AuditAdmin.list_display
    list_filter = ('conference',)


class ConferenceProposallReviewerAdmin(AuditAdmin, SimpleHistoryAdmin):
    list_display = ('conference', 'reviewer', 'active') + AuditAdmin.list_display
    list_filter = ('conference',)


class ConferenceSettingAdmin(AuditAdmin, SimpleHistoryAdmin):
    list_display = ('conference', 'name', 'value') + AuditAdmin.list_display
    list_filter = ('conference',)


admin.site.register(models.Conference, ConferenceAdmin)
admin.site.register(models.ConferenceModerator, ConferenceModeratorAdmin)
admin.site.register(models.ConferenceProposalReviewer,
                    ConferenceProposallReviewerAdmin)
admin.site.register(models.ConferenceVenue)
admin.site.register(models.Room)
admin.site.register(models.ConferenceSetting, ConferenceSettingAdmin)
