@check_mode
@login_required
def create_customer(request): 
    CustomerAddressFormset = formset_factory(CustomerAddressForm)   
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        customer_address_formset = CustomerAddressFormset(request.POST,prefix='customer_address_formset')

        if form.is_valid() and customer_address_formset.is_valid(): 
            
            auto_id = get_auto_id(Customer)
            
            data = form.save(commit=False)
            data.creator = request.user
            data.updater = request.user
            data.auto_id = auto_id
            data.save() 

            # If CustomerAddress is models.Model
            for f in customer_address_formset:
                field_name = f.cleaned_data['field_name']
                
                CustomerAddress.objects.create(      
                    customer = data,
                    field_name = field_name
                )  

            # If CustomerAddress is BaseModel
            for f in customer_address_formset:
                field_name = f.cleaned_data['field_name']
                auto_id = get_auto_id(CustomerAddress)
                
                CustomerAddress.objects.create(      
                    customer = data,
                    field_name = field_name,
                    auto_id = auto_id,
                    creator = request.user,
                    updater = request.user
                )

            response_data = {
                "status" : "true",
                "title" : "Successfully Created",
                "message" : "Customer created successfully.",
                "redirect" : "true",
                "redirect_url" : reverse('module_name:customer',kwargs={'pk':data.pk})
            }   
        
        else:            
            message = generate_form_errors(form,formset=False) 
            message = generate_form_errors(customer_address_formset,formset=True)     
                    
            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
                "message" : message
            }   
        
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    
    else:
        form = CustomerForm()
        customer_address_formset = CustomerAddressFormset(prefix='customer_address_formset')
        context = {
            "title" : "Create Customer",
            "form" : form,
            "url" : reverse('module_name:create_customer'),

            "is_need_select_picker" : True,
            "is_need_popup_box" : True,
            "is_need_custom_scroll_bar" : True,
            "is_need_wave_effect" : True,
            "is_need_bootstrap_growl" : True,
            "is_need_chosen_select" : True,
            "is_need_grid_system" : True,
            "is_need_datetime_picker" : True,

        }
        return render(request,'module_name/entry_customer.html',context)


@check_mode
@login_required
def customers(request):    
    instances = Customer.objects.filter(is_deleted=False)
    title = "Customers"
    
    query = request.GET.get("q")
    if query:
        instances = instances.filter(Q(name__icontains=query))
        title = "Customers - %s" %query    
        
    context = {
        "instances" : instances,
        'title' : title,

        "is_need_select_picker" : True,
        "is_need_popup_box" : True,
        "is_need_custom_scroll_bar" : True,
        "is_need_wave_effect" : True,
        "is_need_bootstrap_growl" : True,
        "is_need_chosen_select" : True,
        "is_need_grid_system" : True,
        "is_need_animations": True,
        "is_need_datetime_picker" : True,

    }
    return render(request,'module_name/customers.html',context) 


@check_mode
@login_required
def customer(request,pk):    
    instance = get_object_or_404(Customer.objects.filter(pk=pk,is_deleted=False))
    customer_addresses = CustomerAddress.objects.filter(customer=instance)
    
    context = {
        "instance" : instance,
        "customer_addresses" : customer_addresses,
        "title" : "Customer : " + instance.name,

        "is_need_select_picker" : True,
        "is_need_popup_box" : True,
        "is_need_custom_scroll_bar" : True,
        "is_need_wave_effect" : True,
        "is_need_bootstrap_growl" : True,
        "is_need_chosen_select" : True,
        "purchases" : True,
        "is_need_grid_system" : True,
        "is_need_datetime_picker" : True,

    }
    return render(request,'module_name/customer.html',context)


@check_mode
@login_required
def edit_customer(request,pk):    
    instance = get_object_or_404(Customer.objects.filter(pk=pk,is_deleted=False))

    if CustomerAddress.objects.filter(customer=instance).exists():
        extra = 0
    else:
        extra = 1
        
    CustomerAddressFormset = inlineformset_factory(
                                            Customer, 
                                            CustomerAddress,
                                            can_delete=True,
                                            form=CustomerAddressForm,
                                            extra=extra
                                        )

    if request.method == 'POST':
            
        form = CustomerForm(request.POST,instance=instance)
        
        if form.is_valid():  
            
            data = form.save(commit=False)
            data.updater = request.user
            data.date_updated = datetime.datetime.now()
            data.save()  

            customer_items = customer_address_formset.save(commit=False)
            for item in customer_items:
                customer = item.data
                item.save()

            for obj in customer_address_formset.deleted_objects:
                obj.delete()
            
            response_data = {
                "status" : "true",
                "title" : "Successfully Updated",
                "message" : "Customer Successfully Updated.",
                "redirect" : "true",
                "redirect_url" : reverse('module_name:customer',kwargs={'pk':data.pk})
            }   
        else:
            message = generate_form_errors(form,formset=False) 
            message = generate_form_errors(customer_address_formset,formset=True)     
                    
            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
                "message" : message
            }  
            
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')

    else: 
        form = CustomerForm(instance=instance)
        customer_address_formset = CustomerAddressFormset(prefix='customer_address_formset',instance=instance)
        
        context = {
            "form" : form,
            "title" : "Edit Customer : " + instance.name,
            "instance" : instance,
            "customer_address_formset" : customer_address_formset,
            "url" : reverse('module_name:edit_customer',kwargs={'pk':instance.pk}),
            "redirect" : True,

            "is_need_select_picker" : True,
            "is_need_popup_box" : True,
            "is_need_custom_scroll_bar" : True,
            "is_need_wave_effect" : True,
            "is_need_bootstrap_growl" : True,
            "is_need_chosen_select" : True,
            "is_need_grid_system" : True,
            "is_need_datetime_picker" : True,
        }
        return render(request, 'module_name/entry_customer.html', context)


@check_mode
@login_required
def delete_customer(request,pk):    
    instance = get_object_or_404(Customer.objects.filter(pk=pk,is_deleted=False))
    instance.is_deleted = True
    instance.save()
    
    response_data = {
        "status" : "true",
        "title" : "Successfully Deleted",
        "message" : "Customer Successfully Deleted.",
        "redirect" : "true",
        "redirect_url" : reverse('module_name:customers')
    }
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')


@check_mode
@login_required
def delete_selected_customers(request):
    pks = request.GET.get('pk')
    if pks:
        pks = pks[:-1]
        
        pks = pks.split(',')
        for pk in pks:      
            instance = get_object_or_404(Customer.objects.filter(pk=pk,is_deleted=False)) 
            instance.is_deleted = True
            instance.save()
    
        response_data = {
            "status" : "true",
            "title" : "Successfully Deleted",
            "message" : "Selected Customer(s) Successfully Deleted.",
            "redirect" : "true",
            "redirect_url" : reverse('module_name:customers')
        }
    else:
        response_data = {
            "status" : "false",
            "title" : "Nothing selected",
            "message" : "Please select some items first.",
        }
        
    return HttpResponse(json.dumps(response_data), content_type='application/javascript')