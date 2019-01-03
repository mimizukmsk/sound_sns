from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Timeline
from .forms import TimelineForm

class TimelineListView(ListView):
    model = Timeline
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().order_by('-posted_date')

class TimelineDetailView(DetailView):
    model = Timeline
    context_object_name = 'post'

class TimelineCreateView(CreateView):
    model = Timeline
    form_class = TimelineForm
    success_url = reverse_lazy('index')
    template_name = 'timeline/timeline_create_form.html'

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        return super().form_invalid(form)

class TimelineUpdateView(UpdateView):
    model = Timeline
    form_class = TimelineForm
    template_name = 'timeline/timeline_update_form.html'

    def get_success_url(self):
        post_pk = self.kwargs['pk']
        url = reverse_lazy('detail', kwargs={'pk': post_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, "更新されました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)

class TimelineDeleteView(DeleteView):
    model = Timeline
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除されました")
        return super().delete(request, *args, **kwargs)