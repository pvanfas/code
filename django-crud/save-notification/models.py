class Notification(models.Model):
    user = models.ForeignKey("auth.User",blank=True,null=True,related_name="user_%(class)s_objects")
    who = models.ForeignKey("auth.User",blank=True,null=True,related_name="who_%(class)s_objects") 
    subject = models.ForeignKey("users.NotificationSubject")
    
    # Add fields or fk we want.
    customer = models.ForeignKey("customers.Customer",null=True,blank=True)
    
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'users_notification'
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')
        ordering = ('-time',)  

    def __unicode__(self):
        return self.subject.name


class NotificationSubject(models.Model):
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'users_notification_subject'
        verbose_name = _('notification subject')
        verbose_name_plural = _('notification subjects')
        ordering = ('name',)

    def __unicode__(self):
        return self.name