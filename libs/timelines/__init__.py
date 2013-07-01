from django.db import transaction, DatabaseError
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

from timelines.models import UserTimelineItem

@transaction.commit_on_success
def setup_timelines_signal(item):
  try:
    app_label     = item['model'].split('.')[0]
    model         = item['model'].split('.')[1]
    content_type  = ContentType.objects.get(app_label=app_label, model=model)
    model         = content_type.model_class()
    UserTimelineItem.objects.follow_model(model)
  except (ContentType.DoesNotExist, DatabaseError):
    transaction.rollback()

for item in settings.TIMELINES_MODELS:
  setup_timelines_signal(item)
