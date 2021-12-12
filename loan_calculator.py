import argparse
import math

types = ["annuity", "diff"]
argument_list = []
counter = 0

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

# store arguments in array
argument_list.append(args.type)
argument_list.append(args.payment)
argument_list.append(args.principal)
argument_list.append(args.periods)
argument_list.append(args.interest)

for element in argument_list:
    if element:
        counter += 1

if counter < 4:
    print("Incorrect parameters")
    exit()
elif argument_list[0] not in types:
    print("Incorrect parameters")
    exit()
elif argument_list[0] == "diff" and argument_list[1]:
    print("Incorrect parameters")
    exit()
elif not argument_list[4]:
    print("Incorrect parameters")
    exit()

for element in argument_list:
    if type(element) == float and element < 0:
        print("Incorrect parameters")
        exit()


def diff(p, n, i):
    i /= (12 * 100)
    m = 0
    sum_ = 0
    while m < n:
        m += 1
        d = p / n + i * (p - (p * (m - 1) / n))
        print(f"Month {m}: payment is {math.ceil(d)}")
        sum_ += math.ceil(d)

    over_payment = round(sum_ - p)
    print(f"\nOverpayment = {over_payment}")


def annuity_a(lp, n, i):
    i /= (12 * 100)
    a = math.ceil(lp * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)))
    over_payment = round(a * n - lp)
    print(f"Your annuity payment = {a}!")
    print(f"Overpayment = {over_payment}")


def annuity_n(lp, p, i):
    i /= (12 * 100)
    x = p / (p - i * lp)
    base = 1 + i
    n = math.ceil(math.log(x, base))

    years = n // 12
    months = n % 12

    period = n

    over_payment = round(p * period - lp)

    if years == 0:
        print("It will take " + str(months) + " months to repay this loan!")
        print(f"Overpayment = {over_payment}")
    elif months == 0:
        print("It will take " + str(years) + " years to repay this loan!")
        print(f"Overpayment = {over_payment}")
    else:
        print("It will take " + str(years) + " years and " + str(months) + " months to repay this loan!")
        print(f"Overpayment = {over_payment}")


def annuity_p(p, pe, i):
    i /= (12 * 100)
    lp = math.floor(p / ((i * math.pow((1 + i), pe)) / (math.pow((1 + i), pe) - 1)))

    over_payment = round(p * pe - lp)

    print("Your loan principal = " + str(lp) + "!")
    print(f"Overpayment = {over_payment}")


if args.type == "diff":
    diff(float(args.principal), float(args.periods), float(args.interest))
elif args.type == "annuity":
    if not args.payment:
        annuity_a(float(args.principal), float(args.periods), float(args.interest))
    elif args.principal:
        annuity_n(float(args.principal), float(args.payment), float(args.interest))
    elif args.periods:
        annuity_p(float(args.payment), float(args.periods), float(args.interest))
