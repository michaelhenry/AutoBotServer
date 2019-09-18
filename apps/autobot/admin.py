from django.contrib import admin
from .models import (
    UIAction,
    UIProperty,
    UIElement,
    Scenario,
    TestAction,
)

admin.site.register(UIAction)
admin.site.register(UIProperty)
admin.site.register(UIElement)
admin.site.register(Scenario)
admin.site.register(TestAction)
