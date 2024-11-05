# test_emulator.py
import unittest
import os
import sys
import tarfile
import shutil
from datetime import datetime
from emulator import ShellEmulator
import csv

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        # Создаем временную файловую систему для тестов
        self.vfs_path = 'test_vfs.tar'
        self.tmp_dir = 'tmp'
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)
        os.makedirs('test_vfs_dir/sub_dir', exist_ok=True)
        with open('test_vfs_dir/test_file.txt', 'w') as f:
            f.write('Sample text')
        with tarfile.open(self.vfs_path, 'w') as tar:
            tar.add('test_vfs_dir/', arcname='/')
        shutil.rmtree('test_vfs_dir')
        self.log_path = 'test_log.csv'
        self.username = 'test_user'
        self.emulator = ShellEmulator(self.username, self.vfs_path, self.log_path)

    def tearDown(self):
        # Удаляем временные файлы и директории после тестов
        if os.path.exists(self.vfs_path):
            os.remove(self.vfs_path)
        if os.path.exists(self.log_path):
            os.remove(self.log_path)
        self.emulator.cleanup()
        if os.path.exists('test_vfs_dir'):
            shutil.rmtree('test_vfs_dir')

    # Тесты для команды ls
    def test_ls_root_directory(self):
        output = self.emulator.ls()
        self.assertIn('sub_dir', output)
        self.assertIn('test_file.txt', output)

    def test_ls_empty_directory(self):
        self.emulator.execute_command('cd sub_dir')
        output = self.emulator.ls()
        self.assertEqual(output, 'Пустая директория')

    def test_ls_nonexistent_directory(self):
        self.emulator.current_directory = '/nonexistent'
        output = self.emulator.ls()
        self.assertEqual(output, 'Ошибка: директория не найдена')

    # Тесты для команды cd
    def test_cd_to_subdirectory(self):
        output = self.emulator.cd('sub_dir')
        self.assertEqual(output, 'Перешел в /sub_dir')
        self.assertEqual(self.emulator.current_directory, '/sub_dir')

    def test_cd_to_parent_directory(self):
        self.emulator.current_directory = '/sub_dir'
        output = self.emulator.cd('..')
        self.assertEqual(output, 'Перешел в /')
        self.assertEqual(self.emulator.current_directory, '/')

    def test_cd_nonexistent_directory(self):
        output = self.emulator.cd('nonexistent')
        self.assertEqual(output, 'Ошибка: директория не найдена')
        self.assertEqual(self.emulator.current_directory, '/')

    # Тесты для команды touch
    def test_touch_create_file(self):
        output = self.emulator.touch('new_file.txt')
        self.assertEqual(output, 'Создан файл new_file.txt')
        full_path = os.path.join(self.emulator.tmp_dir, 'new_file.txt')
        self.assertTrue(os.path.isfile(full_path))

    def test_touch_no_filename(self):
        output = self.emulator.touch()
        self.assertEqual(output, 'Ошибка: не указано имя файла')

    def test_touch_in_subdirectory(self):
        self.emulator.cd('sub_dir')
        output = self.emulator.touch('sub_file.txt')
        self.assertEqual(output, 'Создан файл sub_file.txt')
        full_path = os.path.join(self.emulator.tmp_dir, 'sub_dir', 'sub_file.txt')
        self.assertTrue(os.path.isfile(full_path))

    # Тесты для команды rmdir
    def test_rmdir_existing_directory(self):
        os.mkdir(os.path.join(self.emulator.tmp_dir, 'dir_to_remove'))
        output = self.emulator.rmdir('dir_to_remove')
        self.assertEqual(output, 'Успешно удалено dir_to_remove')
        full_path = os.path.join(self.emulator.tmp_dir, 'dir_to_remove')
        self.assertFalse(os.path.exists(full_path))

    def test_rmdir_nonempty_directory(self):
        os.mkdir(os.path.join(self.emulator.tmp_dir, 'nonempty_dir'))
        with open(os.path.join(self.emulator.tmp_dir, 'nonempty_dir', 'file.txt'), 'w') as f:
            f.write('content')
        output = self.emulator.rmdir('nonempty_dir')
        self.assertEqual(output, 'Ошибка: директория не пуста')

    def test_rmdir_nonexistent_directory(self):
        output = self.emulator.rmdir('nonexistent')
        self.assertEqual(output, 'Ошибка: директория не найдена')

    # Тесты для команды uptime
    def test_uptime_format(self):
        output = self.emulator.uptime()
        self.assertTrue(output.startswith('Время работы эмулятора:'))

    def test_uptime_increases_over_time(self):
        import time
        elapsed_before = datetime.now() - self.emulator.start_time
        time.sleep(1)
        output = self.emulator.uptime()
        elapsed_after = datetime.now() - self.emulator.start_time
        self.assertTrue(elapsed_after > elapsed_before)

    def test_uptime_after_commands(self):
        self.emulator.touch('file.txt')
        output = self.emulator.uptime()
        self.assertTrue(output.startswith('Время работы эмулятора:'))

    # Тесты для команды exit
    def test_exit_emulator(self):
        with self.assertRaises(SystemExit) as cm:
            self.emulator.exit_emulator()
        self.assertEqual(str(cm.exception), 'Эмулятор завершен')

    def test_exit_cleans_up_tmp_dir(self):
        try:
            self.emulator.exit_emulator()
        except SystemExit:
            pass
        self.assertFalse(os.path.exists(self.emulator.tmp_dir))

    def test_exit_writes_to_log(self):
        try:
            self.emulator.execute_command('exit')
        except SystemExit:
            pass
        with open(self.log_path, 'r', encoding='utf-8') as f:
            logs = f.readlines()
            last_log = logs[-1]
            self.assertIn('exit', last_log)

    # Дополнительные тесты для команды exit
    def test_exit_with_unsaved_changes(self):
        # Создаем файл перед выходом
        self.emulator.touch('unsaved_file.txt')
        with self.assertRaises(SystemExit):
            self.emulator.execute_command('exit')
        # Проверяем, что файл сохранен
        full_path = os.path.join(self.emulator.tmp_dir, 'unsaved_file.txt')
        self.assertFalse(os.path.exists(full_path))

    def test_exit_from_subdirectory(self):
        self.emulator.cd('sub_dir')
        with self.assertRaises(SystemExit):
            self.emulator.execute_command('exit')
        # Проверяем, что текущая директория сброшена
        self.assertEqual(self.emulator.current_directory, '/sub_dir')

    # Тесты на обработку неверных команд
    def test_invalid_command(self):
        output = self.emulator.execute_command('invalidcmd')
        self.assertEqual(output, 'Ошибка: команда не распознана')

    def test_empty_command(self):
        output = self.emulator.execute_command('')
        self.assertEqual(output, 'Ошибка: команда не распознана')

    def test_command_with_incorrect_args(self):
        output = self.emulator.execute_command('cd')
        self.assertEqual(output, "Ошибка: неверное использование команды 'cd'")

    # Тестирование логирования
    def test_command_logging(self):
        self.emulator.execute_command('ls')
        with open(self.log_path, 'r', encoding='utf-8') as f:
            logs = [line.strip() for line in f]
            last_log = logs[-1]
        self.assertIn('ls', last_log)

    def test_multiple_command_logging(self):
        self.emulator.execute_command('ls')
        self.emulator.execute_command('touch file.txt')
        self.emulator.execute_command('cd sub_dir')
        with open(self.log_path, 'r', encoding='utf-8') as f:
            logs = [line.strip() for line in f]
        self.assertIn('ls', logs[0])
        self.assertIn('touch file.txt', logs[1])
        self.assertIn('cd sub_dir', logs[2])

    def test_log_format(self):
        self.emulator.execute_command('uptime')
        with open(self.log_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.assertEqual(len(row), 4)
                date_str, time_str, username, command = row
                datetime.strptime(date_str, "%Y-%m-%d")
                datetime.strptime(time_str, "%H:%M:%S")
                self.assertEqual(username, self.username)
                self.assertEqual(command, 'uptime')

if __name__ == '__main__':
    unittest.main()
