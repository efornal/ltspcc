from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class Attribute(models.Model):
    name = models.CharField(
        max_length=254,
        null=False,
        verbose_name=_('name')
    )
    type = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name=_('type')
    )
    default = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name=_('default')
    )
    description = models.TextField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name=_('description')
    )

    class Meta:
        db_table = 'attributes'
        verbose_name = _('Attribute')
        verbose_name_plural = _('Attributes')

    def __unicode__(self):
        return "{}".format(self.name)


class PossibleAttributeValue(models.Model):
    value = models.CharField(
        max_length=200,
        null=False,
        verbose_name=_('value')
    )
    attribute = models.ForeignKey(
        Attribute,
        null=False,
        blank=False,
        verbose_name=_('attribute')
    )

    class Meta:
        db_table = 'possible_attribute_values'
        verbose_name = _('PossibleAttributeValue')
        verbose_name_plural = _('PossibleAttributeValues')

    def __unicode__(self):
        return "{} : {}".format(self.attribute.name, self.value)


class Group(models.Model):
    name = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        verbose_name=_('name')
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name=_('parent')
    )
    attributes = models.ManyToManyField(
        Attribute,
        through='GroupAttributeValue',
        verbose_name = _('attributes')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created_at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated_at')
    )

    class Meta:
        db_table = 'groups'
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    def __unicode__(self):
        return "{}".format(self.name)


class GroupAttributeValue(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        null=False,
        blank=False,
        verbose_name=_('attribute')

    )
    group = models.ForeignKey(
        Group,
        null=False,
        blank=False,
        verbose_name=_('group')
    )
    value = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_('value')
    )

    class Meta:
        db_table = 'group_attribute_values'
        verbose_name = _('GroupAttributeValue')
        verbose_name_plural = _('GroupAttributeValues')

    def __unicode__(self):
        return "{}: {} = {}".format(self.group, self.attribute, self.value)


    
class Node(models.Model):
    dns_name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name=_('dns_name')
        )
    mac_address = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_('mac_address')
        )
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        verbose_name=_('group')
    )
    attributes = models.ManyToManyField(
        Attribute,
        through='NodeAttributeValue',
        verbose_name=_('attributes')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created_at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated_at')
    )

    class Meta:
        db_table = 'nodes'
        verbose_name = _('Node')
        verbose_name_plural = _('Nodes')

    def __unicode__(self):
        return "{}".format(self.dns_name)


class NodeAttributeValue(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        null=False,
        blank=False,
        verbose_name=_('attribute')
    )
    node = models.ForeignKey(
        Node,
        null=False,
        blank=False,
        verbose_name=_('node')
    )
    value = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_('value')
    )

    class Meta:
        db_table = 'node_attribute_values'
        verbose_name = _('NodeAttributeValue')
        verbose_name_plural = _('NodeAttributeValues')

    def __unicode__(self):
        return "{}: {} = {}".format(self.node, self.attribute, self.value)
