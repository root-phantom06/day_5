# Number 1
empty_list = []

# Number 2
web_tech = ["HTML", "CSS", "Javascript", "Python", "React"]

# Number 3
print(len(web_tech))

# Number 4
first_item = web_tech[0]
middle_item = web_tech[int((len(web_tech) / 2) - 1)]
last_item = web_tech[-1]

# Number 5
mixed_data_tyes = [
    {"name": "Mike"},
    {"age": "20"},
    {"height": 173},
    {"marital_status": "Lonely"},
    {"address": "Sogbossito"},
]

# Number 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Number 7
print(it_companies)

# Number 8
print(len(it_companies))

# Number 9
print(it_companies[0])
print(it_companies[int((len(it_companies) / 2) - 1)])
print(it_companies[-1])

# Number 10
it_companies[2] = "Tesla"
print(it_companies)

# Number 11
it_companies.append("NVDIA")

# Number 12
middle_item = int((len(it_companies) / 2) - 1)
it_companies[middle_item] = "Adobe"
print(it_companies)

# Number 13
for i, company in enumerate(it_companies):
    if company.upper() != "IBM":
        it_companies[i] = company.upper()
        break
print(it_companies)

# Number 14
it_companies = "#; ".join(it_companies)
print(it_companies)

# Number 15
it_companies = it_companies.split()
company_exists = "IBM" in it_companies

# Number 16
it_companies.sort()

# Number 17
it_companies.reverse()

#
