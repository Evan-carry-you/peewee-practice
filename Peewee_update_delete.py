from peewee import *
from Lessons.Chapter7.peewee_practice.Models import Supplier, Goods

def update_model():
	# 简单 update
	# good = Goods.get(Goods.id==1)
	# good.click_num += 1
	# good.save()
	# 等价于 UPDATE `goods` SET `add_time` = '2019-10-09', `name` = '52度茅台集团国隆双喜酒500mlx6', `click_num` = 101, `good_num` = 0, `price` = 128, `brief` = '贵州茅台酒厂（集团）保健酒业有限公司生产，是以“龙”字打头的酒水。中国龙文化上下8000年，源远而流长，龙的形象是一种符号、一种意绪、一种血肉相联的情感。' WHERE (`goods`.`id` = 1)

	# Goods.update(click_num=101).where(Goods.id==1).execute()
	# 等价于 UPDATE `goods` SET `click_num` = 101 WHERE (`goods`.`id` = 1)
	Goods.update(click_num=Goods.click_num+1).where(Goods.id==1).execute() # update 里面必须加上 Goods
	# 等价于 UPDATE `goods` SET `click_num` = (`goods`.`click_num` + 1) WHERE (`goods`.`id` = 1)

	# 删除
	# good = Goods.get(Goods.id ==1) # get 不到的时候会报错，实际使用的时候应该进行 catch
	# good.delete_instance()
	# 等价于：DELETE FROM `goods` WHERE (`goods`.`id` = 1)
	Goods.delete().where(Goods.price<100).execute()
	# 等价于： DELETE FROM `goods` WHERE (`goods`.`price` < 100)

if __name__ == "__main__":
	update_model()
