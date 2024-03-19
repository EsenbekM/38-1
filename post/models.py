'''
models.py - это файл, в котором мы будем создавать наши модели.

ORM - Object-Relational Mapping (Объектно-реляционное отображение)
это программная технология, которая связывает базы данных с 
концепциями объектно-ориентированных языков программирования, 
создавая "виртуальную объектную базу данных". 
Это позволяет программистам работать с базами данных, 
используя объектно-ориентированный подход, а не язык SQL.

CREATE TABLE post_post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) DEFAULT NULL,
    content TEXT,
    created_at DATETIME,
    updated_at DATETIME
);

Table relationships:
- One-to-One
- One-to-Many
- Many-to-Many
'''

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    tags = models.ManyToManyField(
        Tag, 
        related_name='posts', 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.rate}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, # К какой модели относится
        on_delete=models.CASCADE, # Что делать с комментарием, если пост удален
        related_name='comments' # default: comment_set. Позволяет обращаться к комментариям через post.comments
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.title} - {self.text}"
    



# class PostInfo(models.Model):
#     post = models.OneToOneField(
#         Post,
#         on_delete=models.CASCADE,
#         primary_key=True, # default: False
#     )
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.post.title} - {self.likes}/{self.dislikes}"