import threading
import time
import random

TOTAL_SEATS = 10

seats = {f"A{i+1}": True for i in range(TOTAL_SEATS)}

lock = threading.Lock()

sold_count = 0


def print_seats():
    print("\nСтан місць:")
    for seat, available in seats.items():
        status = "Вільне" if available else "Продане"
        print(f"{seat}: {status}")
    print("-" * 30)


def sell_ticket(seller_name):
    global sold_count

    while True:
        with lock:
            free_seats = [seat for seat, available in seats.items() if available]
            if not free_seats:
                print(f"{seller_name}: квитки закінчились")
                return

            chosen_seat = random.choice(free_seats)

            seats[chosen_seat] = False
            sold_count += 1

            print(f"{seller_name} продав квиток на місце {chosen_seat} "
                  f"(всього продано: {sold_count})")

        time.sleep(random.uniform(0.3, 1.0))


def main():
    print("Система продажу квитків запущена\n")

    sellers_count = 4

    threads = []

    for i in range(sellers_count):
        t = threading.Thread(target=sell_ticket, args=(f"Продавець {i+1}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nУсі квитки продано!")
    print_seats()


if __name__ == "__main__":
    main()
