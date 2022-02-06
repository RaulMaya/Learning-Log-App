from django.shortcuts import render, redirect

import learning_logs

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """The home page for learning logs"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Shows the topic, with all his entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context ={'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adding a new topic"""
    if request.method != 'POST':
        # No data submitted; and create a blank form
        form = TopicForm()
    else:
        # POST data submitted; Processing data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # Display a blanck or invalid form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)