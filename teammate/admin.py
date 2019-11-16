from django.contrib import admin

from .admin_models.membership_admin import MembershipModelAdmin
from .admin_models.teammate_admin import TeammateModelAdmin
from .models.membership import Membership
from .models.teammate import Teammate

# Register your models here.
admin.site.register(Teammate, TeammateModelAdmin)
admin.site.register(Membership, MembershipModelAdmin)
