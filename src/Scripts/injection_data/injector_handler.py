from Scripts.injection_data.class_injector import Injector


def inject_data_to_db(patients: list, consulations: list, histories: list) -> bool:
      injector = Injector(db_path="database/consultorio_reynoso.db")
      injector.create_tables()
      success = injector.inject_data(patients, consulations, histories)
      
      # Retornar los contadores correctos
      patients_injected = injector.patient_inject_count
      consulations_injected = injector.consulation_inject_count  # ✅ Corregido
      histories_injected = injector.history_inject_count
      
      print(f"📊 Inyección completada - Pacientes: {patients_injected}, Consultas: {consulations_injected}, Historias: {histories_injected}")
      
      return {
          'success': success,
          'injected_counts': {
              'patients': patients_injected,
              'consulations': consulations_injected,
              'histories': histories_injected
          }
      }