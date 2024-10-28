import os
import sys
import tarfile
import csv
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext
from shutil import rmtree

class ShellEmulator:
    def __init__(self, username, vfs_path, log_path):
        self.username = username
        self.vfs_path = vfs_path
        self.log_path = log_path
        self.current_directory = '\\'
        self.start_time = datetime.now()
        self.tmp_dir = 'tmp'
        self.load_virtual_file_system()
        self.commands = {
            'ls': self.ls,
            'cd': self.cd,
            'touch': self.touch,
            'rmdir': self.rmdir,
            'uptime': self.uptime,
            'exit': self.exit_emulator
        }

    def load_virtual_file_system(self):
        # Извлекаем содержимое tar-архива во временную папку
        if os.path.exists(self.tmp_dir):
            rmtree(self.tmp_dir)
        os.makedirs(self.tmp_dir, exist_ok=True)
        with tarfile.open(self.vfs_path) as tar:
            tar.extractall(path=self.tmp_dir)

    def write_log(self, command):
        with open(self.log_path, 'a', newline='', encoding='utf-8') as log_file:
            log_writer = csv.writer(log_file)
            log_writer.writerow([datetime.now().strftime("%Y-%m-%d"), 
                                 datetime.now().strftime("%H:%M:%S"),
                                 self.username,
                                 command])

    def execute_command(self, command):
        self.write_log(command)
        command = command.strip()
        if not command:
            return "Ошибка: команда не распознана"
        command_parts = command.split()
        cmd = command_parts[0]
        args = command_parts[1:]

        if cmd in self.commands:
            try:
                return self.commands[cmd](*args)
            except TypeError:
                return f"Ошибка: неверное использование команды '{cmd}'"
            except Exception as e:
                return f"Ошибка: {e}"
        else:
            return "Ошибка: команда не распознана"

    def ls(self):
        path = os.path.join(self.tmp_dir, self.current_directory.strip('\\'))
        if os.path.exists(path):
            entries = os.listdir(path)
            if entries:
                return '\n'.join(entries)
            else:
                return "Пустая директория"
        else:
            return "Ошибка: директория не найдена"

    def cd(self, path=None):
        if path is None:
            return "Ошибка: неверное использование команды 'cd'"
        if path == "..":
            if self.current_directory != '\\':
                self.current_directory = os.path.dirname(self.current_directory.rstrip('\\'))
                if not self.current_directory:
                    self.current_directory = '\\'
            return f"Перешел в {self.current_directory}"
        else:
            new_directory = os.path.join(self.current_directory, path)
            full_path = os.path.join(self.tmp_dir, new_directory.strip('\\'))
            if os.path.isdir(full_path):
                self.current_directory = os.path.normpath(new_directory)
                return f"Перешел в {self.current_directory}"
            else:
                return "Ошибка: директория не найдена"

    def touch(self, filename=None):
        if filename is None:
            return "Ошибка: не указано имя файла"
        full_path = os.path.join(self.tmp_dir, self.current_directory.strip('\\'), filename)
        try:
            open(full_path, 'a').close()
            return f"Создан файл {filename}"
        except Exception as e:
            return f"Ошибка: {e}"

    def rmdir(self, path=None):
        if path is None:
            return "Ошибка: не указана директория"
        full_path = os.path.join(self.tmp_dir, self.current_directory.strip('\\'), path)
        if os.path.isdir(full_path):
            try:
                os.rmdir(full_path)
                return f"Успешно удалено {path}"
            except OSError:
                return "Ошибка: директория не пуста"
            except Exception as e:
                return f"Ошибка: {e}"
        else:
            return "Ошибка: директория не найдена"

    def uptime(self):
        elapsed = datetime.now() - self.start_time
        return f"Время работы эмулятора: {elapsed}"

    def exit_emulator(self):
        self.cleanup()
        sys.exit("Эмулятор завершен")

    def cleanup(self):
        if os.path.exists(self.tmp_dir):
            rmtree(self.tmp_dir)

    def __del__(self):
        self.cleanup()

class GUI:
    def __init__(self, emulator):
        self.emulator = emulator
        self.window = tk.Tk()
        self.window.title("Shell Emulator")
        self.text_area = scrolledtext.ScrolledText(self.window, width=100, height=20)
        self.text_area.pack()
        self.command_entry = tk.Entry(self.window, width=100)
        self.command_entry.pack()
        self.command_entry.focus()
        self.command_entry.bind("<Return>", self.execute_command)
        self.display_output(f"Добро пожаловать, {self.emulator.username}!\n")

    def execute_command(self, event):
        command = self.command_entry.get()
        self.command_entry.delete(0, tk.END)
        output = self.emulator.execute_command(command)
        prompt = f"{self.emulator.username}@emulator:{self.emulator.current_directory}$ {command}\n"
        self.display_output(f"{prompt}{output}\n")

    def display_output(self, output):
        self.text_area.insert(tk.END, output)
        self.text_area.yview(tk.END)

    def run(self):
        self.window.mainloop()

def main():
    if len(sys.argv) != 7:
        print("Использование: python emulator.py --username <имя> --vfs-path <путь> --log-path <путь>")
        sys.exit(1)
    username = sys.argv[2]
    vfs_path = sys.argv[4]
    log_path = sys.argv[6]

    emulator = ShellEmulator(username, vfs_path, log_path)
    gui = GUI(emulator)
    gui.run()

if __name__ == "__main__":
    main()