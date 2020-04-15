```
function show_loader() {
    $('body').append('<div class="popup-box"><div class="preloader pl-xxl"><svg viewBox="25 25 50 50" class="pl-circular"><circle r="20" cy="50" cx="50" class="plc-path"/></svg></div></div><span class="popup-bg"></span>');
}
```

```
function remove_popup() {
    $('.popup-box,.popup-bg').remove();
}
```

```
$(document).ready(function() {

    $(document).on('submit','form.ajax_file', function(e) {
        e.preventDefault();
        var $this = $(this);
        var data = new FormData(this);
        var isReset = $this.hasClass('reset');
        var isReload = $this.hasClass('reload');
        var isRedirect = $this.hasClass('redirect');
        show_loader();

        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            dataType: "json",

            success: function(data) {
                remove_popup();

                var status = data.status;
                var title = data.title;
                var message = data.message;
                var pk = data.pk;
                var redirect = data.redirect;
                var redirect_url = data.redirect_url;

                if (status == "true") {
                    if (title) {title = title;}
                    else {title = "Success";}
                    swal({title: title,text: message,type: "success"});

                    swal({title: title,text: message,type: "success"},
                    function () {
                        if (isRedirect && redirect == 'true') {
                            window.location.href = redirect_url;
                        }
                        if (isReload) {
                            window.location.reload();
                        }
                        if (isReset) {
                            $this[0].reset();
                        }
                    });
                }
                else {
                    title = "An Error Occurred";
                    swal(title, message, "error");
                }
            },
            error: function(data) {
                remove_popup();
                var title = "An error occurred";
                var message = "Upload a valid image. The file you uploaded was either not an image or a corrupted image.";
                swal(title, message, "error");
            }
        });
    });
```

```

$(document).on('submit','form.ajax', function(e) {
    e.preventDefault();
    var $this = $(this);
    var data = new FormData(this);
    var isReset = $this.hasClass('reset');
    var isReload = $this.hasClass('reload');
    var isRedirect = $this.hasClass('redirect');
    show_loader();

    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",

        success: function(data) {
            remove_popup();

            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;
            var redirect = data.redirect;
            var redirect_url = data.redirect_url;

            if (status == "true") {
                if (title) {title = title;}
                else {title = "Success";}
                swal({title: title,text: message,type: "success"});

                swal({title: title,text: message,type: "success"},
                function () {
                    if (isRedirect && redirect == 'true') {
                        window.location.href = redirect_url;
                    }
                    if (isReload) {
                        window.location.reload();
                    }
                    if (isReset) {
                        $this[0].reset();
                        $this.find('.select2-hidden-accessible').val(null).trigger('change').click();
                    }
                });
            }
            else {
                title = "An Error Occurred";
                swal(title, message, "error");
            }
        },
        error: function(data) {
            remove_popup();
            var title = "An error occurred";
            var message = ".";
            swal(title, message, "error");
        }
    });
});

```

    });

});

```
