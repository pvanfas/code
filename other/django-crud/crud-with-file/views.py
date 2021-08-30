@check_mode
@login_required
def create_customer(request):    
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        
        if form.is_valid(): 
            
            auto_id = get_auto_id(Customer)
            
            data = form.save(commit=False)
            data.creator = request.user
            data.updater = request.user
            data.auto_id = auto_id
            data.save()  

            return HttpResponseRedirect(reverse('module_name:customer',kwargs={'pk':data.pk})) 
        
        else:            
            message = generate_form_errors(form,formset=False)     
                    
            form = CustomerForm(request.POST)
            
            context = {
                "title" : "Create Customer",
                "form" : form,
                "url" : reverse('module_name:create_customer'),
                "message"  message,

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
    
    else:
        form = CustomerForm()
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
    
    context = {
        "instance" : instance,
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

    if request.method == 'POST':
            
        form = CustomerForm(request.POST,request.FILES,instance=instance)
        
        if form.is_valid():  
            
            data = form.save(commit=False)
            data.updater = request.user
            data.date_updated = datetime.datetime.now()
            data.save() 

            return HttpResponseRedirect(reverse('module_name:customer',kwargs={'pk':data.pk}))   
        else:

            message = generate_form_errors(form,formset=False)     
            
            form = CustomerForm(instance=instance)
        
            context = {
                "form" : form,
                "title" : "Edit Customer : " + instance.name,
                "instance" : instance,
                "message" : message,
                "url" : reverse('module_name:edit_customer',kwargs={'pk':instance.pk}),
                "redirect" : True,

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
            return render(request, 'module_name/entry_customer.html', context)

    else: 
        form = CustomerForm(instance=instance)
        
        context = {
            "form" : form,
            "title" : "Edit Customer : " + instance.name,
            "instance" : instance,
            "url" : reverse('module_name:edit_customer',kwargs={'pk':instance.pk}),
            "redirect" : True,

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