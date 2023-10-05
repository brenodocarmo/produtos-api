from django.contrib import admin

from .models import Group, SubGroup, Product


class GroupAdmin(admin.ModelAdmin):
    list_display = ('cod_gpr', 'desc_gpr', 'situ_gpr') # Mostra os campos
    list_filter = ('cod_gpr', 'desc_gpr')
    search_fields = ('cod_gpr', 'desc_gpr')
    list_per_page = 15
admin.site.register(Group, GroupAdmin)


class SubGroupAdmin(admin.ModelAdmin):
    list_display = ('cod_sbg', 'desc_sbg', 'situ_sgb') # Mostra os campos
    list_filter = ('cod_sbg', 'cod_sbg')
    search_fields = ('cod_sbg', 'desc_sbg')
    list_per_page = 15
admin.site.register(SubGroup, SubGroupAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('cod_psv', 'desc_psv', 'group_f', 'sub_group_f','situ_psv') # Mostra os campos
    list_filter = ('cod_psv', 'desc_psv')
    search_fields = ('cod_psv', 'desc_psv')
    list_per_page = 15
admin.site.register(Product, ProductAdmin)
