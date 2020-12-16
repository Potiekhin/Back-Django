from django.urls import path

from categories.views import ProductCategoriesView, EditProductCategoriesView, \
    EditSubProductCategoriesView, ProductSubCategoriesView

urlpatterns = [
    path('', ProductCategoriesView.as_view()),
    path('sub_category/<int:pk>', ProductSubCategoriesView.as_view()),
    path('edit_category/<int:pk>', EditProductCategoriesView.as_view()),
    path('edit_sub_category/<int:pk>', EditSubProductCategoriesView.as_view()),
]
