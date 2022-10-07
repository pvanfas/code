// Ajaxify Django

/*
Ajax is a set of web development techniques using many web technologies on the client side to create asynchronous web 
applications. With Ajax, web applications can send and retrieve data from a server asynchronously without interfering 
with the display and behavior of the existing page. Ajax allows web pages to be updated asynchronously by exchanging 
small amounts of data with the server behind the scenes
*/

// Form Submission
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@9.15.3/dist/sweetalert2.all.min.js"></script>

<script>
    var isLoading = false;
    $(document).on("submit", "form.ajax", function (e) {
        e.preventDefault();
        var $this = $(this),
            data = new FormData(this),
            action_url = $this.attr("action"),
            reset = $this.hasClass("reset"),
            reload = $this.hasClass("reload"),
            redirect = $this.hasClass("redirect"),
            redirect_url = $this.attr("data-redirect");

        if (!isLoading) {
            isLoading = true;
            $.ajax({
                url: action_url,
                type: "POST",
                data: data,
                cache: false,
                contentType: false,
                processData: false,
                dataType: "json",
                success: function (data) {
                    var status = data.status;
                    var title = data.title;
                    var message = data.message;
                    var pk = data.pk;
                    if (status == "true") {
                        title ? (title = title) : (title = "Success");
                        Swal.fire({
                            title: title,
                            html: message,
                            icon: "success",
                        }).then(function () {
                            redirect && (window.location.href = redirect_url), reload && window.location.reload(), reset && window.location.reset();
                        });
                    } else {
                        title ? (title = title) : (title = "An Error Occurred");
                        Swal.fire({
                            title: title,
                            html: message,
                            icon: "error",
                        });
                    }
                },
                error: function (data) {
                    var title = "An error occurred",
                        message = "something went wrong";
                    Swal.fire({
                        title: title,
                        html: message,
                        icon: "error",
                    });
                },
            }).then(function (response) {
                isLoading = false;
            });
        }
    });

    $(document).on("click", ".action-button", function (e) {
        e.preventDefault();
        $this = $(this);
        var html = $this.attr("data-text");
        var icon = "question";
        var id = $this.attr("data-id");
        var url = $this.attr("href");
        var title = $this.attr("data-title");
        if (!title) {
            title = "Are you sure?";
        }

        Swal.fire({
            title: title,
            html: html,
            icon: icon,
            showCancelButton: true,
        }).then((result) => {
            if (result.value) {
                window.setTimeout(function () {
                    $.ajax({
                        type: "GET",
                        url: url,
                        dataType: "json",
                        data: { pk: id },

                        success: function (data) {
                            var message = data.message;
                            var status = data.status;
                            var reload = data.reload;
                            var redirect = data.redirect;
                            var redirect_url = data.redirect_url;
                            var title = data.title;

                            if (status == "true") {
                                title?title=title:title="Success";
                                Swal.fire({title:title,html:message,icon:"success"}).then(function(){"true"==redirect&&(window.location.href=redirect_url),"true"==reload&&window.location.reload()});
                            } else {
                                title?title=title:title="An Error Occurred";
                                Swal.fire({ title: title, html: message, icon: "error" });
                            }
                        },
                        error: function (data) {
                            var title = "An error occurred";
                            var message = "An error occurred. Please try again later.";
                            Swal.fire({ title: title, html: message, icon: "error" });
                        },
                    });
                }, 100);
            } else {
                console.log("action cancelled");
            }
        });
    });

    // Instant Action Button
    $(document).on("click", ".instant-action-button", function (e) {
        e.preventDefault();
        $this = $(this);
        var text = $this.attr("data-text");
        var icon = "success";
        var key = $this.attr("data-key");
        var url = $this.attr("data-url");
        var reload = $this.hasClass("reload");
        var reset = $this.hasClass("reset");
        var redirect = $this.hasClass("redirect");
        var title = $this.attr("data-title");
        var redirect_url = $this.attr("data-redirect");

        $.ajax({
            type: "GET",
            url: url,
            dataType: "json",
            data: { pk: key },

            success: function (data) {
                var status = data.status;
                var message = data.message;

                if (status == "true") {
                    title ? (title = title) : (title = "Success");

                    Swal.fire({ title: title, html: message, icon: "success" }).then(function () {
                        redirect && (window.location.href = redirect_url), reload && window.location.reload(), reset && window.location.reset();
                    });
                } else {
                    title ? (title = title) : (title = "An Error Occurred");
                    Swal.fire({ title: title, html: message, icon: "error" });
                }
            },
            error: function (data) {
                var title = "An error occurred";
                var message = "An error occurred. Please try again later.";
                Swal.fire({ title: title, html: message, icon: "error" });
            },
        });
    });

    // Export Button
    $(document).on("click", ".export-button", function (e) {
        // random data
        var request = new XMLHttpRequest();
        request.open("POST", url, true);
        request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
        request.responseType = "blob";

        request.onload = function (e) {
            if (this.status === 200) {
                let filename = "";
                let disposition = request.getResponseHeader("Content-Disposition");
                // check if filename is given
                if (disposition && disposition.indexOf("attachment") !== -1) {
                    let filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                    let matches = filenameRegex.exec(disposition);
                    if (matches != null && matches[1]) filename = matches[1].replace(/['"]/g, "");
                }
                let blob = this.response;
                if (window.navigator.msSaveOrOpenBlob) {
                    window.navigator.msSaveBlob(blob, filename);
                } else {
                    let downloadLink = window.document.createElement("a");
                    let contentTypeHeader = request.getResponseHeader("Content-Type");
                    downloadLink.href = window.URL.createObjectURL(
                        new Blob([blob], {
                            type: contentTypeHeader,
                        })
                    );
                    downloadLink.download = filename;
                    document.body.appendChild(downloadLink);
                    downloadLink.click();
                    document.body.removeChild(downloadLink);
                }
            } else {
                alert("Download failed.");
            }
        };
        request.send(data);
    });
</script>
