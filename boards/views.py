from msilib.schema import ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponse
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# home page function
# def home(request):    
#     boards = Board.objects.all()
#     return render(request, "index.html", {"boards": boards})

# class for list view for boards in home page
class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'index.html'


# diplaying boards function
def boardTopics(request, board_id):
    board = get_object_or_404(Board, pk = board_id)
    querySet = board.topics.order_by('-created_dt').annotate(comments = Count('posts'))
    page = request.GET.get('page', 1)
    paginator = Paginator(querySet, 1)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)
    return render(request, 'topics.html', {"board": board, 'topics':topics})

# new topic function
@login_required
def newTopic(request, board_id):
    board = get_object_or_404(Board, pk = board_id)
    # user = User.objects.first()
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get("message"),
                created_by = request.user,
                topic = topic
            )
            return redirect('boardTopics', board_id = board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {"board": board, "form":form})

# function for posts of each topic
def topic_posts(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board__pk = board_id, pk = topic_id)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})

# function for post reply
@login_required
def replyTopic(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board__pk = board_id, pk = topic_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topicPosts', board_id = board.pk, topic_id = topic.pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

# update posts class view (Class-Based views)
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message')
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_dt = timezone.now()
        post.save()
        return redirect('topicPosts', board_id = post.topic.board.pk, topic_id = post.topic.pk)

# about page
def about(request):
    return render(request, "about")