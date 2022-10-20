from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'content', 'snippet', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user_id', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = "Tytuł"
        self.fields['category'].label = "Kategoria"
        self.fields['content'].label = "Co słychać?"
        self.fields['snippet'].label = "Jak byś opisał temat jednym zdaniem?"
        self.fields['image'].label = "Dodaj Zdjęcie"

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category', 'content', 'snippet']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = "Tytuł"
        self.fields['category'].label = "Kategoria"
        self.fields['content'].label = "Co słychać?"
        self.fields['snippet'].label = "Jak byś opisał temat jednym zdaniem?"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user_id', 'type':'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['content'].label = "Co sądzisz?"

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditCommentForm, self).__init__(*args, **kwargs)

        self.fields['content'].label = "Co zmieniamy?"