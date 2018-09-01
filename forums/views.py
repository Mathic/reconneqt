from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView

from .forms import ThreadForm, PostForm, NewThreadForm
from .models import Subject, Thread, Post

# Create your views here.
def forum(request):
    try:
        parents = Subject.objects.filter(parent=None)
        children = Subject.objects.exclude(parent=None)
        context = {
            'parents': parents,
            'children': children
        }
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    return render(request, 'forums/forums.html', context)

def threads(request, s_id):
    try:
        parents = Subject.objects.filter(parent=None)
        children = Subject.objects.exclude(parent=None)
        subject = Subject.objects.get(pk=s_id)
        thread_list = Thread.objects.filter(subject_fk__id=s_id)

        paginator = Paginator(thread_list, 5) # Show 5 threads per page
        page = request.GET.get('page')
        threads = paginator.get_page(page)

        context = {
            'parents': parents,
            'children': children,
            'subject': subject,
            'threads': threads
        }
    except Thread.DoesNotExist:
        raise Http404("Thread does not exist")
    return render(request, 'forums/subject.html', context)

def thread_detail(request, pk):
    try:
        parents = Subject.objects.filter(parent=None)
        children = Subject.objects.exclude(parent=None)
        thread = Thread.objects.get(pk=pk)
        posts = Post.objects.filter(thread_fk=thread).filter(original=False).order_by('post_created')
        post = Post.objects.filter(thread_fk=thread).get(original=True)

        context = {
            'parents': parents,
            'children': children,
            'thread': thread,
            'posts': posts,
            'post': post
        }
    except Thread.DoesNotExist:
        raise Http404("Thread does not exist")
    return render(request, 'forums/thread.html', context)

def thread_create(request):
    try:
        parents = Subject.objects.filter(parent=None)
        children = Subject.objects.exclude(parent=None)
        if request.method == 'POST':
            form = NewThreadForm(request.POST, prefix='form')
            form2 = PostForm(request.POST, prefix='form2')
            f1_valid = form.is_valid()
            f2_valid = form2.is_valid()
            if f1_valid or f2_valid:
                thread = form.save(commit=False)
                post = form2.save(commit=False)
                print(form.cleaned_data['subject_fk'])
                thread.user = request.user
                post.user = request.user
                post.original = True
                thread.save()
                post.thread_fk = thread
                post.save()
                return redirect('/forums')
        else:
            form = NewThreadForm(prefix='form')
            form.fields["subject_fk"].queryset = Subject.objects.filter(parent__isnull=False)
            form2 = PostForm(prefix='form2')
            context = {
                'parents': parents,
                'children': children,
                'form': form,
                'form2': form2
            }
            return render(request, 'forums/thread_edit.html', context)
    except Subject.DoesNotExist:
        raise Http404("Thread does not exist")
    return render(request, 'forums/')

def post_create(request, pk):
    try:
        parents = Subject.objects.filter(parent=None)
        children = Subject.objects.exclude(parent=None)
        thread = Thread.objects.get(pk=pk)
        post = Post.objects.filter(thread_fk=thread).get(original=True)
        if request.method == 'POST':
            form = PostForm(request.POST, prefix='form')
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.original = False
                post.thread_fk = thread
                post.save()
                return redirect('/forums/thread/'+str(pk)+'/')
        else:
            form = PostForm(prefix='form')
            context = {
                'parents': parents,
                'children': children,
                'thread': thread,
                'post': post,
                'form': form
            }
            return render(request, 'forums/post_edit.html', context)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    return render(request, 'forums/')
