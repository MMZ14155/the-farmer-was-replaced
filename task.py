import plant
import explore	
	
def collect_items():
	clear()

	if num_items(Items.Power) < 2 * 10 ** 3:
		while(num_items(Items.Power) < 5 * 10 ** 3):
			plant.sunflower(8, 8, 8)
	
	items = [num_items(Items.Hay), num_items(Items.Wood), num_items(Items.Carrot), num_items(Items.Pumpkin), num_items(Items.Cactus), num_items(Items.Bone), num_items(Items.Gold)]
	minor = items[0]
	for i in range(1, 7):
		if minor > items[i]:
			minor = items[i]
			index = i
	
	if index == 0 or index == 2:
		plant.default(0, 0, get_world_size())
		clear()
	elif index == 1:
		plant.tree(0, 0, get_world_size())
	elif index == 3:
		plant.pumpkin(0, 0, get_world_size())
	elif index == 4:
		plant.cactus(0, 0, get_world_size())
	elif index == 5:
		explore.snake()
	else:
		weird_substance = explore.maze(0, 0, get_world_size())
		if weird_substance != 0:
			while(num_items(Items.Weird_Substance) < weird_substance):
				plant.weird_substance(0, 0)
			explore.maze(0, 0, get_world_size())