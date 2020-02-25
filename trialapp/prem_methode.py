# # def ProductDetail(request):
# #     queryset = Product.objects.all()
# #     params = json.loads(request.body)
    
# #     if request.method == "POST":
# #         Product.objects.create(**params)
# #         return JsonResponse({"detail":"Success","success":True})
    
# #     if request.method == "GET":
# #         response = []
# #         for object in queryset:
# #             response.append({
# #                 "id":object.id,
# #                 "productname":object.productname
# #             })
# #         return JsonResponse({"detail":"Success","success":True,"response":response})
    
# #     if request.method == "PUT":
# #         Product.objects.get(id = params['id']).update(**params)
# #         return JsonResponse({"detail":"Success PUT","success":True})

# #     if request.method == "PATCH":
# #         Product.objects.get(id = params['id']).update(**params)
# #         return JsonResponse({"detail":"Success PATCH","success":True})
# #     if request.method == "DELETE":
# #         Product.objects.get(id = params['id']).delete()
# #         return JsonResponse({"detail":"Success  DELETE","success":True})


# # 