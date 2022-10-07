urlpatterns = [
    # other urls
    url(r"^user/create/(?P<pk>.*)/$", views.create_user, name="create_user"),
]
