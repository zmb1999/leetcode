def numUniqueEmails( emails):
    email_set = set()
    for email in emails:
        name, domain = email.split('@')
        name = name.split('+')[0].replace('.', '')
        email_set.add(name + '@'  + domain)
    return len(email_set)

print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))