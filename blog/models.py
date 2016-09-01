from __future__ import unicode_literals

from django.db.models import Model, CharField, TextField, ForeignKey
from django.contrib.auth.models import User


DEFAULT_USER_ID = 1


class Blog(Model):
    user_fk = ForeignKey(User, default=DEFAULT_USER_ID)
    blog_title = CharField(max_length=50, null=False)
    blog_content = TextField(max_length=1000, null=False)

    def __unicode__(self):
        return self.blog_title


class Comment(Model):
    blog_fk = ForeignKey(Blog)
    comment = CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.id
