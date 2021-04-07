# Tucil-3-Stima-2020

Program ini dibuat untuk memenuhi tugas Mata Kuliah **IF 2211 Strategi Algoritma** <br />

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester II Tahun 2020/2021*


## Description
Algoritma A* merupakan salah satu algoritma yang populer untuk mencari lintasan terpendek antara dua titik. Pada prinsipnya, A* bekerja dengan cara Greedy Best-First-Search yang memanfaatkan sebuah heuristik dalam mencari sebuah lintasan. Pada  proses pencariannya, Algoritma A* menggabungkan apa yang dilakukan Algoritma Dijkstra (memprioritaskan simpul yang lebih dekat dengan titik awal) dengan Greedy Best-First-Search (memprioritaskan simpul yang lebih dekat dengan titik akhir). Dalam terminologi standar, Algoritma A* dinyatakan dengan rumus<br />

*f(n) = g(n) + h(n)* <br />

dengan g(n) merepresentasikan exact cost yang dibutuhkan dari starting node ke titik n, sedangkan h(n) merepresentasikan nilai estimasi heuristik dari titik n ke goal node.
<br />

Langkah-langkah program :
1. Baca persoalan
2. Tambahkan start node ke opened list
3. Selama opened list tidak kosong, lakukan :
   - Cari f dengan nilai terkecil yang ada di opened list yang akan disebut n (*current node*)
   - Untuk setiap node yang bertentangga dengan current node, lakukan :
     - Jika simpul hidup belum berada di opened list, tambahkan node tersebut ke dalam list, kemudian jadikan current node sebagai parent dari node tetangga, hitung cost dari node tetangga yg ditambahkan.
     - Jika simpul hidup sudah berada di opened list, lakukan pengecekan apakah path yang dibentuk lebih baik dari segi cost. Jika ada assign sebagai current node.
   - Berhenti ketika :
     - Path telah ditemukan, atau
     - Gagal menemukan node tujuan dan opened listnya kosong yang berarti tidak ada path.

**LINK LAPORAN** <br />
*[Laporan](http://bit.ly/bukanLaporanTucil3Stima)*

## Build With

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries

- gmaps
- math

#### Installing gmaps
```
$ conda install -c conda-forge maps
```
#### Installing math
```
$ pip3 install math
```

## Getting Started

### Executing program

- Buka Terminal atau Command Line
- Arahkan directory ke dalam folder yang berisi file dan folder yang sudah di download
- Kemudian arahkan directory ke dalam folder src (AStarPathFinder\src)
- Buka jupyter notebook dengan command dibawah ini :
```
$ jupyter notebook
```
- Buka file `AStarPathFinder.ipynb`


## Author
Daru Bagus Dananjaya (13519080)
Shifa Salsabiila (13519106)