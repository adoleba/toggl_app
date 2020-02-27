from datetime import timedelta


def dates_for_first_week_days_in_month(valid_data):
    week_days = {}

    week_days['first_monday'] = valid_data['date_start'] + timedelta(days=0 - valid_data['date_start'].weekday())
    week_days['first_tuesday'] = valid_data['date_start'] + timedelta(days=1 - valid_data['date_start'].weekday())
    week_days['first_wednesday'] = valid_data['date_start'] + timedelta(days=2 - valid_data['date_start'].weekday())
    week_days['first_thursday'] = valid_data['date_start'] + timedelta(days=3 - valid_data['date_start'].weekday())
    week_days['first_friday'] = valid_data['date_start'] + timedelta(days=4 - valid_data['date_start'].weekday())

    return week_days
