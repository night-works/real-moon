from fastapi import FastAPI
from datetime import datetime, timedelta
import ephem

app = FastAPI()


@app.get("/phase")
async def moon_phase():
    now = datetime.utcnow()
    observer = ephem.Observer()
    name, key = human_moon(observer)

    return {
            "phase" : {
                "name" : name,
                "key" : key
            },
            "date": now.date()}



def human_moon(observer):
    target_date_utc = observer.date
    target_date_local = ephem.localtime( target_date_utc ).date()
    next_full = ephem.localtime( ephem.next_full_moon(target_date_utc) ).date()
    next_new = ephem.localtime( ephem.next_new_moon(target_date_utc) ).date()
    next_last_quarter = ephem.localtime( ephem.next_last_quarter_moon(target_date_utc) ).date()
    next_first_quarter = ephem.localtime( ephem.next_first_quarter_moon(target_date_utc) ).date()
    previous_full = ephem.localtime( ephem.previous_full_moon(target_date_utc) ).date()
    previous_new = ephem.localtime( ephem.previous_new_moon(target_date_utc) ).date()
    previous_last_quarter = ephem.localtime( ephem.previous_last_quarter_moon(target_date_utc) ).date()
    previous_first_quarter = ephem.localtime( ephem.previous_first_quarter_moon(target_date_utc) ).date()
    
    if target_date_local in (next_full, previous_full):
        return 'Full',4
    elif target_date_local in (next_new, previous_new):
        return 'New',0
    elif target_date_local in (next_first_quarter, previous_first_quarter):
        return 'First Quarter',2
    elif target_date_local in (next_last_quarter, previous_last_quarter):
        return 'Last Full Quarter',6
    elif previous_new < next_first_quarter < next_full < next_last_quarter < next_new:
        return 'Waxing Crescent',1
    elif previous_first_quarter < next_full < next_last_quarter < next_new < next_first_quarter:
        return 'Waxing Gibbous',3
    elif previous_full < next_last_quarter < next_new < next_first_quarter < next_full:
        return 'Waning Gibbous',5
    elif previous_last_quarter < next_new < next_first_quarter < next_full < next_last_quarter:
        return 'Waning Crescent',7

