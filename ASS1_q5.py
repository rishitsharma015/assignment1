gross=float(input("Enter your gross income"))
dependents=float(input("Enter the number of dependents"))
Taxable_income=gross-10000-(dependents*3000)
Tax= Taxable_income*20/100
print("Your tax is",Tax)