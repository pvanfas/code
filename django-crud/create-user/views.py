@check_mode
@login_required
def create_user(request,pk):  
    instance = get_object_or_404(Customer.objects.filter(pk=pk,is_deleted=False))
    
    if request.method == "POST":
        form = UserForm(request.POST)
        response_data = {} 
        message = ""  
        data = []  
        emails = request.POST.get('email')
        username = request.POST.get('username')
        email = str(emails)
        error = False
        
         if User.objects.filter(email=email).exists():
            error = True
            message += "This email already exists."

        if not error:
            if form.is_valid():                    
                data = form.save(commit=False)
                data.email = email
                data.save()               
                
                Customer.objects.filter(pk=pk,is_deleted=False).update(user=data)

                group = Group.objects.get(name="customer")
                data.groups.add(group)

                response_data = {
                    'status' : 'true',     
                    'title' : "User Created",       
                    'redirect' : 'true', 
                    'redirect_url' : reverse('customers:customer', kwargs={"pk":pk}),
                    'message' : "User Created Successfully"
                }

            else:
                error = True
                message = ''            
                message += generate_form_errors(form,formset=False)   
                response_data = {
                    'status' : 'false',
                    'stable' : 'true',
                    'title' : "Form validation error",
                    "message" : message
                }

        else:
            response_data = {
                'status' : 'false',     
                'title' : "Can't create this user",       
                'redirect' : 'true', 
                'redirect_url' : reverse('users:create_user', kwargs={"pk":pk}),
                'message' : message,

                "is_need_popup_box": True,
                "is_need_custom_scroll_bar": True,
                "is_need_wave_effect": True,
                "is_need_bootstrap_growl": True,
                "is_need_animations": True,
                "is_need_grid_system": True,
                "is_need_select_picker": True,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else: 
        customer_email = instance.email
        customer_username_auto = customer_email.split("@")[0]
        form = UserForm(initial={'email':instance.email,'username':customer_username_auto})
        
        context = {
            "form" : form,
            "title" : "Create User",
            "redirect": "true",

            "is_need_select_picker": True,
            "is_need_popup_box": True,
            "is_need_custom_scroll_bar": True,
            "is_need_wave_effect": True,
            "is_need_bootstrap_growl": True,
            "is_need_grid_system": True,

        }
        return render(request, 'users/create_user.html', context)