from django.contrib.admin import widgets
from django.db.models import fields
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Event
import json
# Create your views here.
from django import forms
from .forms import AttendanceForm
from .models import Event
from django.contrib.admin.widgets import (
    AdminDateWidget,
    AdminTimeWidget,
    AdminSplitDateTime,
)
from .models import Event


def index_v2(request):
    return render(request, "index_v2.html")


def update_attendance(request, event_id):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.cleaned_data['attendance']
            # Update the attendance in the database
            event = Event.objects.get(id=event_id)
            event.attendance = attendance
            event.save()
            return redirect('calendar')
    else:
        form = AttendanceForm()
    return render(request, 'attendance_form.html', {'form': form})

def get_events(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        event_list.append({'title': event.title, 'start': event.start_time.strftime("%Y-%m-%d %H:%M:%S"), 'end': event.end_time.strftime("%Y-%m-%d %H:%M:%S"), 'attendance': event.attendance})
    return HttpResponse(json.dumps(event_list), content_type='application/json')