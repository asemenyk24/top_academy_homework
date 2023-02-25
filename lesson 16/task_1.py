import random as rng
from tkinter import *
from tkinter import messagebox

array1 = []
array2 = []


def random_arr():
    """Генерирует 2 массива случайных чисел в заданном диапазоне"""
    try:
        min_num = int(min_entry.get())
        max_num = int(max_entry.get())
    except ValueError:
        messagebox.showinfo("Error", "Use integer numbers only!")
    else:
        global array1
        global array2
        if min_num < max_num:
            array1 = [rng.randint(min_num, max_num) for i in range(6)]
            array2 = [rng.randint(min_num, max_num) for i in range(6)]
            # messagebox.showinfo("Generated arrays", f"First array: {array1}, \nSecond array: {array2}.")
            arraysOnHand.delete("1.0", "end")
            arraysOnHand.insert(0.0, f"1st:{array1},\n2nd:{array2}.")
        elif min_num >= max_num:
            messagebox.showinfo("Error", "Please enter correct range!")


def unite_arr():
    """Объединяет 2 массива"""
    result = array1 + array2
    messagebox.showinfo("United array", f"United array: {result}.")


def norep_arr():
    """Объединяет без повторений"""
    result = list(set(array1 + array2))
    messagebox.showinfo("United arrays without reps", f"United array without repeats: {result}.")


def rep_elements():
    """Выводит массив, состоящий из общих элементов"""
    result = list(set([i for i in (array1 + array2) if i in array1 and i in array2]))
    messagebox.showinfo("Repeating elements", f"Repeating elements from arrays: {result}!")


def unique_elements():
    """Выводит массив уникальных элементов из родительских массивов"""
    unique_arr1 = list(set(array1))
    unique_arr2 = list(set(array2))
    result = unique_arr1 + unique_arr2
    messagebox.showinfo("Unique elements", f"Unique elements from arrays: {result}!")


def min_and_max():
    arr1 = sorted(array1)
    arr2 = sorted(array2)
    arr3 = [arr1[0], arr1[-1], arr2[0], arr2[-1]]
    messagebox.showinfo("Minimum and maximum", f"Minimum and maximum numbers from both arrays: {arr3}.")


window = Tk()
window.title('Operations with two arrays')
window.geometry('500x300')
"""Настройки окна программы"""

frame = Frame(window, padx=10, pady=5, width = 500, height = 250)
frame.pack(expand = True)

frame2 = Frame(window, height = 50)
frame2.pack(expand = True)

"""Подсказка для поля ввода"""
min_number_lb = Label(frame, text='Enter min number: ')
min_number_lb.grid(row = 0, column = 0)

max_number_lb = Label(frame, text='Enter max number: ')
max_number_lb.grid(row = 1, column = 0)

"""Поле ввода"""
min_entry = Entry(frame)
min_entry.grid(row = 0, column = 1, pady = 10)

max_entry = Entry(frame)
max_entry.grid(row = 1, column = 1, pady = 10)

"""Тык."""
generateArr_btn = Button(frame, text = 'Generate', command = random_arr)
generateArr_btn.grid(row = 2, column = 1, pady = 10)

sumArrays_btn = Button(frame, text = '1', command = unite_arr)
sumArrays_btn.grid(row = 0, column = 2, padx = 10)

sumNoRepeat_btn = Button(frame, text = '2', command = norep_arr)
sumNoRepeat_btn.grid(row = 1, column = 2, padx = 10)

onlyRep_btn = Button(frame, text = '3', command = rep_elements)
onlyRep_btn.grid(row = 2, column = 2, padx = 10)

uniqueElem_btn = Button(frame, text = '4', command = unique_elements)
uniqueElem_btn.grid(row = 3, column = 2, padx = 10)

minmaxNum_btn = Button(frame, text = '5', command = min_and_max)
minmaxNum_btn.grid(row = 4, column = 2, padx = 10)

arraysOnHand = Text(frame2, width = 40, height = 3, wrap = WORD)
arraysOnHand.grid(row = 3, column = 1, pady = 10)

btn_lb_un = Label(frame, text='Unite arrays')
btn_lb_un.grid(row = 0, column = 3, pady = 10)

btn_lb_noRep = Label(frame, text='Unite, no reps')
btn_lb_noRep.grid(row = 1, column = 3, pady = 10)

btn_lb_onlyReps = Label(frame, text='Reps only')
btn_lb_onlyReps.grid(row = 2, column = 3, pady = 10)

btn_lb_unique = Label(frame, text='Unique elements')
btn_lb_unique.grid(row = 3, column = 3, pady = 10)

btn_lb_minMax = Label(frame, text='Min and max')
btn_lb_minMax.grid(row = 4, column = 3, pady = 10)

window.mainloop()
