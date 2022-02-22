def convert_time(duration: int) -> str:
    DAY = 86400
    HOUR = 3600
    MINUTE = 60

    if duration // DAY > 0:
        s = duration % MINUTE
        m = (duration % HOUR - s) // MINUTE
        h = (duration % DAY - m) // HOUR
        d = duration // DAY
        return f'{d} дн {h} час {m} мин {s} сек'
    elif duration // HOUR > 0:
        s = duration % MINUTE
        m = (duration % HOUR - s) // MINUTE
        h = duration // HOUR
        return f'{h} час {m} мин {s} сек'
    elif duration // MINUTE > 0:
        s = duration % MINUTE
        m = duration // MINUTE
        return f'{m} мин {s} сек'
    else:
        return f'{duration} сек'


duration = 400153
result = convert_time(duration)
print(result)
