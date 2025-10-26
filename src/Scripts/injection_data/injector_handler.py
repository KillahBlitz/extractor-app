from Scripts.injection_data.class_injector import Injector


def inject_data_to_db(patients: list, consulations: list, histories: list) -> bool:
    injector = Injector(db_path="database/consultorio_reynoso.db")
    injector.create_tables()
    injector.inject_data(patients, consulations, histories)
    print(f"✅ Inyección completada: {injector.patient_inject_count} pacientes, "
          f"{injector.consulation_inject_count} consultas, "
          f"{injector.history_inject_count} historias.")
    return True