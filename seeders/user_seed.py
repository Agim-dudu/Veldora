from app import app, db
from app.model.user import User  # Sesuaikan folder/file import Anda
from werkzeug.security import generate_password_hash
from datetime import datetime

with app.app_context():
    # 1. Hapus data lama
    try:
        db.session.query(User).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"⚠️ Gagal membersihkan tabel: {e}")

    # 2. Data dummy (disesuaikan dengan field di model User)
    users_data = [
        {
            "username": "SuperAdmin",
            "full_name": "Super Admin",
            "password": "12345",
            "level": 2,
        },
        {
            "username": "ContohGuru",
            "full_name": "Contoh Guru",
            "password": "12345",
            "level": 1,
        },
        {
            "username": "SiswaProgres",
            "full_name": "Siswa Progres",
            "password": "12345",
            "level": 0,
        },
        {
            "username": "SiswaBiasa",
            "full_name": "Siswa Biasa",
            "password": "12345",
            "level": 0,
        },
    ]

    # 3. Loop dan masukkan data
    for u in users_data:
        # Menggunakan method set_password jika ingin lebih rapi, 
        # atau langsung hash di sini.
        hashed_pw = generate_password_hash(u["password"])

        new_user = User(
            username=u["username"],
            full_name=u["full_name"],
            password=hashed_pw,
            level=u["level"]
        )

        db.session.add(new_user)

    try:
        db.session.commit()
        print("✅ Seeder User berhasil! Data user sudah masuk sesuai model baru.")
    except Exception as e:
        db.session.rollback()
        print(f"❌ Terjadi kesalahan saat commit: {e}")