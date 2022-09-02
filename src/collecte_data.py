from typing import Iterator, Dict
import datetime as _dt
import scrapper as _scrapper

def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)


def create_events_dict() -> Dict:
    DivList = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for date in _date_range(start_date, end_date):
        #print(date)
        month = date.Strftime("%8").lower()
        if month not in DivList:
            DivList[month] = dict()
        
        DivList[month][date.day] = _scrapper.affichage(month)

#create_events_dict()