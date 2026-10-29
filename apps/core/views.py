from django.contrib.auth.models import AnonymousUser
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from apps.core.models import DemoJob
from apps.core.tasks import send_test_notification, run_demo_job


class HomeView(TemplateView):
    template_name = "core/home.html"


# @login_required
def enqueue_test_notification(request):
    send_test_notification("Привет из Huey!")
    messages.success(request, "Уведомление поставлено в очередь.")
    return redirect("core:home")


# @login_required
@require_POST
def start_demo_job(request):
    active_job = DemoJob.objects.filter(
        status__in=[
            DemoJob.Status.PENDING,
            DemoJob.Status.RUNNING,
        ],
    ).order_by("-created_at").first()

    if active_job:
        job = active_job
    else:
        job = DemoJob.objects.create()
        run_demo_job(job.pk)

    return render(
        request,
        "core/partials/demo_job_status.html",
        {"job": job},
    )


# @login_required
@require_GET
def demo_job_status(request, job_id):
    job = get_object_or_404(
        DemoJob,
        pk=job_id,
    )

    return render(
        request,
        "core/partials/demo_job_status.html",
        {"job": job},
    )


# @login_required
def demo_job_page(request):
    active_job = DemoJob.objects.filter(
        status__in=[
            DemoJob.Status.PENDING,
            DemoJob.Status.RUNNING,
        ],
    ).order_by("-created_at").first()

    return render(
        request,
        "core/demo_job.html",
        {"job": active_job},
    )
