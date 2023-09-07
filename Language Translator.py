from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

frame1 = Frame(root, width = 590, height = 370, relief = RIDGE, borderwidth = 5, bg = '#F7DC6F')
frame1.place(x=0, y=0)

Label(root, text = "Language Translator", font = ("Helvetica 20 bold"), fg = "black", bg = '#F7DC6F').pack(pady = 10)


def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest = cl)
        text_entry2.insert('end', output.text)

    
def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')
    
    
a = tk.StringVar()
auto_select = ttk.Combobox(frame1, width = 27, textvariable = a, state = 'randomly', font = ('verdana', 10, 'bold'))
auto_select['values'] = (
                               'Auto Select',
                        )
auto_select.place(x=15, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width = 27, textvariable = l, state = 'randomly', font = ('verdana', 10, 'bold'))
choose_language['values'] = (
        
                 'Afrikaans',
                 'Amharic',
                 'Aragonese',
                 'Arabic',
                 'Assamese',
                 'Armenian',
                 'Avaric',
                 'Azerbaijani',
                 'Bashkir',
                 'Belarusian',
                 'Bulgarian',
                 'Bihari',
                 'Bislama',
                 'Burmese',
                 'Bengali',
                 'Breton',
                 'Bosnian',
                 'Cree',
                 'Czech',
                 'Church Slavic',
                 'Chuvash',
                 'Dutch',
                 'English',
                 'Esperanto'
                 'German',
                 'Greek',
                 'Persian',
                 'Fulah',
    'Finnish',
    'Fijian',
    'Faroese',
    'French',
    'Irish',
    'Gaelic',
    'Galician',
    'Guarani',
    'Gujarati',
    'Hausa',
    'Hebrew',
    'Hindi',
                 'Hungarian',
    
    'Herero',
    'Interlingua',
    'Indonesian',
    'Interlingue',
    'Igbo',
    'Nuosu',
    'Inupiaq',
    'Ido',
    'Icelandic',
    'Italian',
    'Inuktitut',
    'Japanese',
    'Javanese',
    'Georgian',
    'Kongo',
    'Kikuyu',
    'Kuanyama',
    'Kazakh',
    'Greenlandic',
    'Cambodian',
    'Kannada',
    'Korean',
    'Kanuri',
    'Kashmiri',
    'Kurdish',
    'Komi',
    'Cornish',
    'Kirghiz',
    'Latin',
    'Luxembourgish',
    'Ganda',
    'Limburgish',
    'Lingala',
    'Lao',
    'Lithuanian',
    'Luba-Katanga',
    'Latvian',
    'Malagasy',
    'Marshallese',
    'Maori',
    'Macedonian',
    'Malayalam',
    'Mongolian',
    'Marathi',
    'Malay',
    'Maltese',
    'Nauru',
    'Norwegian Bokmål',
    'North Ndebele',
    'Nepali',
    'Ndonga',
    'Dutch',
    'Norwegian Nynorsk',
    'Norwegian',
    'South Ndebele',
    'Navajo',
    'Chichewa',
    'Occitan',
    'Ojibwa',
    'Oromo',
    'Oriya',
    'Ossetian',
    'Punjabi',
    'Pali',
          
    'Polish',
    'Pashto',
    'Portuguese',
    'Quechua',
    'Romansh',
    'Kirundi',
    'Russian',
    'Kinyarwanda',
    'Sanskrit',
    'Sardinian',
    'Sindhi',
    'Sango',
    'Slovak',
                 'Spanish',
    'Somali',
    'Albanian',
    'Serbian',
    'Swati',
    'Sesotho',
    'Sudanese',
    'Swedish',
    'Swahili',
    'Tamil',
    'Telugu',
                 'Tibetan',
    'Tajik',
    'Thai',
    'Tigrinya',
    'Turkmen',
    'Tagalog',
    'Tswana',
    'Tonga',
    'Turkish',
    'Tsonga',
    'Tatar',
    'Twi',
    'Tahitian',
    'Uighur',
    'Ukrainian',
    'Urdu',
    'Uzbek',
    'Venda',
    'Vietnamese',
    'Volapük',
    'Walloon',
    'Wolof',
    'Xhosa',
    'Yiddish',
    'Yoruba',
    'Zhuang',
    'Chinese',
    'Zulu',
    )

choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 = Text(frame1, width = 20,  height = 7, borderwidth = 5, relief = RIDGE, font = ('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1, width = 20,  height = 7, borderwidth = 5, relief = RIDGE, font = ('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(frame1, command = translate, text = "Translate", relief = RAISED, borderwidth = 2, font = ('verdana', 10, 'bold'), bg = '#248aa2', fg = "white", cursor = "hand2")
btn1.place(x=185, y=300)

btn2 = Button(frame1, command = clear, text = "Clear", relief = RAISED, borderwidth = 2, font = ('verdana', 10, 'bold'), bg = '#248aa2', fg = "white", cursor = "hand2")
btn2.place(x=300, y=300)


root.mainloop()
