hour_v = float(input("How much does cost your hour worked: "))
hour_w = int(input("How many hours you worked: "))

full_salary = hour_v * hour_w
inss = full_salary * 0.1
fgts = full_salary * 0.11

if full_salary <= 900:
    desc = 0
    ir = 0
elif 900 < full_salary <= 1500:
    desc = 5
    ir = full_salary * 0.05
elif 1500 < full_salary <= 2500:
    desc = 10
    ir = full_salary * 0.1
elif full_salary > 2500:
    desc = 20
    ir = full_salary * 0.2
else:
    print("Invalid Entry!")

deductions = ir + inss
net_salary = full_salary - deductions

print(f"\nFull salary: ({hour_v} x {hour_w})\t: ${full_salary}")
print(f"(-) IR ({desc}%)\t\t\t\t\t: ${ir}")
print(f"(-) INSS (10%)\t\t\t\t: ${inss}")
print(f"FGTS (11%)\t\t\t\t\t: ${fgts}")
print(f"Total deductions\t\t\t: ${deductions}")
print(f"Net salary\t\t\t\t\t: ${net_salary}")
