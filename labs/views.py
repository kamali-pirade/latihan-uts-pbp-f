from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_POST

from .forms import ProductForm
from .models import Document, Product


LATIHAN = [
    ("01", "CSS selector", "/latihan/css-selectors/", "Manual: Elements + Styles"),
    ("02", "URL, View, Template", "/latihan/greeting/Budi/", "Test: test_latihan02_greeting"),
    ("03", "Django ORM", "/latihan/orm/", "Shell + query log"),
    ("04", "Fetch dan DOM", "/latihan/fetch-books/", "Manual: Console + Network"),
    ("05", "Debounce", "/latihan/debounce/", "Manual: counter pemanggilan"),
    ("06", "Debug Fetch", "/latihan/debug-fetch/", "Manual: Console + Network"),
    ("07", "Debug ModelForm", "/latihan/product-form/", "Test: test_latihan07_product_form"),
    ("08", "Debug tabel", "/latihan/table-debug/", "Manual: Elements + Console"),
    ("09", "Object authorization", "/latihan/documents/1/?as_user=alice", "Test: test_latihan09_document_access"),
    ("10", "Event listener", "/latihan/events/", "Manual: Console"),
    ("11", "Session dan cookie", "/latihan/session-cookie/", "Application > Cookies"),
    ("12", "Alur pencarian", "/latihan/search-flow/", "Network + DOM"),
]


def home(request):
    return render(request, "labs/home.html", {"latihan_list": LATIHAN})


def css_selectors_latihan(request):
    return render(request, "labs/css_selectors.html")


def greeting(request, name):
    # TODO LATIHAN 02:
    # 1. Ganti response sementara ini dengan render().
    # 2. Kirim `name` melalui context.
    # 3. Tampilkan `Halo, <nama>!` di greeting.html.
    return HttpResponse("TODO LATIHAN 02: hubungkan URL, view, dan template", status=501)


def orm_latihan(request):
    products = Product.objects.all()
    return render(request, "labs/orm_lab.html", {"products": products})


def fetch_books_latihan(request):
    return render(request, "labs/fetch_books.html")


def debounce_latihan(request):
    return render(request, "labs/debounce.html")


def debug_fetch_latihan(request):
    return render(request, "labs/debug_fetch.html")


def product_create(request):
    if request.method == "POST":
        # TODO LATIHAN 07: bind `request.POST` ke ProductForm.
        form = ProductForm()

        # TODO LATIHAN 07: panggil method validasi dan simpan object jika valid.
        if form.is_valid:
            return redirect("latihan:product_create")
    else:
        form = ProductForm()

    return render(
        request,
        "labs/product_form.html",
        {"form": form, "products": Product.objects.all()},
    )


def table_debug_latihan(request):
    return render(request, "labs/table_debug.html")


def document_detail(request, document_id):
    username = request.GET.get("as_user", "alice")
    simulated_user = get_object_or_404(get_user_model(), username=username)
    # TODO LATIHAN 09 (sengaja rentan): batasi query berdasarkan simulated_user.
    document = get_object_or_404(Document, pk=document_id)
    return render(
        request,
        "labs/document_detail.html",
        {"document": document, "simulated_user": simulated_user},
    )


def event_debug_latihan(request):
    return render(request, "labs/event_debug.html")


def session_cookie_latihan(request):
    visits = request.session.get("latihan_visits", 0) + 1
    request.session["latihan_visits"] = visits
    theme = request.COOKIES.get("latihan_theme", "belum tersedia")
    response = render(
        request,
        "labs/session_cookie.html",
        {"visits": visits, "theme": theme},
    )
    if "latihan_theme" not in request.COOKIES:
        response.set_cookie("latihan_theme", "dark", max_age=3600, samesite="Lax")
    return response


@require_POST
def reset_session_latihan(request):
    request.session.flush()
    response = redirect("latihan:session_cookie")
    response.delete_cookie("latihan_theme")
    return response


def search_flow_latihan(request):
    return render(request, "labs/search_flow.html")


@require_GET
def books_api(request):
    books = [
        {"title": "Belajar Django", "author": "Alya"},
        {"title": "Dasar JavaScript", "author": "Bima"},
        {"title": "HTML dan CSS", "author": "Citra"},
    ]
    return JsonResponse(books, safe=False)


@require_GET
def profile_api(request):
    if request.GET.get("mode") == "error":
        return JsonResponse({"detail": "Simulasi server error"}, status=500)
    return JsonResponse({"name": "Mahasiswa PBP", "role": "student"})


@require_GET
def products_api(request):
    keyword = request.GET.get("q", "").strip()
    products = Product.objects.all()
    if keyword:
        products = products.filter(name__icontains=keyword)
    data = list(products.values("id", "name", "stock", "price"))
    return JsonResponse({"results": data})

