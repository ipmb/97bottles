from django.db import models
from django.db.models import signals
from django.contrib.contenttypes.models import ContentType

from savoy.core.new.profiles.models import *

class ProfileManager(models.Manager):
  def remove_orphans(self, instance, **kwargs):
    """
    When a User is deleted, first delete any Profile object that has been created
    on its behalf.
    """
    from savoy.core.profiles.models import Profile
    try:
      self.get(user=instance).delete()
    except Profile.DoesNotExist:
      return
  
  def create_or_update(self, instance, **kwargs):
    """
    Create or update a Profile from some User.
    """
    profile, created = self.get_or_create(
      user = instance,
    )
    return profile