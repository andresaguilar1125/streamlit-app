# Series
def get_trip(x : str):
    trip_mapping = {
        'Uber': 'Uber',
        'Didi': 'Didi',
        'Pirata': 'Pirata'
    }
    
    for prefix, trip_value in trip_mapping.items():
        if x.startswith(prefix):
            return trip_value
    return None

def get_person(x : str):
    person_mapping = {
        'Andres': 'Andres',
        'Doris': 'Doris',
        'Mari': 'Mari',
        'Marvin': 'Marvin',
        'Miriam': 'Miriam',
        'Sam': 'Sam'
    }
    
    for name, search_string in person_mapping.items():
        if search_string in x:
            return name
    return None

def get_week(date_obj):
    week_num = (date_obj.day - 1) // 7 + 1
    return f"W{week_num}"