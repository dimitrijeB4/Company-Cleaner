import csv

suffixes = [
    "incorporated",
    "inc.",
    "inc",
    "corporation",
    "corp.",
    "corp",
    "company",
    "co.",
    "co",
    "pllc",
    "l.l.c.",
    "l.l.c",
    "llp",
    "l.p.",
    "lp",
    "limited",
    "ltd.",
    "ltd",
    "plc",
    "p.c.",
    "pc",
    "p.c",
    "cpa",
    "group",
    "enterprises",
    "enterprise",
    "solutions",
    "systems",
    "technologies",
    "technology",
    "tech",
    "services",
    "service",
    "partners",
    "partner",
    "ventures",
    "international",
    "l.p",
    "llc"
]
noises = ["®", "™", "℠"]
useless_info_list = [" inc. "," by "," an "," a "," powered "]
def camelCase(string):
    if len(string) <6 and len(string.split()) == 1:
        return string
    else:
        lower_string=string.lower()
        names_list = lower_string.split()
        new_name_list=[]
        for name in names_list:
            new_name= name[0].upper() + name[1:]
            new_name_list.append(new_name)
        new_name=" ".join(new_name_list)
        return new_name


def normalize(text):
    return text.lower().replace(" ", "")

def remove_suffix(company_string):
    new_company_name = company_string.strip()
    if len(new_company_name.split()) ==1:
        return new_company_name
    for suffix in suffixes:
        suffix = suffix.lower()
        
        while new_company_name.lower().endswith(suffix):
            new_company_name = new_company_name[:-(len(suffix))].rstrip()

    return new_company_name.rstrip(" ,.-")

    #AO Wealth Advisory -> AO 
def remove_useless_info(company_name):
    new_company_name= company_name.strip()
    small_index=len(new_company_name)
    for info in useless_info_list:
        index = new_company_name.lower().find(info)
        if index != -1 and index < small_index:
                small_index = index
                
    if new_company_name.split(" ")[0] == new_company_name.split(" ")[0].upper() and len(new_company_name.split(" ")[0])<5 :
        small_index = len(new_company_name.split(" ")[0])

    return new_company_name[:small_index].strip()

def remove_noise(company_string):
    new_company_name=company_string.strip()
    for noise in noises:
        new_company_name=new_company_name.replace(noise,"")
    return new_company_name

def process_row(row):
    if len(row) <= 7:
        return row
    domain = row[4].split("@")[-1].lower().split(".")[0]

    company = row[3]
    
    
    cleaned = camelCase(remove_suffix(remove_noise(remove_useless_info(company))).strip())

    if len(cleaned.split()) == 1:
        row[3] = cleaned
        return row

    if normalize(cleaned) in domain or domain in normalize(cleaned):
        if len(normalize(cleaned)) < len(domain):
            row[3] = cleaned.split(" ")[0]
            return row
        row[3] = "@@@ " + cleaned
        return row

    # Otherwise flag

    row[3] = "!!! " + cleaned
    return row

def main():
    print("helloooo")

    try:
        with open("csv/To_Clean.csv") as file, open("csv/Cleaned.csv", "w", newline="") as outfile:
            reader = csv.reader(file)
            writer = csv.writer(outfile)

            for row in reader:
                new_row = process_row(row)
                writer.writerow(new_row)
    except FileNotFoundError:
    # Code to handle the specific error
        print("Please add the To_Clean.csv file in /csv ")

    
    
main()