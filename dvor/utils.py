class MenuMixin:
    menu_slug = ()

    def set_menu_slug(self):
        return self.menu_slug

    def get_context_data(self, **kwargs):
        ctx = super(MenuMixin, self).get_context_data(**kwargs)
        ctx['menu_slug_list'] = self.set_menu_slug()
        return ctx
