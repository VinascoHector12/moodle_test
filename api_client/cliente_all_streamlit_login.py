import requests
import streamlit as st
import json  # Importación para manejar la codificación de los cursos al modificar

# Configuración inicial
MOODLE_URL = 'http://localhost:8080/webservice/rest/server.php'
TOKEN = '55c8aa568b617dbe947d400b004bd67c'
FORMATO = 'json'

def obtener_cursos():
    """Obtiene y muestra la lista de cursos desde la API de Moodle."""
    parametros = {
        'wstoken': TOKEN,
        'wsfunction': 'core_course_get_courses',
        'moodlewsrestformat': FORMATO,
    }
    respuesta = requests.get(MOODLE_URL, params=parametros)
    cursos = respuesta.json()
    return cursos

def mostrar_info_curso(curso_id):
    """Obtiene y muestra la información de un curso específico por ID."""
    parametros = {
        'wstoken': TOKEN,
        'wsfunction': 'core_course_get_courses',
        'moodlewsrestformat': FORMATO,
        'options[ids][0]': curso_id,
    }
    respuesta = requests.get(MOODLE_URL, params=parametros)
    curso_info = respuesta.json()
    return curso_info

def crear_curso(shortname, fullname, categoryid):
    """Crea un curso en Moodle."""
    parametros = {
        'wstoken': TOKEN,
        'wsfunction': 'core_course_create_courses',
        'moodlewsrestformat': FORMATO,
        'courses[0][shortname]': shortname,
        'courses[0][fullname]': fullname,
        'courses[0][categoryid]': categoryid,
    }
    respuesta = requests.post(MOODLE_URL, params=parametros)
    return respuesta.json()

def eliminar_curso(courseid):
    """Elimina un curso en Moodle."""
    parametros = {
        'wstoken': TOKEN,
        'wsfunction': 'core_course_delete_courses',
        'moodlewsrestformat': FORMATO,
        'courseids[0]': courseid,
    }
    respuesta = requests.post(MOODLE_URL, params=parametros)
    return respuesta.text  # Moodle no devuelve un JSON al eliminar cursos

def modificar_curso(courseid, shortname=None, fullname=None, categoryid=None):
    """Modifica un curso en Moodle."""
    curso = {
        'id': courseid,
        'shortname': shortname,
        'fullname': fullname,
        'categoryid': categoryid,
    }
    parametros = {
        'wstoken': TOKEN,
        'wsfunction': 'core_course_update_courses',
        'moodlewsrestformat': FORMATO,
        'courses[0][id]': curso['id'],
        'courses[0][shortname]': curso['shortname'],
        'courses[0][fullname]': curso['fullname'],
        'courses[0][categoryid]': curso['categoryid'],
    }
    respuesta = requests.post(MOODLE_URL, params=parametros)
    return respuesta.json()

# Implementación de Streamlit UI
st.title("Cliente Moodle")

# Agregamos una simple verificación de usuario
usuario = st.sidebar.text_input("Nombre de usuario")
contrasena = st.sidebar.text_input("Contraseña", type="password")

# Un diccionario simple para la demostración, reemplazar con tu lógica de autenticación
usuarios_validos = {
    "admin": "adminpass",
    # Agrega más usuarios aquí
}

if usuario in usuarios_validos and usuarios_validos[usuario] == contrasena:
    accion = st.sidebar.selectbox(
        "¿Qué deseas hacer?",
        ["Listar cursos", "Obtener información de un curso por ID", "Crear un nuevo curso", "Eliminar un curso", "Modificar un curso"]
    )

    if accion == "Listar cursos":
        cursos = obtener_cursos()
        for curso in cursos:
            st.text(f"ID: {curso['id']}, Nombre: {curso['fullname']}, Nombre Corto: {curso['shortname']}")

    elif accion == "Obtener información de un curso por ID":
        curso_id = st.text_input("Ingresa el ID del curso:", "")
        if curso_id:
            curso_info = mostrar_info_curso(curso_id)
            if curso_info:
                for curso in curso_info:
                    st.text(f"ID: {curso['id']}, Nombre: {curso['fullname']}, Nombre Corto: {curso['shortname']}")
            else:
                st.error("No se encontró información para el curso con el ID proporcionado.")
                
    elif accion == "Crear un nuevo curso":
        st.subheader("Crear un nuevo curso")
        
        with st.form(key='curso_form'):
            shortname = st.text_input("Nombre corto del curso", "")
            fullname = st.text_input("Nombre completo del curso", "")
            categoryid = st.text_input("ID de la categoría del curso", "")
            submit_button = st.form_submit_button(label='Crear curso')
            
            if submit_button:
                try:
                    categoryid_int = int(categoryid)
                    curso_creado = crear_curso(shortname, fullname, categoryid_int)
                    if curso_creado:
                        st.success(f"Curso creado con éxito: {curso_creado}")
                    else:
                        st.error("No se pudo crear el curso.")
                except ValueError:
                    st.error("El ID de la categoría debe ser un número entero.")

    elif accion == "Eliminar un curso":
        st.subheader("Eliminar un curso existente")
        curso_id_eliminacion = st.text_input("ID del curso a eliminar:", "")
        if st.button("Eliminar curso"):
            resultado = eliminar_curso(curso_id_eliminacion)
            if "exception" not in resultado:
                st.success("Curso eliminado con éxito.")
            else:
                st.error(f"No se pudo eliminar el curso: {resultado}")

    elif accion == "Modificar un curso":
        st.subheader("Modificar un curso existente")
        curso_id_modificacion = st.text_input("ID del curso a modificar:", "")
        shortname_mod = st.text_input("Nuevo nombre corto del curso (opcional):", "")
        fullname_mod = st.text_input("Nuevo nombre completo del curso (opcional):", "")
        categoryid_mod = st.text_input("Nuevo ID de la categoría del curso (opcional):", "")

        if st.button("Modificar curso"):
            resultado = modificar_curso(
                curso_id_modificacion,
                shortname=shortname_mod if shortname_mod else None,
                fullname=fullname_mod if fullname_mod else None,
                categoryid=int(categoryid_mod) if categoryid_mod else None,
            )
            if "exception" not in resultado:
                st.success("Curso modificado con éxito.")
            else:
                st.error(f"No se pudo modificar el curso: {resultado}")
else:
    st.sidebar.warning("Por favor, ingresa credenciales válidas.")
