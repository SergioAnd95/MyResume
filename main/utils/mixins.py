from django.http import HttpResponse, HttpResponseBadRequest


class AjaxFormMixin:
    def form_valid(self, form):
        return HttpResponse(self.success_url)

    def form_invalid(self, form):
        return HttpResponseBadRequest(form.errors.as_json())