from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Usuario, Producto, Pedido, ItemPedido, Pago, QRToken


class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email')


class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    model = Usuario

    fieldsets = UserAdmin.fieldsets + (
        ('Cafetería', {
            'fields': ('rol', 'saldo', 'id_empleado', 'tarjeta_numero', 'tarjeta_titular', 'tarjeta_expiry')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Cafetería', {
            'fields': ('rol', 'id_empleado')
        }),
    )

    list_display = ['username', 'email', 'first_name', 'last_name', 'rol', 'is_staff']
    list_filter  = ['rol', 'is_staff', 'is_active']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Pago)
admin.site.register(QRToken)
