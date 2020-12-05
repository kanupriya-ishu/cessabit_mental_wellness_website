from django import forms
from article.models import Post

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            # The class here is a CSS class.
            'title' : forms.TextInput(attrs={'class':'TextInputClass'}), #TextInputClass is our class
            'text'  : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}), #postcontent class is our class
        }
