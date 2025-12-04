import matplotlib.pyplot as plt

jurusan = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
jumlah_mahasiswa = [120, 150, 100, 80]


#Basic Bar Chart
plt.bar(jurusan, jumlah_mahasiswa, color='skyblue')
plt.title('Jumlah Mahasiswa per Jurusan')
plt.xlabel('Jurusan')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Menambahkan grid horizontal
plt.show()


#Kustomisasi Basic Bar Chart
colors = ['blue', 'green', 'red', 'purple']

plt.bar(jurusan, jumlah_mahasiswa, color=colors)
plt.title('Jumlah Mahasiswa per Jurusan')
plt.xlabel('Jurusan')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45)

for i, v in enumerate(jumlah_mahasiswa):
    plt.text(i, v + 5, str(v), ha='center')

plt.show()


#Multiple Bar Chart
jumlah_mahasiswa_2024 = [110, 140, 95, 85]

x = range(len(jurusan))  # Indeks posisi untuk batang
width = 0.4

plt.bar(x, jumlah_mahasiswa, width=width, label='2023', color='skyblue')
plt.bar([p + width for p in x], jumlah_mahasiswa_2024, width=width, label='2024', color='orange')

plt.title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
plt.xlabel('Jurusan')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45)

plt.legend()
plt.show()


#Melihat Pola dan Trend
jurusan = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
tahun = ['2019', '2020', '2021', '2022', '2023']
data = {
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [100, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

width = 0.2
x = range(len(tahun))


plt.bar(x, data['Ilmu Komputer'], width=width, label='Ilmu Komputer', color='blue')
plt.bar([p + width for p in x], data['Sistem Informasi'], width=width, label='Sistem Informasi', color='green')
plt.bar([p + width*2 for p in x], data['Teknik Informatika'], width=width, label='Teknik Informatika', color='orange')
plt.bar([p + width*3 for p in x], data['Data Science'], width=width, label='Data Science', color='purple')

plt.title('Tren Jumlah Mahasiswa per Jurusan (2019-2023)')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Mahasiswa')
plt.xticks([p + width*1.5 for p in range(len(tahun))], tahun)  # menaruh label tahun di tengah grup batang
plt.legend()
plt.show()