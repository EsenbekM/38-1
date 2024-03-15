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
'''

from django.db import models


class Post(models.Model):
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.rate}"
