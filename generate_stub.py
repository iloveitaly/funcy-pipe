# import inspect
# import funcy_pipe


# def generate_stubs(module):
#     for name, obj in inspect.getmembers(module):
#         if inspect.isfunction(obj):
#             # This will be more complex for dynamically wrapped functions.
#             # You might only get '(*args, **kwargs)' for these, unfortunately.
#             print(f"def {name}{inspect.signature(obj)}: ...")


# breakpoint()
# generate_stubs(funcy_pipe)

# stub_gen.py

import inspect
from typing import Any, Callable, get_type_hints

import typing as t


def get_generic_signature() -> inspect.Signature:
    return inspect.signature(lambda *args, **kwargs: ...)


def generate_signature(obj) -> inspect.Signature:
    try:
        return inspect.signature(obj)
    except ValueError:  # No signature could be extracted
        return get_generic_signature()


def is_literal_default(value):
    return isinstance(value, (str, int, float, bool, type(None)))


def get_default(param: inspect.Parameter):
    if is_literal_default(param.default):
        return param.default

    return inspect.Parameter.empty


def guess_type(param):
    if param.name in ["f", "pred", "func"]:
        return Callable
    elif param.name in ["regex"]:
        return str
    elif param.name in ["n"]:
        return int
    else:
        return param.annotation


stop_it = False


def modify_signature_for_pipe(signature, pipe_type):
    params = list(signature.parameters.values())

    # Remove the first or second parameter based on the pipe type
    if pipe_type == "PipeFirst" and params:
        del params[0]
    elif pipe_type == "PipeSecond" and len(params) > 1:
        del params[1]
    else:
        print(f"Skipping modifying {signature} for {pipe_type}...")

    # Reconstruct the signature without the removed parameter
    new_params = [
        inspect.Parameter(
            name=param.name,
            kind=param.kind,
            default=get_default(param),
            annotation=guess_type(param),
        )
        for param in params
    ]

    # since we don't support all default params, we need to remove all defaults if one cannot be set
    # *** ValueError: non-default argument follows default argument
    has_default = False

    for i, param in enumerate(new_params):
        if param.default != inspect.Parameter.empty:
            if i == 0:
                has_default = True
        else:
            has_default = False

        if i > 0 and not has_default:
            new_params[i] = param.replace(default=inspect.Parameter.empty)

    return str(inspect.Signature(parameters=new_params))


def generate_pyi(module_name: str):
    lines = ["from typing import Any, Callable\n"]

    all_objects = globals()[module_name].__all__

    for obj_name in all_objects:
        obj = getattr(globals()[module_name], obj_name)

        if not obj:
            print(f"Skipping {obj_name}, could not find...")
            continue

        if callable(obj):
            cls = obj.__class__.__name__

            # Modify signature based on class type
            if cls in ["PipeFirst", "PipeSecond"]:
                signature = generate_signature(obj.function)
                modified_signature = modify_signature_for_pipe(signature, cls)
            else:
                print(f"Skipping {obj_name}, not a PipeFirst or PipeSecond...")
                signature = generate_signature(obj)
                modified_signature = modify_signature_for_pipe(signature, cls)

            lines.append(f"def {obj_name}{modified_signature}: ...\n")
        else:
            lines.append(f"{obj_name}: Any\n")  # Handle non-callable objects

    return "\n".join(lines)


# TODO pull from argv
import_call = "import funcy_pipe; import funcy_pipe.funcy_extensions; funcy_pipe.funcy_extensions.patch()"
exec(import_call)
module_name = "funcy_pipe"

pyi_content = generate_pyi(module_name)
with open(f"{module_name}/__init__.pyi", "w") as f:
    f.write(pyi_content)
