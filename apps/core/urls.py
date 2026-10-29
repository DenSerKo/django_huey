from django.urls import path

from apps.core import views


app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(
        "push/test-queue/",
        views.enqueue_test_notification,
        name="enqueue_test_notification",
    ),
    path(
        "demo-job/start/",
        views.start_demo_job,
        name="start_demo_job",
    ),
    path(
        "demo-job/<int:job_id>/status/",
        views.demo_job_status,
        name="demo_job_status",
    ),
    path("demo-job/", views.demo_job_page, name="demo_job_page"),
]