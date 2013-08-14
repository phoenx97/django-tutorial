import datetime

from django.utils import timezone
from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=200)  # var name 'question' will be the column name
    pub_date = models.DateTimeField('date published')  # use date published as human readable name instead of pub_date

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
