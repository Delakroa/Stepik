def reverse_time() -> None:
    time = int(input("Введите время: "))
    time_hours: int = time // 60
    time_minute: int = time % 60
    return print(f"{time} мин - это {time_hours} час {time_minute} минут.")


reverse_time()
