from django.urls import path

from . import views


app_name = "latihan"

urlpatterns = [
    path("", views.home, name="home"),
    path("latihan/css-selectors/", views.css_selectors_latihan, name="css_selectors"),
    path("latihan/greeting/<str:name>/", views.greeting, name="greeting"),
    path("latihan/orm/", views.orm_latihan, name="orm"),
    path("latihan/fetch-books/", views.fetch_books_latihan, name="fetch_books"),
    path("latihan/debounce/", views.debounce_latihan, name="debounce"),
    path("latihan/debug-fetch/", views.debug_fetch_latihan, name="debug_fetch"),
    path("latihan/product-form/", views.product_create, name="product_create"),
    path("latihan/table-debug/", views.table_debug_latihan, name="table_debug"),
    path(
        "latihan/documents/<int:document_id>/",
        views.document_detail,
        name="document_detail",
    ),
    path("latihan/events/", views.event_debug_latihan, name="events"),
    path("latihan/session-cookie/", views.session_cookie_latihan, name="session_cookie"),
    path("latihan/session-cookie/reset/", views.reset_session_latihan, name="reset_session"),
    path("latihan/search-flow/", views.search_flow_latihan, name="search_flow"),
    path("api/books/", views.books_api, name="books_api"),
    path("api/profile/", views.profile_api, name="profile_api"),
    path("api/products/", views.products_api, name="products_api"),
]

