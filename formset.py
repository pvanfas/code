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


