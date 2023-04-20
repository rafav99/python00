cookbook = {
	"Sandwich" : {
    "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
	"meal" : "lunch",
    "prep_time" : 10
  },
	"Cake" : {
    "ingredients" : ["flour", "sugar", "eggs"],
	"meal" : "dessert",
    "prep_time" : 60
  },
	"Salad" : {
    "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
	"meal" : "lunch",
    "prep_time" : 15
  }
}

def	print_recipes():
	for key in cookbook:
		print(key)

def print_details(recipe):
	print("Ingredients:", ', '.join(cookbook[recipe]["ingredients"]))
	print("Meal:", cookbook[recipe]["meal"])
	print("Prep_time:", cookbook[recipe]["prep_time"])

def	del_recipe(recipe):
	del cookbook[recipe]

def add_recipe():
	name = input("Enter a name:\n")
	ingredients = []
	print("Enter ingredients:")
	while True:
		ing = input()
		if len(ing) == 0:
			break
		ingredients.append(ing)
	meal_type = input("Enter a meal type: \n")
	while True:
		prep_time = input("Enter preparation time: \n")
		try: 
			prep_time = int(prep_time)
			assert prep_time > 0
			break
		except:
			print("prep_time must be a non negative integer")
	cookbook[name] = {
		"ingredients" : ingredients,
		"meal" : meal_type,
    	"prep_time" : int(prep_time)
	}
	print(f"{name} has been added to the cookbook")

print('''Welcome to the Python Cookbook !
List of available option:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit''')
while True:
	try:
		option = int(input("Please select an option:\n"))
		if option == 1:
			add_recipe()
		elif option == 2:
			recipe = input("Please select a recipe to delete:\n")
			try:
				del_recipe(recipe)
				print(recipe, "deleted.")
			except:
				print("Selected recipe does not exist")
		elif option == 3:
			recipe = input("Please select a recipe to get its details:\n")
			if recipe in cookbook.keys():
				print("Recipe for {}:".format(recipe))
				print_details(recipe)
			else:
				print("Selected recipe does not exist")
		elif option == 4:
			print("List of cookbook recipes:")
			print_recipes()
		elif (option == 5):
			print("Cookbook closed. Goodbye!")
			break
		else:
			print("Please insert a valid option")
	except:
		print("Please insert a valid option")

