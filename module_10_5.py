import time
import multiprocessing


def read_info(name):
    all_data = []
    try:
        with open(name, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                all_data.append(line)
    except FileNotFoundError:
        print(f"Файл {name} не найден")


filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Пример

if __name__ == '__main__':
    print("Линейный вызов:")
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейное выполнение заняло: {end_time - start_time:.6f} секунд")

    print("\nМногопроцессный вызов:")
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессное выполнение заняло: {end_time - start_time:.6f} секунд")
