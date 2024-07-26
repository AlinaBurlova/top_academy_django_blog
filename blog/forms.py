from django import forms
from .models import Post

# class PostForm(forms.Form):
#     author = forms.CharField(max_length=50, label="Автор")
#     title = forms.CharField(max_length=200, label="Заголовок")
#     text = forms.CharField(label="Текст поста", widget=forms.Textarea())

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text']  # вручную (что используем)
        # fields = '__all__'  # все сразу, НО! так не надо
        # exclude = ['created_at']  # вручную (что НЕ используем)