from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404

from .models import Brand, Supplier
from .forms import BrandForm

def home(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BrandForm()
    return render(request, "home.html", {
        "form": BrandForm(),
        "brands": Brand.objects.select_related('supplier__country').all().order_by("-id")
    })

def hx_get_country(request):
    supplier = get_object_or_404(Supplier, id=request.GET.get("supplier"))

    return render(request, "home.html#country_field", {
        "country": supplier.country
    })