# Search with query

(customers / views.py)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
@renderer_classes((JSONRenderer,))
def customers(request):
    instances = Customer.objects.filter(is_deleted=False)
    # ---- addition starts ---
    query = Customer.objects.filter(is_deleted=False)
    if query:
        instances = instances.filter(name__icontains=query)
    # ---- addition ends ---

    serialized = CustomerSerializer(instances, many=True, context={"request": request})

    response_data = {"statusCode": 6000, "data": serialized.data}

    return Response(response_data, status=status.HTTP_200_OK)
