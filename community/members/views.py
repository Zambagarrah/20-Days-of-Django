from django.shortcuts import render
from .models import Member

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/members.html', {'members': members})
