from peewee import *
from Lessons.Chapter7.peewee_practice.Models import Supplier, Goods

def query_model():
	# 通过 get 方法
	# good = Goods.get(Goods.id==1)
	# 通过 get_by_id 方法
	# good = Goods.get_by_id(1)
	# 通过 [] 方法

	# good = Goods[1]
	# good = Goods.select() # 不会指定具体的字段
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1`
	# good = Goods.select(Goods.name, Goods.price)
	# SELECT `t1`.`name`, `t1`.`price` FROM `goods` AS `t1`

	# 进行条件查询
	# good = Goods.select().where(Goods.price>100)
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` WHERE (`t1`.`price` > 100)
	good = Goods.select().where((Goods.price>100) & (Goods.click_num>100))
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` WHERE ((`t1`.`price` > 100) AND (`t1`.`click_num` > 100))
	# good = Goods.select().where((Goods.price>100) | (Goods.click_num>100))
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` WHERE ((`t1`.`price` > 100) OR (`t1`.`click_num` > 100))
	# good = Goods.select().where(Goods.name.contains('飞天'))
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` WHERE (`t1`.`name` LIKE '%飞天%')

	# good = Goods.select().where(Goods.id << [1,3])
	good = Goods.select().where(Goods.id.in_([1, 3]))#等价于上面的语句
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` WHERE (`t1`.`id` IN (1, 3))
	# 1

	# good = Goods.select().where(Goods.price < Goods.click_num)
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` WHERE (`t1`.`price` < `t1`.`click_num`)

	# 排序
	good = Goods.select().order_by(Goods.price.desc())# 正序是 asc()
	# good = Goods.select().order_by(-Goods.price)# 正序是 +
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` ORDER BY `t1`.`price` DESC

	# 分页
	good = Goods.select().order_by(Goods.price).paginate(2,2)
	# SELECT `t1`.`id`, `t1`.`add_time`, `t1`.`name`, `t1`.`click_num`, `t1`.`good_num`, `t1`.`price`, `t1`.`brief` FROM `goods` AS `t1` ORDER BY `t1`.`price` LIMIT 2 OFFSET 2
	for g in good:
		print(g.id)
		print(g.name, g.price, g.click_num)




if __name__ == "__main__":
	query_model()
