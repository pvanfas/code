from django.conf import settings
from django.template.loader import render_to_string
from users.functions import send_email


@check_mode
@login_required
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():

            auto_id = get_auto_id(Customer)

            data = form.save(commit=False)
            data.creator = request.user
            data.updater = request.user
            data.auto_id = auto_id
            data.save()

            # Send a mail to admin : New customer added with customer name and details

            template_name = "emails/email.html"
            subject = "New customer created"  # Subject of the mail
            content = "New Customer Added"
            email = settings.ADMIN_EMAIL
            context = {
                "request": request,
                "email": email,
                "subject": subject,
                "content": content,
            }
            html_content = render_to_string(template_name, context)
            send_email(email, subject, content, html_content)

            response_data = {
                "status": "true",
                "title": "Successfully Created",
                "message": "Customer created successfully.",
                "redirect": "true",
                "redirect_url": reverse("module_name:customer", kwargs={"pk": data.pk}),
            }

        else:
            message = generate_form_errors(form, formset=False)

            response_data = {
                "status": "false",
                "stable": "true",
                "title": "Form validation error",
                "message": message,
            }

        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )

    else:
        form = CustomerForm()
        context = {
            "title": "Create Customer",
            "form": form,
            "url": reverse("module_name:create_customer"),
            "is_need_select_picker": True,
            "is_need_popup_box": True,
            "is_need_custom_scroll_bar": True,
            "is_need_wave_effect": True,
            "is_need_bootstrap_growl": True,
            "is_need_chosen_select": True,
            "is_need_grid_system": True,
            "is_need_datetime_picker": True,
        }
        return render(request, "module_name/entry_customer.html", context)
