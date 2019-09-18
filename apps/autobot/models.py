from enum import Enum
from django.db import models


class DataType(Enum):
    BOOL = 1
    INT = 2
    DOUBLE = 3
    STRING = 4


class UIAction(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200)


class UIProperty(models.Model):
    name = models.CharField(max_length=15)
    data_type = models.IntegerField(
        choices=[(obj.value, obj.name) for obj in DataType])


class UIElement(models.Model):
    name = models.CharField(max_length=15)
    properties = models.ManyToManyField(UIProperty)
    actions = models.ManyToManyField(UIAction)


class Scenario(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class TestActionType(Enum):
    EXCUTE = 1
    EXPECT = 2
    EXPECT_WITH_TIMEOUT = 3
    TAKE_SCREENSHOT = 4


class TestAction(models.Model):
    description = models.CharField(max_length=200)
    scenario = models.ForeignKey(
        Scenario,
        related_name='test_actions',
        on_delete=models.CASCADE,
    )
    test_action_type = models.IntegerField(
        choices=[(obj.value, obj.name) for obj in TestActionType])
    ui_element_identifier = models.CharField(max_length=30)
    ui_element = models.ForeignKey(UIElement, on_delete=models.CASCADE,)
    ui_action = models.ForeignKey(UIAction, on_delete=models.CASCADE,)
    ui_property = models.ForeignKey(UIProperty,  on_delete=models.CASCADE,)
    reference_value = models.CharField(max_length=100)
    timeout = models.IntegerField(null=True, blank=True,)
