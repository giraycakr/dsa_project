import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cargo_system import CargoSystem
from enums import CargoStatus
from enums import DeliveryStatus


class CargoSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kargo Takip Sistemi")
        self.system = CargoSystem()

        # Ana notebook oluştur
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)

        # Ana sekmeleri oluştur
        self.create_customer_tab()
        self.create_shipment_tab()
        self.create_route_tab()
        self.create_query_tab()

    def create_customer_tab(self):
        """Müşteri işlemleri sekmesi"""
        customer_frame = ttk.Frame(self.notebook)
        self.notebook.add(customer_frame, text='Müşteri İşlemleri')

        # Müşteri ekleme formu
        ttk.Label(customer_frame, text="Yeni Müşteri Ekle", font=('Helvetica', 12, 'bold')).pack(pady=10)

        form_frame = ttk.Frame(customer_frame)
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Müşteri ID:").grid(row=0, column=0, padx=5, pady=5)
        self.customer_id_entry = ttk.Entry(form_frame)
        self.customer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="İsim:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(form_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Soyisim:").grid(row=2, column=0, padx=5, pady=5)
        self.surname_entry = ttk.Entry(form_frame)
        self.surname_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(customer_frame, text="Müşteri Ekle", command=self.add_customer).pack(pady=10)

    def create_shipment_tab(self):
        """Kargo işlemleri sekmesi"""
        shipment_frame = ttk.Frame(self.notebook)
        self.notebook.add(shipment_frame, text='Kargo İşlemleri')

        # Kargo ekleme formu
        ttk.Label(shipment_frame, text="Yeni Kargo Ekle", font=('Helvetica', 12, 'bold')).pack(pady=10)

        form_frame = ttk.Frame(shipment_frame)
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Müşteri ID:").grid(row=0, column=0, padx=5, pady=5)
        self.ship_customer_id_entry = ttk.Entry(form_frame)
        self.ship_customer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Gönderi ID:").grid(row=1, column=0, padx=5, pady=5)
        self.shipment_id_entry = ttk.Entry(form_frame)
        self.shipment_id_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Teslimat Süresi (gün):").grid(row=2, column=0, padx=5, pady=5)
        self.delivery_time_entry = ttk.Entry(form_frame)
        self.delivery_time_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(shipment_frame, text="Kargo Ekle", command=self.add_shipment).pack(pady=10)

    def create_query_tab(self):
        """Sorgulama sekmesi"""
        query_frame = ttk.Frame(self.notebook)
        self.notebook.add(query_frame, text='Sorgulama')

        # Notebook için sorgulama sekmeleri
        query_notebook = ttk.Notebook(query_frame)
        query_notebook.pack(fill='both', expand=True, padx=5, pady=5)

        # 1. Kargo Sorgulama Sekmesi
        cargo_query_frame = ttk.Frame(query_notebook)
        query_notebook.add(cargo_query_frame, text='Kargo Sorgula')

        ttk.Label(cargo_query_frame, text="Gönderi ID:").pack(pady=5)
        self.search_id_entry = ttk.Entry(cargo_query_frame)
        self.search_id_entry.pack(pady=5)
        ttk.Button(cargo_query_frame, text="Sorgula", command=self.query_shipment).pack(pady=5)

        # Sonuç alanı
        self.result_text = tk.Text(cargo_query_frame, height=8, width=50)
        self.result_text.pack(pady=5, padx=5)

        # 2. Müşteri Geçmişi Sekmesi
        history_frame = ttk.Frame(query_notebook)
        query_notebook.add(history_frame, text='Müşteri Geçmişi')

        ttk.Label(history_frame, text="Müşteri ID:").pack(pady=5)
        self.history_customer_id = ttk.Entry(history_frame)
        self.history_customer_id.pack(pady=5)
        ttk.Button(history_frame, text="Geçmişi Göster", command=self.show_customer_history).pack(pady=5)

        self.history_text = tk.Text(history_frame, height=8, width=50)
        self.history_text.pack(pady=5, padx=5)

        # 3. Teslimat Süresi Sekmesi
        delivery_frame = ttk.Frame(query_notebook)
        query_notebook.add(delivery_frame, text='Teslimat Süresi')

        ttk.Label(delivery_frame, text="Şehir ID:").pack(pady=5)
        self.delivery_city_id = ttk.Entry(delivery_frame)
        self.delivery_city_id.pack(pady=5)
        ttk.Button(delivery_frame, text="Süre Hesapla", command=self.calculate_city_delivery_time).pack(pady=5)

        self.delivery_text = tk.Text(delivery_frame, height=8, width=50)
        self.delivery_text.pack(pady=5, padx=5)

        # 4. Kargo Listesi Sekmesi
        list_frame = ttk.Frame(query_notebook)
        query_notebook.add(list_frame, text='Kargo Listesi')

        ttk.Button(list_frame, text="Teslim Edilmiş Kargoları Göster",
                   command=self.show_delivered_shipments).pack(pady=5)
        ttk.Button(list_frame, text="Teslim Edilmemiş Kargoları Göster",
                   command=self.show_undelivered_shipments).pack(pady=5)

        self.list_text = tk.Text(list_frame, height=8, width=50)
        self.list_text.pack(pady=5, padx=5)

    def create_route_tab(self):
        """Rota işlemleri sekmesi"""
        route_frame = ttk.Frame(self.notebook)
        self.notebook.add(route_frame, text='Rota İşlemleri')

        # Sol taraf - Şehir ekleme formu
        form_frame = ttk.LabelFrame(route_frame, text="Yeni Şehir Ekle")
        form_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=5, pady=5)

        ttk.Label(form_frame, text="Üst Şehir ID:").pack(pady=5)
        self.parent_city_entry = ttk.Entry(form_frame)
        self.parent_city_entry.pack(pady=5)

        ttk.Label(form_frame, text="Şehir ID:").pack(pady=5)
        self.city_id_entry = ttk.Entry(form_frame)
        self.city_id_entry.pack(pady=5)

        ttk.Label(form_frame, text="Şehir Adı:").pack(pady=5)
        self.city_name_entry = ttk.Entry(form_frame)
        self.city_name_entry.pack(pady=5)

        ttk.Button(form_frame, text="Şehir Ekle", command=self.add_city).pack(pady=10)

        # Sağ taraf - Rota görüntüleme
        view_frame = ttk.LabelFrame(route_frame, text="Rota Görünümü")
        view_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=5, pady=5)

        # Rota gösterimi için Text widget
        self.route_text = tk.Text(view_frame, height=15, width=40)
        self.route_text.pack(padx=5, pady=5)

        ttk.Button(view_frame, text="Rotaları Göster", command=self.show_routes).pack(pady=5)

    def show_customer_history(self):
        """Müşterinin gönderim geçmişini gösterir"""
        customer_id = self.history_customer_id.get()
        if not customer_id:
            messagebox.showerror("Hata", "Müşteri ID giriniz!")
            return

        history = self.system.get_customer_history(customer_id)
        self.history_text.delete(1.0, tk.END)

        if history:
            self.history_text.insert(tk.END, "Gönderim Geçmişi (Tarihe göre sıralı):\n\n")
            for shipment in history:
                self.history_text.insert(tk.END, f"Gönderi ID: {shipment.shipment_id}\n")
                self.history_text.insert(tk.END, f"Tarih: {shipment.shipment_date}\n")
                self.history_text.insert(tk.END, f"Durum: {shipment.cargo_status.value}\n")
                self.history_text.insert(tk.END, "-" * 40 + "\n")
        else:
            self.history_text.insert(tk.END, "Gönderim geçmişi bulunamadı!")
    def show_routes(self):
        """Rota ağacını görselleştirir"""
        self.route_text.delete(1.0, tk.END)
        self._print_tree(self.system.delivery_tree.root)

    def _print_tree(self, node, level=0):
        """Ağaç yapısını recursive olarak görselleştirir"""
        if not node:
            self.route_text.insert(tk.END, "Henüz rota eklenmemiş!\n")
            return

        indent = "  " * level
        self.route_text.insert(tk.END, f"{indent}└── {node.city_name} (ID: {node.city_id})\n")

        for child in node.children:
            self._print_tree(child, level + 1)
    def add_customer(self):
        """Müşteri ekleme işlemi"""
        customer_id = self.customer_id_entry.get()
        name = self.name_entry.get()
        surname = self.surname_entry.get()

        if not all([customer_id, name, surname]):
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")
            return

        if self.system.add_customer(customer_id, name, surname):
            messagebox.showinfo("Başarılı", "Müşteri başarıyla eklendi!")
            # Formu temizle
            self.customer_id_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            self.surname_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Müşteri eklenirken bir hata oluştu!")

    def add_shipment(self):
        """Kargo ekleme işlemi"""
        customer_id = self.ship_customer_id_entry.get()
        shipment_id = self.shipment_id_entry.get()
        delivery_time = self.delivery_time_entry.get()

        if not all([customer_id, shipment_id, delivery_time]):
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun!")
            return

        try:
            delivery_time = int(delivery_time)
        except ValueError:
            messagebox.showerror("Hata", "Teslimat süresi sayı olmalıdır!")
            return

        if self.system.add_shipment(shipment_id, customer_id, delivery_time):
            messagebox.showinfo("Başarılı", "Kargo başarıyla eklendi!")
            # Formu temizle
            self.ship_customer_id_entry.delete(0, tk.END)
            self.shipment_id_entry.delete(0, tk.END)
            self.delivery_time_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Kargo eklenirken bir hata oluştu!")

    def query_shipment(self):
        """Kargo sorgulama işlemi"""
        shipment_id = self.search_id_entry.get()

        if not shipment_id:
            messagebox.showerror("Hata", "Lütfen gönderi ID girin!")
            return

        # Tüm kargolar içinde arama yap
        found = False
        for shipment in self.system.all_shipments:
            if shipment.shipment_id == shipment_id:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Gönderi ID: {shipment.shipment_id}\n")
                self.result_text.insert(tk.END, f"Gönderi Tarihi: {shipment.shipment_date}\n")
                self.result_text.insert(tk.END, f"Teslimat Durumu: {shipment.delivery_status.value}\n")
                self.result_text.insert(tk.END, f"Kargo Durumu: {shipment.cargo_status.value}\n")
                self.result_text.insert(tk.END, f"Teslimat Süresi: {shipment.delivery_time} gün\n")
                found = True
                break

        if not found:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Gönderi bulunamadı!")

    def calculate_city_delivery_time(self):
        """Şehre göre teslimat süresini hesaplar"""
        city_id = self.delivery_city_id.get()
        if not city_id:
            messagebox.showerror("Hata", "Şehir ID giriniz!")
            return

        time = self.system.calculate_delivery_time(city_id)
        self.delivery_text.delete(1.0, tk.END)

        if time is not None:
            self.delivery_text.insert(tk.END, f"Teslimat Süresi: {time} gün\n")
            self.delivery_text.insert(tk.END, "\nNot: Süre, şehrin ağaçtaki derinliğine göre hesaplanmıştır.")
        else:
            self.delivery_text.insert(tk.END, "Şehir bulunamadı!")

    def show_delivered_shipments(self):
        """Teslim edilmiş kargoları gösterir (Binary Search kullanılarak sıralanmış)"""
        self.list_text.delete(1.0, tk.END)
        delivered = [s for s in self.system.all_shipments
                     if s.delivery_status == DeliveryStatus.TESLIM_EDILDI]

        if delivered:
            self.list_text.insert(tk.END, "Teslim Edilmiş Kargolar (ID'ye göre sıralı):\n\n")
            # ID'ye göre sırala
            delivered.sort(key=lambda x: int(x.shipment_id))
            for shipment in delivered:
                self.list_text.insert(tk.END, f"Gönderi ID: {shipment.shipment_id}\n")
                self.list_text.insert(tk.END, f"Tarih: {shipment.shipment_date}\n")
                self.list_text.insert(tk.END, "-" * 40 + "\n")
        else:
            self.list_text.insert(tk.END, "Teslim edilmiş kargo bulunmamaktadır!")

    def show_undelivered_shipments(self):
        """Teslim edilmemiş kargoları teslimat süresine göre sıralı gösterir"""
        self.list_text.delete(1.0, tk.END)
        undelivered = self.system.get_undelivered_shipments_sorted()

        if undelivered:
            self.list_text.insert(tk.END, "Teslim Edilmemiş Kargolar (Teslimat süresine göre sıralı):\n\n")
            for shipment in undelivered:
                self.list_text.insert(tk.END, f"Gönderi ID: {shipment.shipment_id}\n")
                self.list_text.insert(tk.END, f"Teslimat Süresi: {shipment.delivery_time} gün\n")
                self.list_text.insert(tk.END, f"Durum: {shipment.cargo_status.value}\n")
                self.list_text.insert(tk.END, "-" * 40 + "\n")
        else:
            self.list_text.insert(tk.END, "Teslim edilmemiş kargo bulunmamaktadır!")
    def add_city(self):
        """Şehir ekleme işlemi"""
        parent_id = self.parent_city_entry.get()
        city_id = self.city_id_entry.get()
        city_name = self.city_name_entry.get()

        if not city_id or not city_name:
            messagebox.showerror("Hata", "Şehir ID ve adı zorunludur!")
            return

        if self.system.add_delivery_route(parent_id if parent_id else None, city_id, city_name):
            messagebox.showinfo("Başarılı", "Şehir başarıyla eklendi!")
            # Formu temizle
            self.parent_city_entry.delete(0, tk.END)
            self.city_id_entry.delete(0, tk.END)
            self.city_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Şehir eklenirken bir hata oluştu!")