from OpenGL.GL import *
from glew_wish import *
import glfw 
import random


def main():
    #inicia glfw 
    if not glfw.init():
        return
    #crea ventana independientemente del SO que usemos
    window = glfw.create_window(800, 600, "my window", None, None)
    #configuramos OPEGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    #VALIDAMOS QUE SE CREE LA VENTANA
    if not window:
        glfw.terminate()
        return
    #ESTABLECEMOS EL CONTEXTO, O SEA CREAMOS LA VENTANA PERO AUN NO SE MUESTRA
    glfw.make_context_current(window)

    #aCTIVAMOS LA VALIDACION DE FUNCIONES MODERNAS DE OPENLGL

    glewExperimental = True 

    #inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #obtenemos versiones de OPENGL Y SHADERS
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):

        color1= random.random()
        color2= random.random()
        color3= random.random()

        #establecer region de dibujo
        glViewport(0,0,800,600) #window size
        #color de borrado
        glClearColor(color1,color2,color3,1) #colores rgb
        #borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #aqui va el dibujo

        #preguntar si hubo entradas de perifericos
        #(teclado, mouse, gamepad, etc)
        glfw.poll_events()
        #intercambia los buffers
        glfw.swap_buffers(window)

    #se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #termina los procesos que inicio glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()













