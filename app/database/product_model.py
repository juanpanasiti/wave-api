from peewee import Model, CharField, DecimalField

from .wave_db import wave_db


class ProductModel(Model):
    name = CharField()
    image_url = CharField()
    description = CharField()
    price = DecimalField()

    class Meta:
        database = wave_db.db
        table_name = 'products'