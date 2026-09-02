from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# Inline Editor Allowing Lessons to Be Managed Within a Course
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Inline Editor Allowing Choices to Be Managed Within a Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Inline Editor Allowing Questions to Be Managed Within a Course
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# Admin Configuration for the Course Model
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Admin Configuration for the Question Model
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content']


# Admin Configuration for the Lesson Model
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Model Registration
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
