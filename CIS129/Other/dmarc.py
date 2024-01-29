
emails=['admin1@absenceplus.com','admin1@btsdetroit.org','admin1@compone.net','admin1@echelon-properties.com','admin1@fdigroup.com','admin1@financial-designs.com','admin1@georgebford.com','admin1@haaweb.net','admin1@hcami.com','admin1@hcaweb.net','admin1@mai-ime.com','admin1@manageability.com','admin1@manageabilityime.com','admin1@medicarecs.com','admin1@medicarecs.com','admin1@medicarecs.net','admin1@rizikon.net','admin1@startechsoftware.com']
for email in emails:
    print(f"v=DMARC1; p=quarantine; rua=mailto:{email}; ruf=mailto:{email}; pct=100;")