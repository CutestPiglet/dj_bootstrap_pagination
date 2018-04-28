from django.conf import settings
from django.core.paginator import Page, Paginator
from django.template.loader import render_to_string

DJ_BOOTSTRAP_PAGINATION_SETTINGS = getattr(settings, 'DJ_BOOTSTRAP_PAGINATION_SETTINGS', {})
PAGE_NUMBER_QUERY_STRING = DJ_BOOTSTRAP_PAGINATION_SETTINGS.get('PAGE_NUMBER_QUERY_STRING', 'page')


class BootstrapPaginator(Paginator):
    def __init__(self, object_list, items_per_page=20):
        super().__init__(object_list, items_per_page)

    def page(self, request):
        number = self.validate_number(request.GET.get(PAGE_NUMBER_QUERY_STRING, 1))
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        return BootstrapPage(self.object_list[bottom:top], number, self)


class BootstrapPage(Page):
    def __init__(self, object_list, number, paginator):
        super().__init__(object_list, number, paginator)
        self.page_number_query_string = PAGE_NUMBER_QUERY_STRING

    def render_pager(self):
        return render_to_string('dj_bootstrap_pagination/pager.html', {'pager': self})
