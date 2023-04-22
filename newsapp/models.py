from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title} - {self.author}'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text = models.TextField('Текст комментария', max_length=2000)
    news = models.ForeignKey(News, verbose_name='Публикации', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name} - {self.news}'


class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=100)
    news = models.ForeignKey(News, verbose_name='Публикация', on_delete=models.CASCADE)

