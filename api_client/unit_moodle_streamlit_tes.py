import requests
import unittest
from unittest.mock import patch, MagicMock
import cliente_all_streamlit_login  

class TestMoodleAPI(unittest.TestCase):

    @patch('cliente_all_streamlit_login.requests.get')
    def test_obtener_cursos(self, mock_get):
        # Simula una respuesta JSON de la API de Moodle
        mock_response = [{'id': 1, 'fullname': 'Curso de prueba', 'shortname': 'CP1'}]
        mock_get.return_value = MagicMock(json=lambda: mock_response)

        # Llama a la función
        response = cliente_all_streamlit_login.obtener_cursos()

        # Verifica que la respuesta sea la esperada
        self.assertEqual(response, mock_response)

    #Prueba real del servicio obtener cursos
    def test_obtener_cursos_real(self):
        # Llama a la función sin parchearla para obtener la respuesta real
        response = cliente_all_streamlit_login.obtener_cursos()

        # Respuesta esperada simulada
        mock_response = [
          {'id': 2, 'fullname': 'moodle_test', 'shortname': 'Test'},
        ]

        # Verifica que la respuesta sea exactamente la esperada
        #self.assertEqual(response, mock_response)

        # Verifica si los parámetros del mock_response están presentes en algún objeto de la respuesta del servicio
        for curso in response:
            if all(curso.get(key) == value for key, value in mock_response[0].items()):
                # Si todos los parámetros del mock_response están presentes en el objeto de la respuesta del servicio, la prueba pasa
                return
        # Si no se encuentra ningún objeto que coincida con el mock_response, la prueba falla
        self.fail("No se encontró ningún objeto que coincida con el mock_response")

    @patch('cliente_all_streamlit_login.requests.get')
    def test_mostrar_info_curso(self, mock_get):
        # Simula una respuesta JSON de la API de Moodle para un curso específico
        mock_response = [{'id': 1, 'fullname': 'Curso de prueba', 'shortname': 'CP1'}]
        mock_get.return_value = MagicMock(json=lambda: mock_response)

        # Llama a la función con el ID del curso
        response = cliente_all_streamlit_login.mostrar_info_curso(1)

        # Verifica que la respuesta sea la esperada
        self.assertEqual(response, mock_response)

    @patch('cliente_all_streamlit_login.requests.post')
    def test_crear_curso(self, mock_post):
        # Simula una respuesta JSON de la API de Moodle tras crear un curso
        mock_response = {'id': 1, 'shortname': 'CP1', 'fullname': 'Curso de prueba'}
        mock_post.return_value = MagicMock(json=lambda: mock_response)

        # Llama a la función con detalles del curso a crear
        response = cliente_all_streamlit_login.crear_curso('CP1', 'Curso de prueba', 1)

        # Verifica que la respuesta sea la esperada
        self.assertEqual(response, mock_response)

    # Continúa con las pruebas para eliminar_curso y modificar_curso...
    @patch('cliente_all_streamlit_login.requests.post')
    def test_eliminar_curso(self, mock_post):
        # Simula una respuesta de éxito al eliminar el curso
        mock_post.return_value.text = "Curso eliminado correctamente."

        # Llama a la función para eliminar un curso y verifica la respuesta
        response = cliente_all_streamlit_login.eliminar_curso(1)
        self.assertEqual(response, "Curso eliminado correctamente.")

        # Simula una respuesta de error al eliminar el curso
        mock_post.return_value.text = "Error al eliminar el curso."

        # Llama a la función para eliminar un curso y verifica la respuesta de error
        response = cliente_all_streamlit_login.eliminar_curso(2)
        self.assertEqual(response, "Error al eliminar el curso.")
    
    @patch('cliente_all_streamlit_login.requests.post')
    def test_modificar_curso(self, mock_post):
        # Simula una respuesta de éxito al modificar el curso
        mock_post.return_value.json.return_value = {'id': 1, 'shortname': 'CP1', 'fullname': 'Curso modificado'}

        # Llama a la función para modificar un curso y verifica la respuesta
        response = cliente_all_streamlit_login.modificar_curso(1, shortname='CP1', fullname='Curso modificado', categoryid=1)
        self.assertEqual(response, {'id': 1, 'shortname': 'CP1', 'fullname': 'Curso modificado'})

        # Simula una respuesta de error al modificar el curso
        mock_post.return_value.json.return_value = {'exception': 'Error al modificar el curso.'}

        # Llama a la función para modificar un curso y verifica la respuesta de error
        response = cliente_all_streamlit_login.modificar_curso(2, shortname='CP1', fullname='Curso modificado', categoryid=1)
        self.assertEqual(response, {'exception': 'Error al modificar el curso.'})

        
    
if __name__ == '__main__':
    unittest.main()
