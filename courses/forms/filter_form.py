from django import forms

class filterForm(forms.Form):
    SORT_CHOICES = [
        ('name_asc', 'Name (A-Z)'),
        ('name_desc', 'Name (Z-A)'),
        ('price_asc', 'Price (Low to High)'),
        ('price_desc', 'Price (High to Low)'),
        ('date_asc', 'Date (Oldest to Newest)'),
        ('date_desc', 'Date (Newest to Oldest)'),
    ]
    
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, widget=forms.RadioSelect, required=False)