import moderngl_window as mglw
import numpy as np
import glm
from math import sin

class Viewer(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "Viewer"
    window_size = (800, 600)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Enable the ModernGL context already created by the window
        self.ctx.enable(self.ctx.DEPTH_TEST)

        #Program containing basic vertex and fragment shaders (no lighting model yet)
        self.prog = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec3 in_vert;
                in vec3 in_color;
                uniform mat4 model;
                uniform mat4 view;
                uniform mat4 projection;
                out vec3 v_color;
                void main() {
                    v_color = in_color;
                    gl_Position = projection * view * model * vec4(in_vert, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                in vec3 v_color;
                out vec3 f_color;
                void main() {
                    f_color = v_color;
                }
            '''
        )

        #Vertices of a cube
        vertices = np.array([
            -0.5, -0.5, -0.5,  0.0,  0.0, 1.0,
             0.5, -0.5, -0.5,  0.0,  0.0, 1.0,
             0.5,  0.5, -0.5,  0.0,  0.0, 1.0,
             0.5,  0.5, -0.5,  0.0,  0.0, 1.0,
            -0.5,  0.5, -0.5,  0.0,  0.0, 1.0,
            -0.5, -0.5, -0.5,  0.0,  0.0, 1.0,

            -0.5, -0.5,  0.5,  0.0,  0.0, 1.0,
             0.5, -0.5,  0.5,  0.0,  0.0, 1.0,
             0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
             0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
            -0.5,  0.5,  0.5,  0.0,  0.0, 1.0,
            -0.5, -0.5,  0.5,  0.0,  0.0, 1.0,

            -0.5,  0.5,  0.5, 1.0,  0.0,  0.0,
            -0.5,  0.5, -0.5, 1.0,  0.0,  0.0,
            -0.5, -0.5, -0.5, 1.0,  0.0,  0.0,
            -0.5, -0.5, -0.5, 1.0,  0.0,  0.0,
            -0.5, -0.5,  0.5, 1.0,  0.0,  0.0,
            -0.5,  0.5,  0.5, 1.0,  0.0,  0.0,

             0.5,  0.5,  0.5,  1.0,  0.0,  0.0,
             0.5,  0.5, -0.5,  1.0,  0.0,  0.0,
             0.5, -0.5, -0.5,  1.0,  0.0,  0.0,
             0.5, -0.5, -0.5,  1.0,  0.0,  0.0,
             0.5, -0.5,  0.5,  1.0,  0.0,  0.0,
             0.5,  0.5,  0.5,  1.0,  0.0,  0.0,

            -0.5, -0.5, -0.5,  0.0, 1.0,  0.0,
             0.5, -0.5, -0.5,  0.0, 1.0,  0.0,
             0.5, -0.5,  0.5,  0.0, 1.0,  0.0,
             0.5, -0.5,  0.5,  0.0, 1.0,  0.0,
            -0.5, -0.5,  0.5,  0.0, 1.0,  0.0,
            -0.5, -0.5, -0.5,  0.0, 1.0,  0.0,

            -0.5,  0.5, -0.5,  0.0,  1.0,  0.0,
             0.5,  0.5, -0.5,  0.0,  1.0,  0.0,
             0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
             0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
            -0.5,  0.5,  0.5,  0.0,  1.0,  0.0,
            -0.5,  0.5, -0.5,  0.0,  1.0,  0.0
        ], dtype='f4')

        #Define the vertex buffer
        self.vbo = self.ctx.buffer(vertices)

        #Create a vertex array object linking the program, vbo and shaders attributes
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'in_vert', 'in_color')

        # Fixed matrices (model matric varies with time)
        view = glm.lookAt(glm.vec3(0, 0, 3), glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))
        projection = glm.perspective(glm.radians(45.0), self.aspect_ratio, 0.1, 100.0)

        # We pass the matrices as uniforms to the shaders
        self.prog['view'].write(view.to_bytes())
        self.prog['projection'].write(projection.to_bytes())

    def on_render(self, time_sec, frame_time):
        self.ctx.clear(0.0, 0.0, 0.0, 1.0, depth=1.0)

        model = glm.mat4(1.0)
        model = glm.rotate(model, time_sec, glm.vec3(1, 1, 0))
        self.prog['model'].write(model.to_bytes())

        self.vao.render(self.ctx.TRIANGLES)

if __name__ == '__main__':
    # Launch the main window
    mglw.run_window_config(Viewer)