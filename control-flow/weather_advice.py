# Ask the user to input the current weather from a predefined set of conditions
current_weather = input("What's the weather like today? (sunny/rainy/cold): ")
# print(current_weather)

# If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
if current_weather == 'sunny':
    print("Wear a t-shirt and sunglasses.")

# If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.    
elif current_weather == 'rainy':
    print("Don't forget your umbrella and a raincoat.")

# If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
elif current_weather == 'cold':
    print("Make sure to wear a warm coat and a scarf.")

# else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.
else: print("Sorry, I don't have recommendations for this weather.")