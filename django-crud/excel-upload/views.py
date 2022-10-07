import xlrd


@check_mode
@login_required
def upload_students(request, pk):
    instance = get_object_or_404(Division.objects.filter(pk=pk))

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            input_excel = request.FILES["file"]
            book = xlrd.open_workbook(file_contents=input_excel.read())
            sheet = book.sheet_by_index(0)

            dict_list = []
            keys = [
                str(sheet.cell(0, col_index).value) for col_index in xrange(sheet.ncols)
            ]
            for row_index in xrange(1, sheet.nrows):
                d = {
                    keys[col_index]: str(sheet.cell(row_index, col_index).value)
                    for col_index in xrange(sheet.ncols)
                }
                dict_list.append(d)

            is_ok = True
            message = ""
            row_count = 2

            for item in dict_list:
                name = item["name"]
                gender = item["gender"]

                if not Student.objects.filter(code=code, is_deleted=False).exists():
                    auto_id = get_auto_id(Student)
                    instance = Student.objects.create(
                        name=name,
                        gender=gender,
                        division=instance,
                        auto_id=auto_id,
                        creator=request.user,
                        updater=request.user,
                    )

            return HttpResponseRedirect(reverse("students:students", kwargs={"pk": pk}))
        else:
            form = FileForm()
            title = "Upload Students in division %s" % (instance.name)

            context = {
                "form": form,
                "title": title,
                "is_need_select_picker": True,
                "is_need_popup_box": True,
                "is_need_custom_scroll_bar": True,
                "is_need_wave_effect": True,
                "is_need_bootstrap_growl": True,
                "is_need_chosen_select": True,
                "is_need_grid_system": True,
                "is_need_datetime_picker": True,
            }
            return render(request, "students/upload_students.html", context)
    else:
        form = FileForm()
        title = "Upload Students in division %s" % (instance.name)

        context = {
            "form": form,
            "title": title,
            "is_need_select_picker": True,
            "is_need_popup_box": True,
            "is_need_custom_scroll_bar": True,
            "is_need_wave_effect": True,
            "is_need_bootstrap_growl": True,
            "is_need_chosen_select": True,
            "is_need_grid_system": True,
            "is_need_datetime_picker": True,
        }
        return render(request, "students/upload_students.html", context)
