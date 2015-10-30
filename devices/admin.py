from django.contrib import admin

from .models import SensorType, ActuatorType, Sensor, Actuator, SensorData, ActuatorData
from nodes.models import Node
"""Inlines"""


class SensorInline(admin.TabularInline):
    model = Sensor
    extra = 3


class ActuatorInline(admin.TabularInline):
    model = Actuator
    extra = 3


class SensorDataInline(admin.TabularInline):
    model = SensorData
    extra = 0


class ActuatorDataInline(admin.TabularInline):
    model = ActuatorData

"""End Inlines"""


class abstractAdmin(admin.ModelAdmin):
    # I dont know why, but if the admin imports this class, everything breaks
    # so for now I have to keep it duplicated :(
    readonly_fields = ['created', 'last_modified']
    fieldsets = [
        ('Basic Information', {'fields': ['name']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    inlines = []


class SensorAdmin(abstractAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['name', 'model', 'node']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    list_display = ['name', 'node', 'created', 'last_modified']
    inlines = [SensorDataInline]
    list_filter = ['node']
    search_fields = ['name', 'node']


class ActuatorAdmin(abstractAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['name', 'model', 'node']}),
        ('Date Information', {
            'fields': ['created', 'last_modified'], 'classes': ['collapse']}),
    ]
    list_display = ['name', 'node', 'created', 'last_modified']
    inlines = [ActuatorDataInline]
    list_filter = ['node']
    search_fields = ['name', 'node']

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Actuator, ActuatorAdmin)
admin.site.register(SensorType)
admin.site.register(ActuatorType)
admin.site.register(SensorData)
admin.site.register(ActuatorData)

# As Opposed to setting this in nodes/admin.py I have elected to put this
# here instead to avoid a circular dependancy
admin.site._registry[Node].inlines.append(SensorInline)
admin.site._registry[Node].inlines.append(ActuatorInline)
