from rocketry import Rocketry
from rocketry.conds import every
from rocketry.conds import cron

app = Rocketry(config={"task_execution": "async"})

@app.task(every('10 seconds'))
async def do_every_10sec():
    print('10 sec')

@app.task("daily between 08:00 and 09:00")
def do_daily():
    print('daily between 08:00 and 09:00')

@app.task("weekly on Monday")
def do_weekly():
    print('weekly on Mondays')

@app.task(cron('0 2 * * *'))
def do_every_2am():
    print('everyday at 2 am')

if __name__ == "__main__":
    # Run only Rocketry
    app.run()