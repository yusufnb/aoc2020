import re

with open('./day4-input.txt') as f:
    lines = f.read().splitlines()

def is_valid(passport):
    if (len(passport) == 8 or (len(passport) == 7 and "cid" not in passport) ):
        return True
    else:
        return False

def is_valid_format(str):
    fields = [s.split(":") for s in str.split(" ")]
    try:
        for rec in fields:
            if rec[0] == "byr" and ( int(rec[1]) < 1920 or int(rec[1]) > 2002 ):
                return False
            elif rec[0] == "iyr" and ( int(rec[1]) < 2010 or int(rec[1]) > 2020 ):
                return False
            elif rec[0] == "eyr" and ( int(rec[1]) < 2020 or int(rec[1]) > 2030 ):
                return False
            elif rec[0] == "hgt":
                matches = re.match("^([0-9]+)(cm|in)$", rec[1])
                if matches is None:
                    return False
                hgt = int(matches.group(1))
                unit = matches.group(2)
                if (unit == "cm" and (hgt < 150 or hgt > 193)):
                    return False
                if (unit == "in" and (hgt < 59 or hgt > 76)):
                    return False
            elif rec[0] == "hcl" and re.match("^#[0-9a-f]{6}$", rec[1]) is None:
                return False
            elif rec[0] == "ecl" and re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", rec[1]) is None:
                return False
            elif rec[0] == "pid" and re.match("^[0-9]{9}$", rec[1]) is None:
                return False

        return True

    except:
        return False

passport = []
valids = 0
for str in lines:
    if len(str) <= 1:
        if is_valid(passport):
            valids = valids + 1
        passport = []
    else:
        print(str)
        print(is_valid_format(str))
        if is_valid_format(str):
            passport = passport + [s.split(":")[0] for s in str.split(" ")]

if is_valid(passport):
    valids = valids + 1

print(valids)


