#python czysc.py emails.txt przeczyszczone.txt
# "\n".join(emails)

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


with open("dane/"+ input_file) as in_file:
    data = in_file.read().splitlines()

cleaned_emails = set()
for email in data:
    if email.count("@") ==1:
        cleaned_emails.add(email.strip().lower())

cleaned_emails = list(cleaned_emails)
cleaned_emails.sort()

print(cleaned_emails)
with open("wyniki/"+output_file, "w") as f:
    for email in cleaned_emails:
        f.write(email)