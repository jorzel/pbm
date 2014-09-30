from django.db import models


class News(models.Model):
    date = models.DateTimeField("Date", auto_now=True)
    title = models.CharField("Title", max_length=200)
    content = models.TextField("News content (html allowed)", max_length=2000)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"


class Research(models.Model):
    Unit = models.CharField("Unit", max_length=200)
    title = models.CharField("Title", max_length=200)
    start_date = models.DateTimeField("Start date")
    end_date = models.DateTimeField("Estimated end date")
    content = models.TextField("Research description (html allowed)", max_length=2000)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Research"