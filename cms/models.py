from django.db import models

# Create your models here.


class Book(models.Model):
    """書籍"""
    ISBN = models.CharField('ISBN', max_length=255, blank=True)
    ASIN = models.CharField('ASIN', max_length=255, blank=True)
    NDLBibID = models.CharField('NDL書誌ID', max_length=255)
    title = models.CharField('書名', max_length=255)
    volume = models.CharField('巻次', max_length=255, blank=True)
    seriesTitle = models.CharField('シリーズ名', max_length=255)
    creator = models.CharField('著者名', max_length=255, blank=True)
    publisher = models.CharField('出版者', max_length=255)
    publicationPlace = models.CharField('出版地', max_length=255, blank=True)
    date = models.CharField('出版年', max_length=255)
    NDC = models.CharField('NDC', max_length=255, blank=True)
    subject = models.CharField('件名', max_length=255, blank=True)
    price = models.CharField('価格', max_length=255, blank=True)
    extent = models.CharField('ページ数', max_length=255, blank=True)
    description = models.CharField('注記', max_length=255, blank=True)
    partTC = models.CharField('内容', max_length=255, blank=True)
    #photo = 'https://iss.ndl.go.jp/thumbnail/' + ISBN.replace('-', '')

class jpro(models.Model):
    ISBN = models.CharField('ISBN', max_length=255, blank=True)
    title = models.CharField('書名', max_length=255)
    volume = models.CharField('巻次', max_length=255, blank=True)
    subtitle = models.CharField('副書名', max_length=255, blank=True)
    series = models.CharField('シリーズ名', max_length=255, blank=True)
    creator = models.CharField('著者名', max_length=255, blank=True)
    publisher = models.CharField('出版者', max_length=255)
    date = models.CharField('出版日', max_length=255)
    price = models.CharField('価格', max_length=255, blank=True)
    extent = models.CharField('ページ数', max_length=255, blank=True)
    ccode = models.CharField('Cコード', max_length=255, blank=True)
    genrecode = models.CharField('ジャンルコード', max_length=255, blank=True)
    keywords = models.CharField('キーワード', max_length=255, blank=True)
    audience = models.CharField('対象年齢', max_length=255, blank=True)
    creatornote = models.CharField('著者紹介', max_length=255, blank=True)
    description = models.CharField('内容', max_length=1000, blank=True)
    ToC = models.CharField('目次', max_length=1000, blank=True)
    datemodified = models.CharField('データ修正日', max_length=255, blank=True)
    NDC = models.CharField('NDC', max_length=255, blank=True)

    def __str__(self):
        return self.title
