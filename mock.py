import string, random, names, datetime
from faker import Faker
fake = Faker()
Faker.seed(0)

separators = ["_", ""]
special = [";", ";", "&"]
domains = ["gmail", "protonmail", "yahoo"]
occupations = ["Footballer", "Actor", "Singer", "Astronaut"]
passport_range = {'start': datetime.date(2025,1,1), 'end': datetime.date(2030,12,31)}
birth_range = {'start': datetime.date(1980,1,1), 'end': datetime.date(2000,12,31)}

def mock_dict():

	temp_name = name()
	temp_username = username(temp_name)

	return {
		"name": temp_name,
		"username": temp_username,
		"email": email(temp_username),
		"password": password(),
		"job": job(),
		"date_of_birth": date_of_birth().strftime("%d-%b-%Y"),
		"passport_num": passport_num(),
		"passport_exp": passport_exp().strftime("%d-%b-%Y"),
	}

def name():
	return str(names.get_full_name())

def username(name):
	return name.lower().replace(" ", random.choice(separators)) + str(random.randint(1,1000))

def email(username):
	return username + "@" + random.choice(domains) + ".com"

def password():
	return ('').join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=15)) + random.choice(special)

def job():
	return random.choice(occupations)

def date_of_birth():
	return fake.date_between_dates(birth_range['start'], birth_range['end'])

def passport_num():
	return str(fake.passport_number())

def passport_exp():
	return fake.date_between_dates(passport_range['start'], passport_range['end'])