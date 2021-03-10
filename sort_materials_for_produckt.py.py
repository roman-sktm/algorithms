
def series_sort(DATA:list):
	""" Return dictionary. 
	Keys - names of products.
	Values - lists.
	Number of list (value) element is number of series (zero series skipped)
	Content of list (value) - string with names of materials.
	"""
	products_series_materials = {}
	# Filling the dictionary with keys (products):
	products_and_series = series_of_products(DATA)
	for product, series in products_and_series.items():
		products_series_materials[product] = [0]*(series[1]+1)
	# Filling the dictionary with values (materials).
	# Number of element is number of series with this materials.
	for i in DATA:
		series = products_series_materials[i[1]]
		if i[3] != 0:
			for k in range (i[2], i[3]+1, 1):
				if series[k] == 0:
					series[k] = i[0]
				else:
					series[k] = series[k] + ", " + i[0]
		else:
			for k in range (len(series)):
				if series[k] == 0:
					series[k] = i[0]
				else:
					series[k] = series[k] + ", " + i[0]
	printing_products_unique_materials(products_series_materials)

def series_of_products(DATA:list):
	""" Return dictionary. 
	Keys - names of products.
	Values - list. Element 0 - first series of the product.
	Element 1 - last series of the product.
	"""
	dict_of_products = {}
	for i in DATA:
		# Filling the dictionary with keys (products):
		if i[1] not in dict_of_products.keys():
			dict_of_products[i[1]] = [i[2], i[3]]
		else:
			series = dict_of_products[i[1]]
			if i[2] < series[0]:
				series[0] = i[2]
			if i[3] > series[1]:
				series[1] = i[3]
	return dict_of_products


def printing_products_unique_materials(database:dict):
	""" Print numbers of series with unique set of materials
	for every produckt
	"""
	for product, series in database.items():
		i = 1
		k = 1
		while k < len(series)-1:
			k += 1
			if series[i] != series[k]:
				if i == k-1:
					print ((f"Изделие: {product}, номер серии: {i}, материалы: {series[i]}"))
					i = k
				else:
					print ((f"Изделие: {product}, номера серий: {i}-{k-1}, материалы: {series[i]}"))
					i = k
			if k == len(series)-1:
				print ((f"Изделие: {product}, номера серий: {i}-{k}, материалы: {series[i]}"))
	return

def printing_products_all_materials(database:dict):
	""" Print numbers of all series with set of materials
	for every produckt
	"""
	for product, series in database.items():
		for i in range(1, len(series)):
			print (f"Изделие: {product}, серия: {i}, материалы: {series[i]}")
	return


# Data input - list of tuples
DATA = [
	("пенопласт", "стена", 1, 10),
	("шурупы", "крыша", 0, 0),
	("пеноплекс", "стена", 8, 12),
	("пенопласт", "стена", 16, 25),
	("пленка", "крыша", 11, 18),
	("кирпич", "стена", 1, 20),
	("пеноблок", "стена", 21, 28),
	("пенопласт", "крыша", 3, 10),
	("краска", "крыша", 5, 0),
	("цемент", "стена", 3, 0),
	("профлист", "крыша", 2, 20),
	("краска", "стена", 0, 0),
]

series_sort(DATA)




