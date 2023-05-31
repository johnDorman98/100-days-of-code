# Create a band name generator using input from the user
# The band name should be based on the users selected city and a pet/random name.

# Greeting message and inputs for the band name.
print('Welcome to the band name generator!')

city = input('Please select a city: ')
random_name = input('Please select a random name or even using a pets name: ')
band_name = f'Your bands name could be: {city} {random_name}'

print(band_name)