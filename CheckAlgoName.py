import os
import re

def process_directory(directory_path):
    print(f"Начало проверки каталога: {directory_path}")
    
    # Проверяем, существует ли каталог
    if not os.path.isdir(directory_path):
        print(f"Ошибка: Указанный путь не является каталогом: {directory_path}")
        return
    
    # Получаем список файлов в каталоге
    files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
    if not files:
        print("Нет текстовых файлов для обработки.")
        return
    
    total_methods = 0
    error_count = 0

    # Обрабатываем каждый файл
    for file_name in files:
        module_name = os.path.splitext(file_name)[0]  # Имя модуля (без расширения)
        file_path = os.path.join(directory_path, file_name)
        print(f"Обработка файла: {file_name} (Имя модуля: {module_name})")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except Exception as e:
            print(f"Ошибка при чтении файла {file_name}: {e}")
            continue
        
        # Обработка строк файла
        inside_method = False
        method_name = None
        algorithm_found = False
        method_start_line = None

        for line_number, line in enumerate(lines, start=1):
            line = line.strip()
            
            # Проверяем начало метода
            match = re.match(r'(?i)(Процедура|Функция)\s+(\w+)', line)
            if match:
                if inside_method:
                    print(f"Ошибка: Метод {method_name} не завершен в файле {file_name} "
                          f"(строка {method_start_line}).")
                    error_count += 1
                
                inside_method = True
                method_name = match.group(2)
                method_start_line = line_number
                algorithm_found = False
                total_methods += 1
                continue
            
            # Проверяем конец метода
            if inside_method and re.match(r'(?i)(КонецПроцедуры|КонецФункции)', line):
                if not algorithm_found:
                    print(f"Ошибка: В файле {file_name}, метод {method_name} (строка {method_start_line}): "
                          f"Не найдена строка с ТекстАлгоритмаЗамены.")
                    error_count += 1
                inside_method = False
                method_name = None
                method_start_line = None
                continue
            
            # Ищем строку с ТекстАлгоритмаЗамены
            if inside_method:
                algo_match = re.search(r'ТекстАлгоритмаЗамены\("([^"]+)"\)', line)
                if algo_match:
                    algorithm_name = algo_match.group(1)
                    expected_name = f"{module_name}_{method_name}"
                    if algorithm_name != expected_name:
                        print(f"Ошибка: В файле {file_name}, метод {method_name} (строка {method_start_line}): "
                              f"Имя алгоритма '{algorithm_name}' не совпадает с '{expected_name}'.")
                        error_count += 1
                    algorithm_found = True

    print(f"Проверка завершена. Обработано методов: {total_methods}. Найдено ошибок: {error_count}.")

# Пример вызова функции
if __name__ == "__main__":
    directory = input("Введите путь к каталогу с файлами: ")
    process_directory(directory)