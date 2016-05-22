from cms.admin import pageadmin
from django.contrib import admin


class PageAdmin(pageadmin.PageAdmin):
    """
    Remove the meta description field from the page admin (we have this in django-cms-meta)
    """
    def get_form(self, request, obj=None, **kwargs):
        form_cls = self.get_form_class(request, obj)
        form = super(pageadmin.PageAdmin, self).get_form(request, obj, form=form_cls, **kwargs)
        try:
            del form.base_fields['meta_description']
        except KeyError:
            pass

        return form

admin.site.unregister(pageadmin.Page)
admin.site.register(pageadmin.Page, PageAdmin)
