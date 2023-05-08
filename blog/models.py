from django.db import models


class Post(models.Model):
    title = models.CharField('title post', max_length=200)
    description = models.TextField('post text')
    author = models.CharField('Author name', max_length=100)
    date = models.DateField('Publication date')
    img = models.ImageField('image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    text_coments = models.TextField('Comment...', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Post',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    ip = models.CharField('ip', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='post',
                            on_delete=models.CASCADE)


class AboutUs(models.Model):
    email = models.EmailField('Email', max_length=50)
    name = models.CharField('Full name develpoer', max_length=100)
    gitLink = models.CharField('GitHub links', max_length=300)
    work = models.CharField('Work exip', max_length=100)
    descr = models.TextField('Work description', max_length=2000)
    img = models.ImageField('User img', upload_to='image/%Y')

    def __str__(self):
        return f'{self.name}, {self.email},{self.gitLink},{self.work},{self.descr}'

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
