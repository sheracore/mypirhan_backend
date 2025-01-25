from django.apps import AppConfig


class BillingConfig(AppConfig):
    name = 'billing'
    app_label = "billing"
    verbose_name = _("Billing")
    verbose_name_plural = _("Billings")
