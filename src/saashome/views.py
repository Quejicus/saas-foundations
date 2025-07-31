from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.filter(path=request.path)
    my_title = "SaaS Home Page Title"
    my_context = {
        "page_title": my_title,
        "page_visit_count": queryset.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
