import tkinter.filedialog
import tkinter
import pyAesCrypt


def choose_file():
    filetypes = (("Зашифрованные файлы", "*.aes"),)
    filename = tkinter.filedialog.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        return filename


try:
    file = choose_file()
    password = input('Введите пароль для дешифрования файла: ')
    pyAesCrypt.decryptFile(file, 'decryption.txt', password)
    print('Дешифрование успешно завершено!')
except:
    print('Файл не найден')
