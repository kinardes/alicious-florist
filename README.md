TUGAS 2 ☆*: .｡. o(≧▽≦)o .｡.:*☆ 

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

TUGAS 3 ☆*: .｡. o(≧▽≦)o .｡.:*☆

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery sangat penting dalam pengimplementasian sebuah platform karena memungkinkan pertukaran informasi secara efisien antara komponen-komponen sistem. Platform yang memerlukan interaksi data, seperti pengambilan, pengiriman, dan pembaruan informasi, harus memiliki mekanisme data delivery yang baik untuk menjaga integritas dan kecepatan akses data. Data delivery juga membantu menyampaikan data dalam format yang bisa diolah oleh komponen lain, mendukung integrasi dengan berbagai sistem eksternal, serta memastikan bahwa data yang dikirim akurat, lengkap, dan sampai ke tujuan dengan aman.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON (JavaScript Object Notation) lebih baik dan lebih populer dibandingkan XML (eXtensible Markup Language) dalam konteks web karena beberapa alasan. JSON memiliki format yang lebih ringkas dan mudah dibaca oleh manusia serta mesin. Strukturnya yang menggunakan objek dan array lebih cocok untuk data yang kompleks dan nested. Selain itu, JSON lebih efisien dalam hal parsing dan memerlukan bandwidth yang lebih sedikit dibandingkan XML karena tidak menggunakan tag pembuka dan penutup sebanyak XML. JSON juga terintegrasi dengan baik dengan JavaScript dan berbagai bahasa pemrograman lainnya, sehingga lebih praktis digunakan dalam pengembangan aplikasi web modern.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan dan validasi yang telah didefinisikan di model atau form tersebut. Method ini memastikan bahwa hanya data yang valid yang akan diproses lebih lanjut. Method is_valid() digunakan untuk memeriksa apakah data yang dikirim melalui form valid. Jika kondisi terpenuhi, data form akan disimpan ke dalam basis data dengan form. User akan diarahkan ke halaman utama dengan redirect. Menggunakan is_valid() mencegah data yang tidak valid atau berbahaya masuk ke sistem, menjaga integritas dan keamanan data.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF (Cross-Site Request Forgery) token diperlukan pada form di Django untuk melindungi aplikasi dari serangan CSRF. Serangan CSRF terjadi ketika penyerang meniru tindakan pengguna yang terautentikasi tanpa izin, seperti mengirimkan form dari situs berbahaya. Dengan menambahkan csrf_token, Django memastikan bahwa setiap permintaan form berasal dari pengguna yang sah dengan memberikan token unik pada setiap sesi pengguna. Jika CSRF token tidak ditambahkan, penyerang dapat memanfaatkan celah tersebut untuk mengeksekusi tindakan yang tidak diinginkan seperti manipulasi data atau serangan lainnya. Pengaturan CSRF_TRUSTED_ORIGINS memastikan bahwa hanya asal permintaan tertentu yang dianggap tepercaya, menambah lapisan keamanan dalam aplikasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Saya mulai dengan membuat input form untuk menambahkan objek model pada aplikasi dengan membuat form menggunakan Django ModelForm di forms.py. Form ini digunakan untuk menangani input data dari pengguna dan ditampilkan di halaman web.
- Selanjutnya, saya menambahkan 4 fungsi views baru di views.py untuk menampilkan objek dalam format XML, JSON, XML by ID, dan JSON by ID. Untuk implementasi ini, saya menggunakan Django serializers untuk mengubah queryset model menjadi representasi XML dan JSON.
- Setelah membuat views, saya menambahkan routing URL untuk masing-masing views di urls.py dengan menggunakan fungsi path untuk menghubungkan URL ke fungsi view yang telah dibuat pada langkah sebelumnya.
- Saya kemudian menjawab beberapa pertanyaan yang relevan dengan project pada README.md di root folder untuk mendokumentasikan proses dan penjelasan terkait fitur-fitur yang telah ditambahkan.
- Selanjutnya, saya mengakses keempat URL yang telah dibuat (untuk XML, JSON, XML by ID, dan JSON by ID) menggunakan Postman untuk memastikan bahwa mereka bekerja dengan benar. Saya melakukan tes dengan mengirimkan permintaan GET ke setiap URL dan mengambil screenshot hasilnya.
- Terakhir, saya menambahkan screenshot hasil dari Postman ke dalam README.md sebagai dokumentasi. Setelah semuanya siap, saya melakukan git add, commit, dan push ke repositori GitHub untuk menyimpan perubahan. Saya memastikan workflow CI/CD berjalan dengan baik setelah push tersebut.

Screenshot Postman https://drive.google.com/drive/folders/1vOK4n4F3WPT17B6r80q7PbYnxnNEqHdI?usp=sharing 




