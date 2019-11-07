
# ALTER AJAX SUBMISSION --------------------------------------------------------------------------------

# Ensure the correctness of media, static file path
    os.path.join(BASE_DIR, "media")
# Add models field
    photo = models.FileField(blank=True,null=True,upload_to="customers/")
    
# Add to create templates
    <div class="form-group fg-line">
        <label for="{{ form.photo.id_for_label }}">
            {{ form.photo.label }}
            {% if form.photo.field.required %}
                <small class="star">*</small>
            {% endif %}

            {% if form.photo.help_text %}
                <span data-original-title="Field Info" title="" data-content="{{ form.photo.help_text }}" data-placement="left" data-toggle="popover" data-trigger="hover" class="help-text-icon zmdi zmdi-info-outline"></span>
            {% endif %}
        </label>
        {{ form.photo }}

        {% if form.photo.errors %}
            <label class="error">{{ form.photo.errors.as_text }}</label>
        {% endif %}
    </div>

# Migrate changes
    python manage.py makemigrations
    python manage.py migrate
    
#Add to customer view template
    {% if instance.customer %}
        <div class="list-group-item media">
            <div class="media-body">
                <div class="lgi-heading">Photo</div>
                <img src="{{instance.photo.url}}" alt="{{instance.name}}" class="img-responsive">
            </div>
        </div>
    {% else %}
        <p class="text-center">Photo not Found</p>
    {% endif %}
    
# Remove form classes 
    class ="ajax reset redirect skip_empty_row not_allowed_without_formset"
    
# Add attr
    enctype="multipart/form-data"
    
# Change View request
    form = CustomerForm(request.POST,request.FILES)
    
# Replace view response data with HttpResponseRedirect
    return HttpResponseRedirect(reverse('customers:customer',kwargs={"pk":data.pk}))

# Display Customer filled form on else response
    form = CustomerForm(request.POST,request.FILES)
    context = {
        "form" : form,
        "title" : "Create Customer",
        "redirect" : True,

        "is_need_select_picker" : True,
        "is_need_popup_box" : True,
        "is_need_custom_scroll_bar" : True,
        "is_need_wave_effect" : True,
        "is_need_bootstrap_growl" : True,
        "is_need_chosen_select" : True,
        "is_need_grid_system" : True,
        "is_need_datetime_picker" : True,
        "is_need_animations": True,
        "is_dashboard" :True
    }
    return render(request,"customers/entry.html", context)
    
# Final view
def create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.creator = request.user
            data.updater = request.user
            data.auto_id = get_auto_id(Customer)
            form.save()

            return HttpResponseRedirect(reverse('customers:customer',kwargs={"pk":data.pk}))
        else:
            message = generate_form_errors(form,formset=False)

            form = CustomerForm(request.POST)
            context = {
                "form" : form,
                "title" : "Create Customer",
                "redirect" : True,

                "is_need_select_picker" : True,
                "is_need_popup_box" : True,
                "is_need_custom_scroll_bar" : True,
                "is_need_wave_effect" : True,
                "is_need_bootstrap_growl" : True,
                "is_need_chosen_select" : True,
                "is_need_grid_system" : True,
                "is_need_datetime_picker" : True,
                "is_need_animations": True,
                "is_dashboard" :True
            }
            return render(request,"customers/entry.html", context)
    else:

        form = CustomerForm()
        context = {
            "form" : form,
            "title" : "Create Customer",
            "redirect" : True,

            "is_need_select_picker" : True,
            "is_need_popup_box" : True,
            "is_need_custom_scroll_bar" : True,
            "is_need_wave_effect" : True,
            "is_need_bootstrap_growl" : True,
            "is_need_chosen_select" : True,
            "is_need_grid_system" : True,
            "is_need_datetime_picker" : True,
            "is_need_animations": True,
            "is_dashboard" :True
        }

        return render(request,"customers/entry.html", context)

