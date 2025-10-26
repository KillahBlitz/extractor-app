from Scripts.injection_data.class_injector import Injector


def inject_data_to_db(patients: list, consulations: list, histories: list) -> bool:
      injector = Injector(db_path="database/consultorio_reynoso.db")
      injector.create_tables()
      injector.inject_data(patients, consulations, histories)
      patients_injected = injector.patient_inject_count
      consulations_injected = injector.patient_inject_count
      histories_injected = injector.history_inject_count
      return patients_injected, consulations_injected, histories_injected