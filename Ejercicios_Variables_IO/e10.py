# Starting Out with Python, Third Edition
# Capítulo 2, Ejercicio 10

"""
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, and then displays the number of
cups of each ingredient needed for the specified number of cookies.
"""

def ingredient_adjuster():
    cookies = 48
    sugar = 1.5
    butter = 1 
    flour = 2.75
    sugar_per_cookie = sugar / cookies
    butter_per_cookie = butter / cookies
    flour_per_cookie = flour / cookies

    requested_cookies = int(input("Enter the amount of cookies: "))
    sugar_total  = sugar_per_cookie * requested_cookies
    butter_total = butter_per_cookie * requested_cookies
    flour_total = flour_per_cookie * requested_cookies
    print(f"Sugar needed {sugar_total:,.2f} cups")
    print(f"Butter needed: {butter_total:,.2f} cups")
    print(f"Flour needed {flour_total:,.2f} cups")



def main():
    ingredient_adjuster()
    pass

if __name__ == "__main__":
    main()
