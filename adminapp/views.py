from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from adminapp.forms import AdminShopUserUpdateForm, AdminShopUserCreateForm
from mainapp.models import ProductCategory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SetPageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["page_title"] = self.page_title
        return context


class ShopUserList(SuperUserOnlyMixin, SetPageTitleMixin, ListView):
    model = get_user_model()
    page_title = 'Admin panel'


class ShopUserCreate(SuperUserOnlyMixin, SetPageTitleMixin, CreateView):
    model = get_user_model()
    form_class = AdminShopUserCreateForm
    success_url = reverse_lazy('myadmin:index')
    page_title = 'Create user'


class ShopUserDelete(SuperUserOnlyMixin, SetPageTitleMixin, DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk' 
    page_title = 'Delete user'


class ShopUserUpdate(SuperUserOnlyMixin, SetPageTitleMixin, UpdateView):
    model = get_user_model()
    form_class = AdminShopUserCreateForm
    success_url = reverse_lazy('myadmin:index')
    pk_url_kwarg = 'user_pk'
    page_title = 'Update user'



@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    items = ProductCategory.objects.all()
    context = {
        'page_title': 'Categories',
        'object_list': items
    }
    return render(request, 'adminapp/categories.html', context=context)