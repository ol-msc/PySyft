from .torch import create_torch_ast
from .numpy import create_numpy_ast
from ..ast.globals import Globals

# now we need to load the relevant frameworks onto the node
def create_lib_ast():

    torch_ast = create_torch_ast()
    numpy_ast = create_numpy_ast()

    lib_ast = Globals()
    lib_ast.add_attr(attr_name="torch", attr=torch_ast.attrs["torch"])
    lib_ast.add_attr(attr_name="numpy", attr=numpy_ast.attrs["numpy"])

    return lib_ast


lib_ast = create_lib_ast()
lib_ast.copy = create_lib_ast
