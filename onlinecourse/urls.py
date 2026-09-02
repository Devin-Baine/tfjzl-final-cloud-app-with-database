from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Route Is a String Containing a URL Pattern
    # View Refers to the View Function
    # Name Identifies the URL
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # Example: /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # Example: /onlinecourse/5/enroll/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    # Example: /onlinecourse/5/submit/
    path('<int:course_id>/submit/', views.submit, name='submit'),
    # Example: /onlinecourse/course/5/submission/1/result/
    path('course/<int:course_id>/submission/<int:submission_id>/result/',
         views.show_exam_result, name='exam_result'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
