# 🎧 Spotify Wrapped

Project ini akan menampilkan data untuk:
- 🎵 **Top 10 lagu yang paling sering kamu dengar**
- 🎤 **Top 10 artis favoritmu**

Berdasarkan histori pemutaran **1 tahun terakhir**.

---

## 🛠️ Yang digunakan
- Python 3
- [Spotipy](https://spotipy.readthedocs.io/)
- [Spotify Web API](https://developer.spotify.com/dashboard)

---

## 📦 Instalasi

1. **Clone repository** (atau unduh file script ini)

```bash
git clone https://github.com/fahilsum/spotify-wrapped.git
cd spotify-wrapped
```
2. **Install dependency**

```bash
pip install -r requirements.txt
```

3. **Membuat Spotify App**

- Kunjungi: https://developer.spotify.com/dashboard
- Klik Create app
- App Name: `Spotify Wrapped`
- App Desc: `Spotify Wrapped`
- Tambahkan Redirect URI berikut di pengaturan app:

```
http://127.0.0.1:8888/callback
```
- Checklist Web API ✔️
- Catat atau copy:
  - `Client ID`
  - `Client Secret` ( klik _View client secret_)
---

## ⚙️ Konfigurasi

Ganti kredensial berikut di dalam kode `spotify_wrapped.py`:

```python
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
```

---

## ▶️ Cara menjalankan

Jalankan script dengan perintah:

```bash
python spotify_wrapped.py
```

### Saat pertama kali dijalankan:
- Browser akan terbuka otomatis
- Login ke akun Spotify
- Berikan izin akses aplikasi

---

## 📊 Contoh Output

| Top 10 Tracks | Top 10 Artists |
| :---: | :---: |
| <img src="https://i.ibb.co.com/3GzVQk6/top10tracks.png" width="400"> | <img src="https://i.ibb.co.com/39cp0dCc/top10artists.png" width="400"> |

