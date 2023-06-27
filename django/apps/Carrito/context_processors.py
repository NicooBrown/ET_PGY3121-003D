def totalCompra(request):
    total = 0
    if request.user.is_authenticated:
        if request.session["cart"]:
            for key, value in request.session["cart"].items():
                total += int(value["acumulado"])
    return {"totalCompra": total}