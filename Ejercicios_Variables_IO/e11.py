# Starting Out with Python, Third Edition
# Capítulo 2, Ejercicio 11
"""
Write a program that asks the user for the number of males and the number of females registered
in a class. The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
class. The percentage of males can be calculated as 8 4 20 5 0.4, or 40%. The percentage
of females can be calculated as 12 4 20 5 0.6, or 60%.
"""

def male_female_percentages():
    males = int(input("Enter the number of males: "))
    females = int(input("Enter the number of females: "))
    total_alumni = males + females
    perc_males = (males / total_alumni) * 100
    perc_females = (females / total_alumni) * 100

    print(f"Males percentage: {perc_males:,.0f}%")
    print(f"Females percentages: {perc_females:,.0f}%")

def main():
    male_female_percentages()
    pass

if __name__ == "__main__":
    main()
