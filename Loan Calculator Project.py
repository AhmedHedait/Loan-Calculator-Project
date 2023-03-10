from math import log, ceil, floor
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="my credit calculator")

# Add the parameters positional/optional
parser.add_argument("--type", help="Annuity or differentiated")
parser.add_argument("--payment", help="Monthly payment", type=int)
parser.add_argument("--principal", help="Total amount loaned", type=int)
parser.add_argument("--periods", help="How many periods to return the loan", type=int)
parser.add_argument("--interest", help="Interest of the loan", type=float)

# Parse the arguments
args = parser.parse_args()

if args.type not in ("diff", "annuity"):
    print("Incorrect parameters")
elif args.type is None:
    print("Incorrect parameters")
elif (args.payment or args.principal or args.periods or args.interest) <= 0:
    print("Incorrect parameters")
if args.interest == None:
    print("Incorrect parameters")
else:
    if args.type == "diff":
        if args.principal is None or args.periods is None or args.interest is None:
            print("Incorrect parameters")
        else:
            diff_payment = []
            i = args.interest / 1200
            for m in range(1, args.periods + 1):
                d = ceil((args.principal / args.periods) + i * (args.principal - args.principal * (m - 1) / args.periods))
                diff_payment.append(d)
                print(f"Month {m}: paid out {d}")
            overpayment = int(sum(diff_payment) - args.principal)
            print()
            print(f"Overpayment = {overpayment}")
    elif args.type == "annuity":
        if (args.principal is None or args.periods is None or args.interest is None) and args.payment is None:
            print("Incorrect parameters")
        else:
            if args.principal is not None and args.periods is not None and args.interest is not None:
                i = args.interest / 1200
                cuota = ceil((args.principal * i) / (1 - ((1 + i) ** - args.periods)))
                overpayment = (cuota * args.periods) - args.principal
                print(f"Your annuity payment = {cuota}!")
                print(f"Overpayment = {overpayment}")
            elif args.principal is not None and args.interest is not None and args.payment is not None:
                i = args.interest / 1200
                calculation = log((args.payment / (args.payment - i * args.principal)), (1 + i))
                overpayment = int((ceil(calculation) * args.payment) - args.principal)

                if (calculation / 12).is_integer():
                    if calculation / 12 == 1:
                        print(f"It takes {int(calculation)} year to repay the credit")
                        print(f"Overpayment = {overpayment}")
                    else:
                        years = calculation / 12
                        print(f"It takes {years} years to repay the credit")
                        print(f"Overpayment = {overpayment}")
                else:
                    years = floor(calculation / 12)
                    months = (calculation / 12 % 1) * 12
                    if ceil(months) == 12:
                        years += 1
                        print(f"It takes {years} years to repay the credit")
                        print(f"Overpayment = {overpayment}")
                    else:
                        print(f"It takes {years} years and {ceil(months)} months to repay the credit")
                        print(f"Overpayment = {overpayment}")
            elif args.payment is not None and args.periods is not None and args.interest is not None:
                i = args.interest / 1200
                principal = round(args.payment * ((1 - ((1 + i) ** - args.periods)) / i))
                overpayment = (args.payment * args.periods) - principal
                print(f"Your credit principal = {principal}!")
                print(f"Overpayment = {overpayment}")