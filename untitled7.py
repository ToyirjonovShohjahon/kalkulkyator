# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14RLiR_PfupOG58o74UGLiPZViQgVbAo2
"""

# Funksiyani aniqlaymiz
def kalkulyator():
    print("Oddiy kalkulyator dasturiga xush kelibsiz!")
    print("Amallar:")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")

    # Foydalanuvchidan amal tanlashni so'raymiz
    amal = input("Amal raqamini tanlang (1/2/3/4): ")

    # Foydalanuvchidan ikkita sonni kiritishni so'raymiz
    try:
        birinchi_son = float(input("Birinchi sonni kiriting: "))
        ikkinchi_son = float(input("Ikkinchi sonni kiriting: "))
    except ValueError:
        print("Faqat raqam kiriting!")
        return

    # Amalni bajarish
    if amal == "1":
        print(f"Natija: {birinchi_son} + {ikkinchi_son} = {birinchi_son + ikkinchi_son}")
    elif amal == "2":
        print(f"Natija: {birinchi_son} - {ikkinchi_son} = {birinchi_son - ikkinchi_son}")
    elif amal == "3":
        print(f"Natija: {birinchi_son} * {ikkinchi_son} = {birinchi_son * ikkinchi_son}")
    elif amal == "4":
        if ikkinchi_son != 0:
            print(f"Natija: {birinchi_son} / {ikkinchi_son} = {birinchi_son / ikkinchi_son}")
        else:
            print("Nolga bo'lish mumkin emas!")
    else:
        print("Noto'g'ri amal tanlandi!")

# Kalkulyatorni ishga tushiramiz
kalkulyator()