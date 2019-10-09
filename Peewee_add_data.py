from Lessons.Chapter7.peewee_practice.Models import Supplier, Goods
from Lessons.Chapter7.peewee_practice.datas import supplier_list, goods_list


def input_supplier_datas():
	for supplier in supplier_list:
		sup = Supplier()
		sup.name = supplier['name']
		sup.address = supplier['address']
		sup.phone = supplier['phone']
		sup.save()


def input_goods_datas():
	for good in goods_list:
		g = Goods(**good)
		g.save()
		print(g.id)


def init_data():
	input_goods_datas()



if __name__ == "__main__":
	init_data()
