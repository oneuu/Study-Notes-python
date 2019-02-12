#coding:utf-8

from nose.tools import *

from ex47.game import Room

def test_room():
	#实例化对象
	gold = Room("GoldRoom",
		"""This Room has gold in it you can grab.There is a door to the north.""")
	#验证变量是否正确
	assert_equal(gold.name,"GoldRoom")
	assert_equal(gold.paths,{})

def test_room_paths():
	#实例化对象
	center = Room("Center", "Test room in the center.") 
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	#调用其中一个方法
	center.add_paths({'north': north, 'south': south}) 
	#验证方法是否执行
	assert_equal(center.go('north'), north) 
	assert_equal(center.go('south'), south)
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	start.add_paths({'west': west, 'down': down}) 
	west.add_paths({'east': start}) 
	down.add_paths({'up': start})
	assert_equal(start.go('west'), west) 
	assert_equal(start.go('west').go('east'), start) 
	assert_equal(start.go('down').go('up'), start)



