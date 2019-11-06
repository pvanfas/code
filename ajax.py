# FORM AJAX --------------------------------------------------------------------------------

# template script
$('#id_customer').on('change', function(){
	var $this = $(this);
	get_customer_data($this);
});

function get_customer_data(element){
	var customer_id = element.val();

	if (customer_id != undefined || customer_id != ""){
		var url = "{% url 'customers:get_customer' %}";
		$.ajax({
           type : "GET",
           url : url,
           dataType :'json',
           data : {
               "id" : customer_id,
           },
           success : function(data){
               var status = data['status'];
			   if(status =='true'){
				   // assign object key-values into variables
				   var name = data.name;
				   var email = data.email;
				   var phone = data.phone;
				   var address = data.address;

					// insert var value into input field
				   $("#customer_name").val(name);
				   $("#customer_email").val(email);
				   $("#customer_phone").val(phone);
				   $("#customer_address").val(address);
			   }
           },
           error : function(data){
               var status = data['status'];
           }
       });
	};
};

# define url in customers
url(r'^get-customer/$', views.get_customer, name='get_customer'),

#write view in customers
def get_customer(request):
    pk = request.GET.get('id')
    if Customer.objects.filter(pk=pk).exists():
        customer =  Customer.objects.get(pk=pk)

        response_data = {
            "status" : "true",
            "name" : customer.name,
            "address" : customer.address,
            "phone" : customer.phone,
            "email" : customer.email,
            "pk" : str(customer.pk)
        }
    else:
        response_data = {
            "status" : "false",
            "message" : "Customer does not exist."
        }
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')
	

# FORMSET AJAX --------------------------------------------------------------------------------

# template script
$('.sale_item select').on('change', function(){
	var $this = $(this);
	getProductInfo($this);
});

function getProductInfo($selector){
	var url = "{% url 'products:get_product' %}";
	var product_id = $selector.val();
	var $parent = $selector.parents('tr.form_set_row');
	if(product_id != '' && product_id != null){
		$.ajax({
		   type : "GET",
		   url : url,
		   dataType :'json',
		   data : {
			   "id" : product_id,
		   },
		   success : function(data){
			   var status = data['status'];
			   if(status =='true'){
				   var stock = data.stock;
				   $parent.find('.sale_item_stock input').val(stock);
			   }
		   },
		   error : function(data){
			   var status = data['status'];
		   }
	   });
   }
}

# define url in customers
url(r'^get-product/$', views.get_product, name='get_product'),

#write view in customers
class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Product.objects.none()

        items = Product.objects.filter(is_deleted=False)

        if self.q:
            query = self.q
            items = items.filter(Q(name__icontains=query))

        return items


