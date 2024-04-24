import cliente_all_streamlit_login as cli
import pytest

@pytest.mark.parametrize(
  'mock_response',
  [
      {'id': 1, 'fullname': 'moodle_test', 'shortname': 'Test'},
      {'id': 3, 'fullname': 'Pruebas de Software', 'shortname': 'Testing'}
  ]
)

def test_obtener_cursos(mock_response):
  # Llama a la función para obtener los cursos
  response = cli.obtener_cursos()

  # Verifica si los parámetros del mock_response están presentes en algún objeto de la respuesta del servicio
  for curso in response:
    if all(curso.get(key) == value for key, value in mock_response.items()):
      # Si todos los parámetros del mock_response coiniden con los del servicio pasa la prueba
      return
  # Si no se encuentra ningún objeto que coincida con el mock_response, la prueba falla
  pytest.fail("No se encontró ningún objeto que coincida con el mock_response")
