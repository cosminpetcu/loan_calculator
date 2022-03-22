import math
import argparse
parser = argparse.ArgumentParser()
# write your code here
parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

if (args.type != "annuity" and args.type != "diff") or (args.type == "diff" and args.payment != 0) or not args.interest or len(vars(args)) < 4:
    print("Incorrect parameters")

if args.interest is not None:
    if args.type == 'annuity':
        if args.periods is None:
            nominal_interest = (args.interest / 100) / 12
            num_months = math.ceil(math.log(args.payment / (args.payment - nominal_interest * args.principal), 1 + nominal_interest))
            years = math.floor(num_months / 12)
            months = num_months - (years * 12)
            if years != 0 and months != 0:
                print(years, 'years and', months, 'months')
            elif months == 0:
                print(years, 'years')
            elif years == 0:
                print(months, 'months')
            overpayment = num_months * args.payment - args.principal
            print('Overpayment =', overpayment)
        elif args.payment is None:
            nominal_interest = (args.interest / 100) / 12
            annuity_payment = math.ceil(args.principal * ((nominal_interest * math.pow((1 + nominal_interest), args.periods)) / (math.pow((1 + nominal_interest), args.periods) - 1)))
            print('Your annuity payment =', annuity_payment, '!')
            overpayment = args.periods * annuity_payment - args.principal
            print('Overpayment =', overpayment)
        elif args.principal is None:
            nominal_interest = (args.interest / 100) / 12
            loan_principal = args.payment / ((nominal_interest * math.pow((1 + nominal_interest), args.periods)) / (math.pow((1 + nominal_interest), args.periods) - 1))
            print('Your loan principal =', loan_principal, '!')
            overpayment = args.periods * args.payment - loan_principal
            print('Overpayment =', overpayment)
    elif args.type == 'diff':
        nominal_interest = (args.interest / 100) / 12
        sums = 0
        for i in range(1, args.periods + 1):
            diff_payment = math.ceil(args.principal / args.periods + nominal_interest * (args.principal - (args.principal * (i - 1)) / args.periods))
            sums = sums + diff_payment
            print('Month', i, ': payment is', diff_payment)
        overpayment = sums - args.principal
        print('Overpayment =', overpayment)
