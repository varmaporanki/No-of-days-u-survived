import datetime
now=datetime.datetime.today()
year,month,day=map(int,input("enter birth year month and day:").split())
birth_day=datetime.datetime(year,month,day)
survived=now-birth_day
print(f"you survived survived :{survived.days} days")
