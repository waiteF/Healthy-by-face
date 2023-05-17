from tkinter import Tk, Button, filedialog, Label
from PIL import Image, ImageTk
from emotions import analysis_data

file_path = "src\\data\\train\\happy\\Training_1206.jpg"

def choose_photo():
    global file_path
    # Відкриваємо діалогове вікно вибору файлу
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    
    if file_path:
        # Відображаємо вибране фото
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Змінюємо розмір зображення
        photo = ImageTk.PhotoImage(image)
        photo_label.configure(image=photo)
        photo_label.image = photo  # Зберігаємо посилання на фото, щоб уникнути видалення з пам'яті

def start_analysis():
    analysis_data(file_path)

# Створюємо графічне вікно
window = Tk()
window.title("Визначити життєздатність людини")
window.geometry("400x450")

# Мітка з текстом
label = Label(window, text="Визначити життєздатність людини")
label.pack(pady=10)

# Кнопка вибору фото
choose_button = Button(window, text="Вибрати фото", command=choose_photo)
choose_button.pack(pady=10)

# Мітка для відображення вибраного фото
photo_label = Label(window)
photo_label.pack()

# Кнопка для запуску аналізу
analyze_button = Button(window, text="Почати аналіз", command=start_analysis)
analyze_button.pack(pady=10)

# Запускаємо цикл обробки подій
window.mainloop()
