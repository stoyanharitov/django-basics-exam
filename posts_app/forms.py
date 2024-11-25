from django import forms

from posts_app.models import Post
from reg_exam_main.mixins import ReadOnlyMixin


class PostFormBase(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }
        widgets = {'title': forms.TextInput(attrs={'placeholder':'Put an attractive and unique title...'}),
                   'content': forms.Textarea(attrs={'placeholder':'Share some interesting facts about your adorable pets...'})
                   }


class PostCreateForm(PostFormBase):
    class Meta(PostFormBase.Meta):
        model = Post
        exclude = ('author',)



class PostEditForm(PostFormBase):
    class Meta(PostFormBase.Meta):
        model = Post
        exclude = ('author',)
        help_texts = {
            'image_url': ''}


class PostDeleteForm(ReadOnlyMixin, PostFormBase):
    read_only_fields = [ 'title', 'image_url', 'content']

    class Meta(PostFormBase.Meta):
        model = Post
        exclude = ('author',)
        help_texts = {
            'image_url': ''}
