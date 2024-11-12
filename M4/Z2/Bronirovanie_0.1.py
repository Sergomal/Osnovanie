"""
reservation
freely
occupied
"""


def book_seat(seats):
    seat_name = input("Введите место для бронирования (от Б1 до Б9): ").upper()
    try:
        # Находим индекс места, которое пользователь хочет забронировать
        i = seats.index((seat_name, "свободно"))
        # Отмечаем место как забронированное
        seats[i] = (seat_name, "забронировано")
        print(f"Место '{seat_name}' успешно забронировано.")
    except ValueError:
        print(f"Место '{seat_name}' уже забронировано или не существует.")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


if __name__ == "__main__":

    # Инициализация списка мест с использованием спискового включения
    seats = [(f"Б{i}", "свободно") for i in range(1, 10)]
    # print(seats)

    # Отображение начального состояния бронирования
    print("Начальное состояние бронирования мест:")
    for seat in seats:
        print(f"{seat[0]}: {seat[1]}")

    # Запуск функции бронирования с возможностью повторного ввода
    while True:
        book_seat(seats)
        booking = input("Хотите забронировать еще одно место? (да/нет): ")
        if booking.lower() != "да":
            break

    # Отображение итогового состояния бронирования
    print("Итоговое состояние бронирования мест:")
    for seat in seats:
        print(f"{seat[0]}: {seat[1]}")
