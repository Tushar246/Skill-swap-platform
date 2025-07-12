from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def home(request):
    query = request.GET.get("search", "")
    availability = request.GET.get("availability", "")
    users = UserProfile.objects.filter(public=True)

    if query:
        users = users.filter(offered_skills__skill__name__icontains=query).distinct()

    if availability:
        users = users.filter(availability=availability)

    return render(request, "home.html", {"users": users, "query": query})
