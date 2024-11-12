def analyze_log(file_name):
    counter = {"INFO": 0, "ERROR": 0, "WARNING": 0, "DEBUG": 0, "NOTICE":0, }

    try:
        with open(file_name) as file:
            for line in file:
                if "[INFO]" in line:
                    counter["INFO"] += 1
                elif "[ERROR]" in line:
                    counter["ERROR"] += 1
                elif "[WARNING]" in line:
                    counter["WARNING"] += 1
                elif "[DEBUG]" in line:
                    counter["DEBUG"] += 1
                elif "[NOTICE]" in line:
                    counter["NOTICE"] += 1

        for event, count in counter.items():
            print(f"{event}: {count}")

    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


analyze_log('log.txt')
