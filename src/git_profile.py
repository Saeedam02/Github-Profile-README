from pathlib import Path

def generate_profile(theme,**kwargs):

    '''Generate profile readme from theme and kwargs'''
    # read theme
    with open(f"src/themes/{theme}/profile.txt") as f:
        profile=f.read()

    # Replace placeholders with user input
    for item, value in kwargs.items():
        item_path=Path(f"src/themes/{theme}/{item}.txt")
        with open(item_path) as f:
                profile_item=f.read()

        profile_item=profile_item.replace("{ value  }",value)
        profile=profile.replace(f"{{ {item} }}",profile_item)

    return profile

if __name__ =='__main__':
     #personal info
     name="John Doe"
     email="johndoe@gmail.com"
     phone="1 123 456 7890"
     homepage="https://johndoe.com"
     location="New York,USA"

     # Social Media
     github="johndoe"
     linkdin="johndoe"
     twitter="johndoe"
     facebook="johndoe"
     instagram="johndoe"
     youtube="johndoe"
     medium="johndoe"

    #select theme
     theme="default"

     #Generate github readme
     profile = generate_profile(theme, name=name, email=email,linkdin=linkdin)
     print(profile)