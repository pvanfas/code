urlpatterns = [
	# other urls

    url(r'^customer/create/$', views.create_customer, name='create_customer'),
    url(r'^customers/$', views.customers, name='customers'),
    url(r'^customer/edit/(?P<pk>.*)/$', views.edit_customer, name='edit_customer'),
    url(r'^customer/view/(?P<pk>.*)/$', views.customer, name='customer'),
    url(r'^customer/delete/(?P<pk>.*)/$', views.delete_customer, name='delete_customer'),
    url(r'^customer/delete-selected/$', views.delete_selected_customers, name='delete_selected_customers'),
]