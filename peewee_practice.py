from peewee import *
from peewee import Model
from datetime import datetime

db = MySQLDatabase("message", host="127.0.0.1", port=3306, user='root', password='')


class BaseModel(Model):
	add_time = DateField(datetime.now, verbose_name="添加时间")

	class Meta:
		database = db

class Suplier(BaseModel):
	name = CharField(max_length=100, verbose_name="商家名称", index=True)
	address = CharField(max_length=200, verbose_name="商家地址")
	phone = CharField(max_length=11, verbose_name="商家手机")
	class Meta:
		table_name = "suplier"


class Goods(BaseModel):
	ForeignKeyField(Suplier, verbose_name="商家", backref="goods" )
	name = CharField(max_length=100, verbose_name="商品名称", index=True)
	click_num = IntegerField(default=0, verbose_name="点击量")
	good_num = IntegerField(default=0, verbose_name="库存")
	price = FloatField(default=0.0, verbose_name="价格")
	brief = TextField(verbose_name="商品简介")

	class Meta:
		table_name = "goods"


def init_tables():
	db.create_tables([Goods, Suplier])


if __name__ == "__main__":
	init_tables()
