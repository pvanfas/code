pip install django-autocomplete-light==3.2.10
pip install six

#installed apps before contrib.admin
'dal',
'dal_select2',

#on required views.py
from dal import autocomplete


class CustomerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Customer.objects.none()

        items = Customer.objects.filter(is_deleted=False)
        #items = Customer.objects.all()

        if self.q:
            query = self.q
            items = items.filter(Q(name__icontains=query) | Q(phone__icontains=query) | Q(email__icontains=query) | Q(address__icontains=query))
            #items = items.filter(name__istartswith=self.q)
        return items


#on urls
from customers.views import CustomerAutocomplete

urlpatterns = [
    url(r'^customer-autocomplete/$',CustomerAutocomplete.as_view(),name='customer_autocomplete',),
]

#on sale-forms change widget field
from dal import autocomplete

autocomplete.ModelSelect2(url='customers:customer_autocomplete',attrs={'data-placeholder': 'Customer','data-minimum-input-length': 1},),

#on template after all script
{{ form.media }}


#Removing close button in autocomplete repeator
row.find('.sale_item_select').val(null).trigger('change');
row.find('.select2-selection').click();
