from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass


@dataclass
class Teams:
    name: str
    description: str
    members: list


teams = {
    "management": Teams(
        name="Management",
        description="The management team is responsible for the overall management of the building",
        members=["Owen", "Jeremiah", "Nick", "Ab", "Abigail", "Mathew"],
    ),
    "procurement": Teams(
        name="Procurement",
        description="The procurement team is responsible for the food",
        members=["Adrian", "Bryce", "Big John", "Blaine", "Wyatt"],
    ),
    "documentation": Teams(
        name="Documentation",
        description="The documentation team is responsible for documenting things that happen around the building and events.",
        members=["Conner", "Kaleigh", "Blair", "Mina", "Jay", "Joshua", "Kayleah"],
    ),
    "community": Teams(
        name="Community",
        description="The community team is responsible for the planning the events and activities for the building.",
        members=["Jordan", "Joby", "Aj", "Micah", "Caleb"],
    ),
}


def homepage(request):
    return render(request, "homepage.html")


def team_viewer(request, team):
    context = {
        "team": teams[team],
    }
    if (
        team == "management"
        or team == "procurement"
        or team == "documentation"
        or team == "community"
    ):
        return render(request, "details.html", context)
    else:
        return HttpResponse("Team is unavailable")
