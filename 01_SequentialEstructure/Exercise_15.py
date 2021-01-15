gain_hour = float(input("How much you earn for hour: "))
hour_month = int(input("How much you worked in this month: "))

full_wage = gain_hour * hour_month
print("="*40)
print(f"Your full wage in this month was ${round(full_wage, 2)} dollars.")

impost_1 = (full_wage * 8) / 100
impost_2 = (full_wage * 11) / 100
print("-"*40)
print(f"You payed ${round(impost_1, 2)} to the social security.")

union = (full_wage * 5) / 100
print("-"*40)
print(f"You payed ${round(union, 2)} to the syndicate.")

des_wage = full_wage - impost_1 - impost_2 - union
print("-"*40)
print(f"In the end you received ${round(des_wage, 2)} in this month.")

des = impost_1 + impost_2 + union
print("-"*40)
print(f"You payed ${round(des, 2)} in imposts.")
print("-"*40)