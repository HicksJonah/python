alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
if name in friends:
    print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)