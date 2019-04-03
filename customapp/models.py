from django.db import models


class student(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    branch = models.CharField(max_length=30)


class Comment(models.Model):
    comment = models.TextField(max_length=200)
    student_id = models.IntegerField()
    teacher_id = models.IntegerField()


class teacher(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    sub = models.CharField(max_length=30)
    branch = models.CharField(max_length=40)


class teafollower(models.Model):
    teacher_id = models.IntegerField()
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    sub = models.CharField(max_length=30)
    student_id = models.IntegerField()


class userprofile(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)
    user_id = models.IntegerField()
    follower_id = models.IntegerField(default=0)
    requested_id = models.IntegerField()


class twit1(models.Model):
    Twit = models.TextField(max_length=200)
    user_id = models.IntegerField()
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=256)
    referenced_id = models.IntegerField()


class create_group(models.Model):
    group_name = models.CharField(max_length=30)
    admin_no = models.IntegerField()


class add_group_member(models.Model):
    user_id = models.IntegerField()
    group_name = models.CharField(max_length=30)
    member_no = models.IntegerField()


class message(models.Model):
    message = models.CharField(max_length=100)
    user_id = models.IntegerField()
    mem_id = models.IntegerField()


class groupmessage(models.Model):
    message = models.CharField(max_length=100)
    user_id = models.IntegerField()
