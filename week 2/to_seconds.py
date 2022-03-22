# to_seconds(0, 0, 10, 20) -> 620 seconds

def to_seconds(days, hours, mins, seconds):

    days_as_seconds = days * 24 * 60 * 60
    hours_as_secs = hours * 60 * 60
    mins_as_secs = mins * 60

    return days_as_seconds + hours_as_secs + mins_as_secs + seconds
    

answer = to_seconds(0, 0, 10, 20)
print(answer)
