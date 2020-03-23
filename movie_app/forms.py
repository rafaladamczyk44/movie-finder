from django import forms

MOVIE_GENRES = [
    ('none', '...or...'),
    ('popular', 'GET SOMETHING POPULAR'),
    ]

class SearchForm(forms.Form):
    search = forms.CharField(
        label="", 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Type the keyword here...'}))

    #"OR...."
    
    movie_genre = forms.CharField( 
        label='',
        required=False,
        widget=forms.Select(choices=MOVIE_GENRES))


    search.widget.attrs.update({'class': 'form-element'})
    movie_genre.widget.attrs.update({'class': 'form-element'})
