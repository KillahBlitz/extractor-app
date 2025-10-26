import sqlite3
import os

class Injector:  # ✅ Cambiado de 'Inyector' a 'Injector'
    patient_inject_count = 0
    consulation_inject_count = 0
    history_inject_count = 0

    def __init__(self):
        self.data_dir = "data"
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        self.db_path = os.path.join(self.data_dir, "database.db")

        self._create_tables()

    def _create_tables(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            age INTEGER DEFAULT 0,
                            type_patient TEXT DEFAULT 'N/A',
                            weight REAL NOT NULL,
                            height REAL NOT NULL,
                            total_consulation INTEGER DEFAULT 0
                          )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS consulations (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            date DATE NOT NULL,
                            weight REAL NOT NULL,
                            height REAL NOT NULL,
                            observations TEXT NOT NULL,
                            medications TEXT DEFAULT ''
                          )''')
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS histories (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            history TEXT NOT NULL,
                            type_history TEXT DEFAULT 'N/A'
                          )''')
            
            conn.commit()
            conn.close()
            print(f"✅ Tablas creadas correctamente en: {self.db_path}")
            
        except Exception as e:
            print(f"❌ Error al crear las tablas: {e}")

    def inject_data(self, patients: list, consulations: list, histories: list):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            for patient in patients:
                cursor.execute('''INSERT INTO patients (name, age, type_patient, weight, height, total_consulation)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                               (patient.name, patient.age, patient.type_patient, patient.weight,
                                patient.height, patient.total_consulation))
                self.patient_inject_count += 1

            for consulation in consulations:
                cursor.execute('''INSERT INTO consulations (name, date, weight, height, observations, medications)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                               (consulation.name, consulation.date, consulation.weight,
                                consulation.height, consulation.observations, consulation.medications))
                self.consulation_inject_count += 1

            for history in histories:
                cursor.execute('''INSERT INTO histories (name, history, type_history)
                                  VALUES (?, ?, ?)''',
                               (history.name, history.history, history.type_history))
                self.history_inject_count += 1
            
            conn.commit()
            conn.close()

            print(f"✅ Datos guardados en: {self.db_path}")
            print(f"📊 Pacientes: {self.patient_inject_count}, Consultas: {self.consulation_inject_count}, Historias: {self.history_inject_count}")
            return True
            
        except Exception as e:
            print("❌ Error al inyectar los datos en la base de datos:", e)
            if 'conn' in locals():
                conn.close()
            return False