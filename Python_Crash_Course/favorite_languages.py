favorite_languages = {
    'jen': 'python',
    'laurens': 'python',
    'tim': 'javascript',
    'paul': 'java',
    'max': 'ruby',
}

language = favorite_languages['laurens'].title()
print(f"Laurens favorite language is {language}.\n")


for name in favorite_languages.keys():
    print(name.title())

print("\n")

for name in favorite_languages:
    print(name.upper())

if 'erin' not in favorite_languages.keys():
    print("Erin, please take the poll!")

friends = ['jen', 'laurens']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
print("\nSorted list")
for name in sorted(favorite_languages.keys()):
    print(f"{name}")

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Using set to show only the unique values
print("\nOnly showing the unique languages:")
for language in set(favorite_languages.values()):
    print(language.title())