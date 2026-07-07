from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import mail_managers
from blog.models import BlogEntry
from blog.forms import BlogEntryForm


class BlogEntryListView(ListView):
    model = BlogEntry
    template_name = 'blog/blogentry_list.html'
    context_object_name = 'entries'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogEntryDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog/blogentry_detail.html'
    context_object_name = 'entry'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        
        if obj.views_count == 100:
            mail_managers(
                subject='Поздравляем!',
                message=f'Статья "{obj.title}" достигла 100 просмотров!'
            )
        return obj


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    form_class = BlogEntryForm
    template_name = 'blog/blogentry_form.html'
    success_url = reverse_lazy('blog:blogentry_list')


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    form_class = BlogEntryForm
    template_name = 'blog/blogentry_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:blogentry_detail', kwargs={'pk': self.object.pk})


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    template_name = 'blog/blogentry_confirm_delete.html'
    success_url = reverse_lazy('blog:blogentry_list')
