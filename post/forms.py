from django import forms

from post.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        min_length=3, 
        required=True, 
        label='Заголовок',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }
            )
        )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            }
        )
    )
    image = forms.ImageField(
        required=False,
        label='Изображение',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'python' in title:
            # self.errors['title'] = ['Python в заголовке недопустим!']
            raise forms.ValidationError('Python в заголовке недопустим!')
        
        return title
    
    def clean(self):
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')

        if title == content:
            raise forms.ValidationError('Заголовок и текст не должны совпадать!')
        
        return self.cleaned_data
    

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите заголовок'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите текст'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rate': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Текст',
            'image': 'Изображение'
        }
