LINK PWS : http://alica-kinar-aliciousflorist.pbp.cs.ui.ac.id/ 

1. Cara Implementasi Checklist Secara Step-by-Step
- Buat proyek Django
Dengan menjalankan perintah django-admin startproject myproject di terminal, saya memulai proyek baru.
- Membuat aplikasi main
Saya menjalankan python manage.py startapp main untuk membuat aplikasi bernama 'main'.
- Routing aplikasi main
Di dalam urls.py pada proyek utama, saya menambahkan path ke aplikasi main dengan include('main.urls').
- Membuat model Product
Di models.py pada aplikasi main, saya mendefinisikan model Product dengan atribut name, price, dan description.
- Membuat views.py
Saya membuat fungsi di views.py untuk menampilkan nama aplikasi dan nama kelas saya, lalu dihubungkan dengan template HTML.
- Routing views.py
Di urls.py aplikasi main, saya menambahkan path ke fungsi yang ada di views.py.
- Deployment ke PWS
Setelah memastikan aplikasi berjalan dengan baik di localhost, saya deploy ke PWS menggunakan cf push.
- README.md
README berisi link aplikasi yang di-deploy dan jawaban dari pertanyaan yang diberikan.

2. Request Client  -------->  urls.py (Main Project)  -------->  urls.py (Main App)  -------->  views.py
                                                   \                                      |
                                                    \                                   (Optional)
                                                     \--->  models.py (Database)  --------/
                                                              |
                                                              v
                                                  Template HTML  -------->  Response Client

Penjelasan:

- Request Client: Client mengirimkan request ke server.
- urls.py (Main Project): Mencocokkan URL request ke aplikasi terkait (Main App).
- urls.py (Main App): Mencocokkan URL di aplikasi dan memetakan ke fungsi yang sesuai di views.py.
- views.py: Mengelola logika, mengambil data dari models.py.
- models.py (Opsional): Berfungsi untuk berinteraksi dengan database jika ada data yang perlu diambil.
- Template HTML: Menampilkan data yang dikirimkan dari views dan mengembalikan response ke client.

3. Fungsi Git dalam Pengembangan Perangkat Lunak
Git berfungsi sebagai version control system (VCS) yang melacak perubahan kode dalam proyek. Git memungkinkan developer bekerja secara kolaboratif tanpa risiko kehilangan data atau benturan versi kode. Dengan Git, developer dapat membuat branch, melakukan commit, dan merge perubahan mereka, menjaga kode tetap rapi dan terorganisir. Fungsi Git juga mencakup rollback ke versi sebelumnya jika terjadi kesalahan.

4. Kenapa Django Dijadikan Framework Permulaan?
Django dipilih karena memiliki struktur yang jelas dan lengkap, serta menyediakan tools bawaan seperti admin panel, ORM, dan security features, yang memudahkan pemula memahami konsep dasar web development. Django juga menggunakan arsitektur MVT (Model-View-Template), yang sangat membantu pemula dalam memahami bagaimana aplikasi web bekerja secara keseluruhan.

5. Kenapa Model di Django Disebut ORM?
ORM (Object-Relational Mapping) di Django memungkinkan kita untuk berinteraksi dengan database menggunakan objek Python alih-alih menulis SQL. Model di Django adalah representasi dari tabel database dalam bentuk class, yang mempermudah proses pengambilan dan manipulasi data tanpa perlu memahami query SQL secara mendalam.