# -*- coding: utf-8 -*-
nama = input("Masukkan nama mahasiswa: " )
nim = input("Masukkan NIM: ")
nilai = int(input("Masukkan nilai ujian (0-100): "))

print("\nNama: ", nama, "(type: ",type(nama),")")
print("NIM: ", nim, "(type: ",type(nim),")")
print("Nilai: ", nilai, "(type: ",type(nilai),")")

print("\nHasil Evaluasi:")
print("Mahasiswa: ", nama, "( NIM: ",nim,")")
print("Nilai Ujian: ", nilai)

if nilai >= 85 and nilai <= 100 :
    kategori = "A (Sangat Baik)"
elif nilai >= 75 and nilai <= 84 :
    kategori = "B (Baik)"
elif nilai >= 60 and nilai <= 74 :
    kategori = "C (Cukup)"
elif nilai >= 40 and nilai <= 59 :
    kategori = "D (Kurang)"
elif nilai <= 40 :
    kategori = "E (Sangat Kurang)"
else:
  print("Nilai tidak valid")

print("Kategori Nilai:", kategori)

nama = input("Masukkan nama mahasiswa: " )
nim = input("Masukkan NIM: ")
nilai = int(input("Masukkan nilai ujian (0-100): "))

print(f"\nNama: {nama} (type: {type(nama)})")
print(f"NIM: {nim} (type: {type(nim)})")
print(f"Nilai: {nilai} (type: {type(nilai)})")

print("\nHasil Evaluasi:")
print(f"Mahasiswa: {nama} (NIM: {nim})")
print("Nilai Ujian: ", nilai,)

if nilai >= 85 and nilai <= 100 :
    kategori = "A (Sangat Baik)"
elif nilai >= 75 and nilai <= 84 :
    kategori = "B (Baik)"
elif nilai >= 60 and nilai <= 74 :
    kategori = "C (Cukup)"
elif nilai >= 40 and nilai <= 59 :
    kategori = "D (Kurang)"
elif nilai <= 40 :
    kategori = "E (Sangat Kurang)"
else:
  print("Nilai tidak valid")

print("Kategori Nilai:", kategori)
