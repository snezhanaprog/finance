from django.contrib import admin
from .models import *


admin.site.register(Budget)
admin.site.register(SavingGoal)
admin.site.register(Expense)
admin.site.register(Income)