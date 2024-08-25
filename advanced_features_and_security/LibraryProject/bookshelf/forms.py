from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, help_text="Enter the title of the book")
    author = forms.CharField(max_length=100, help_text="Enter the author's name")
    published_date = forms.DateField(widget=forms.SelectDateWidget, help_text="Select the publication date")
    isbn = forms.CharField(max_length=13, help_text="Enter the 13-character ISBN number")

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)