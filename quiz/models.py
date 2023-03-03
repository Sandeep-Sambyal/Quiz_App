from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):
    title = models.CharField(max_length=300, primary_key=True)
    description = models.CharField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} created on {self.created_on}"
    
    # def get_questions(self):
    #     questions = list(self.question_set.all())
    #     return questions
class quiz_allocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    diff_level = models.CharField(max_length=6, choices=DIFF_CHOICES, default='easy')

    def __str__(self):
        return f"{self.quiz.title} DIFFICULTY: {self.diff_level} assigned to {self.user}"

    class Meta:
        unique_together = ["user", "quiz", "diff_level"]

class Question(models.Model):
    title = models.TextField(verbose_name='Question', unique=True)
    # quiz = models.ForeignKey(Quiz, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    quiz = models.ManyToManyField(Quiz)
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self,):
        return f"{self.title}"

    def get_answers(self):
        questions = list(self.answer_set.all())
        return questions

class Answer(models.Model):
    option = models.CharField(max_length=1000)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.option}"
