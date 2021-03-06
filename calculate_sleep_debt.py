import fitbit
import secret
from datetime import date, timedelta

def prettyPrintTime(minutes):
	hours = minutes / 60
	minutes = minutes % 60
	return "%d:%02d" % (hours, minutes)

DAY_RANGE = 7
client = fitbit.Fitbit(secret.FITBIT_CONSUMER_KEY, secret.FITBIT_CONSUMER_SECRET, resource_owner_key=secret.FITBIT_USER_KEY, resource_owner_secret=secret.FITBIT_USER_SECRET)
data = client.time_series('sleep/minutesAsleep', period=str(DAY_RANGE) + 'd')

totalTimeSlept = 0
for currentDate in data['sleep-minutesAsleep']:
	totalTimeSlept += int(currentDate['value'])
	print unicode(currentDate['dateTime']) + ': ' + prettyPrintTime(int(currentDate['value']))
print 'Total time slept: ' + prettyPrintTime(totalTimeSlept)

dailyGoal = raw_input('How much do you want to sleep on average every night (in hours)? ')
if dailyGoal:
	totalGoalTime = int(dailyGoal)*60*DAY_RANGE
	print 'Total goal time: ' + prettyPrintTime(totalGoalTime)
	print 'Difference between goal and real: ' + prettyPrintTime(totalTimeSlept-totalGoalTime)