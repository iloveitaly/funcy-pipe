# stub_gen.py

import inspect
import subprocess
from typing import Callable


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


def modify_signature_for_pipe(signature, pipe_type):
    params = list(signature.parameters.values())

    # Remove the first or second parameter based on the pipe type
    if pipe_type == "PipeFirst" and params:
        del params[0]
    elif pipe_type == "PipeSecond" and len(params) > 1:
        del params[1]

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


def discover_extensions():
    import funcy_pipe.funcy_extensions as extensions

    return [
        name
        for name, obj in inspect.getmembers(extensions)
        if inspect.isfunction(obj) and not name.startswith("_")
    ]


def generate_pyi(module_name: str):
    # Use dict.fromkeys to deduplicate while preserving order
    import funcy_pipe

    all_objects = list(dict.fromkeys(funcy_pipe.__all__))

    extension_names = discover_extensions()
    import funcy_pipe.funcy_extensions as extensions

    # Combine and deduplicate
    all_objects = list(dict.fromkeys(all_objects + extension_names))

    body_lines = []
    use_any = False

    for obj_name in all_objects:
        # Check main module first, then extensions
        obj = getattr(funcy_pipe, obj_name, None)
        if obj is None:
            obj = getattr(extensions, obj_name, None)

        if not obj:
            print(f"Skipping {obj_name}, could not find...")
            continue

        if callable(obj):
            cls = obj.__class__.__name__

            # Modify signature based on class type
            if cls in ["PipeFirst", "PipeSecond"]:
                wrapped_func = getattr(obj, "function", obj)
                signature = generate_signature(wrapped_func)
                modified_signature = modify_signature_for_pipe(signature, cls)
            else:
                signature = generate_signature(obj)
                modified_signature = modify_signature_for_pipe(signature, cls)

            body_lines.append(f"def {obj_name}{modified_signature}: ...\n")
        else:
            use_any = True
            body_lines.append(f"{obj_name}: Any\n")

    header_lines = ["from typing import Callable\n"]
    if use_any:
        header_lines[0] = "from typing import Any, Callable\n"

    return "".join(header_lines) + "\n" + "".join(body_lines)


def main():
    module_name = "funcy_pipe"
    pyi_path = f"{module_name}/__init__.pyi"
    pyi_content = generate_pyi(module_name)
    with open(pyi_path, "w") as f:
        f.write(pyi_content)

    # format the generated file
    subprocess.run(["uv", "run", "ruff", "format", pyi_path], check=True)


if __name__ == "__main__":
    main()