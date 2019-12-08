from django.db import models

class Entry(models.Model):
    title = models.CharField('タイトル', max_length=128)
    content = models.TextField('本文')
    thumbnail = models.ImageField('サムネイル', null=True)

    class Meta:
        db_table = 'entry'
        verbose_name = '記事'
        verbose_name_plural = '記事一覧'

    def __str__(self):
        return(self.title)
