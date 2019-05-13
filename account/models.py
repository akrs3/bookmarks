from django.db import models

from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    first_name = models.CharField(_('first name'),
                                  max_length=50)
    last_name = models.CharField(_('last name'),
                                 max_length=50)
    email = models.EmailField(_('e-mail'))
    address = models.CharField(_('address'),
                               max_length=250)
    postal_code = models.CharField(_('postal code'),
                                   max_length=20)
    city = models.CharField(_('city'),
                            max_length=100)

    def __str__(self):
        return self.first_name
