# The goal of this calculator should be to find out how much Chris has to pay given a certain amount of time for his car
# This calculator will take into account the APR % listed on the Subaru website, plus any possible plans

print("\n")
print("Hello Christopher. "
      "This is a program designed to "
      "calculate the cost of paying off a car "
      "given a certain input of years.\n")

numYears = int(input('To begin with, how many years do you plan on taking to pay off this car? (max: 6 years) \n'))
numMonths = numYears * 12
downPayment = int(input("How much are you willing to put down in down payment? \n"))
whatCar = str(input("What car are you looking to buy in the Wilderness trim? \n"
                    "Please choose from the following: \n"
                    "A. Outback \n"
                    "B. Forester \n"
                    "C. Crosstrek \n"))

# Below is a list of prices about the cars he would potentially buy as well as APR and calculations
# For the monthly fee

outbackPrice = 39960
foresterPrice = 34920
crosstrekPrice = 32195

outbackCost = round((outbackPrice - downPayment), 2)
foresterCost = round((foresterPrice - downPayment), 2)
crosstrekCost = round((crosstrekPrice - downPayment), 2)

outbackAPR = round((outbackCost * (.029 / 365) * 30), 2)
foresterAPR = round((foresterCost * (.029 / 365) * 30), 2)
crosstrekAPR = round((crosstrekCost * (.039 / 365) * 30), 2)

monthlyFeeOutB = round((((outbackCost / 1000) * 15.15) / numMonths), 2)
monthlyFeeForest = round((((foresterCost / 1000) * 15.15) / numMonths), 2)
monthlyFeeCross = round((((crosstrekCost / 1000) * 15.15) / numMonths), 2)

while True:
    if whatCar in ["A", "a"]:
        print("Outback! Ok, cool. Let me fetch you some data about that!\n")
        print(
            f'So currently the starting price of the 2024 Outback Wilderness is ${outbackPrice} and the dealer is '
            f'offering\n'
            f'2.9% financing for 72 months.\n')
        print("So knowing this, let's calculate! \n")
        print(f"Based on your down payment of ${downPayment}, the new total cost would be ${outbackCost}.\n")

        outbackCost = round((outbackCost / numMonths), 2)
        totalOB = round((outbackCost + outbackAPR + monthlyFeeOutB), 2)

        print(f"Assuming you're gonna loan the rest, there is an extra monthly charge per every $1000\n"
              f"you loan out for this car.\n"
              "\n"
              f"That would make your monthly payment look like something below: \n"
              f"     MONTHLY COST AFTER DOWNPAYMENT: ${outbackCost}\n"
              f"     MONTHLY APR: {outbackAPR} \n"
              f"+    EXTRA LOAN FEE: ${monthlyFeeOutB}\n"
              f"________________________________________________________\n"
              f"    TOTAL MONTHLY COST: {totalOB}")
        break

    elif whatCar in ["B", "b"]:
        print("So you're going with the Forester? Nice. Let's give you some info about that.\n")
        print(
            f"Alright. The 2024 Forester Wilderness's starting price is ${foresterPrice} and the dealer is offering \n"
            f"2.9% financing for 72 months.\n")
        print("So knowing this, let's calculate! \n")
        print(f" Based on your down payment of ${downPayment}, the new total cost would be ${foresterCost}.\n")

        foresterCost = round((foresterCost / numMonths), 2)
        totalForest = round((foresterCost + foresterAPR + monthlyFeeForest), 2)

        print(f"Assuming you're gonna loan the rest, there is an extra monthly charge per every $1000\n"
              f"you loan out for this car.\n"
              "\n"
              f"That would make your monthly payment look like something below: \n"

              f"     MONTHLY COST AFTER DOWNPAYMENT: ${foresterCost}\n"
              f"     MONTHLY APR: {foresterAPR}\n"
              f"+    EXTRA LOAN FEE: ${monthlyFeeForest}\n"
              f"________________________________________________________\n"
              f"    TOTAL MONTHLY COST: {totalForest}")
        break

    elif whatCar in ["C", "c"]:
        print("Crosstrek! Great. Let's get you some info about that.\n")
        print(f"The Crosstrek Wilderness's starting price is ${crosstrekPrice} and \n"
              f"the dealer is offering 3.9% financing for 72 months.")
        print("So knowing this, let's calculate! \n")
        print(f" Based on your down payment of ${downPayment}, the new total cost would be ${crosstrekCost}.\n")

        crosstrekCost = round((crosstrekCost / numMonths), 2)
        totalCross = round((crosstrekCost + crosstrekAPR + monthlyFeeCross), 2)

        print(f"Assuming you're gonna loan the rest, there is an extra monthly charge per every $1000\n"
              f"you loan out for this car.\n"
              "\n"
              f"That would make your monthly payment look like something below: \n"

              f"     MONTHLY COST AFTER DOWNPAYMENT: ${crosstrekCost}\n"
              f"     MONTHLY APR: {crosstrekAPR}\n"
              f"+    EXTRA LOAN FEE: ${monthlyFeeCross}\n"
              f"________________________________________________________\n"
              f"    TOTAL MONTHLY COST: {totalCross}")
        break

    else:
        print("Ehhh that's not an option. Try again please.\n")
        whatCar = str(input("What car are you looking to buy in the Wilderness trim? \n"
                            "Please choose from the following: \n"
                            "A. Outback \n"
                            "B. Forester \n"
                            "C. Crosstrek \n"))
