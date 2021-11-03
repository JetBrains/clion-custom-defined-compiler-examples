output_filename = "custom-compiler-tasking-generated.yaml"
tasking_install_folder = "C:\\Program Files\\TASKING\\TriCore v6.3r1"
tasking_platform_suffix = ["51", "arm", "mcs", "pcp", "tc"]  # TriCore, ARM

c_additional_compile_switches = "--iso=99"  # example, may be empty

cpp_additional_compile_switches = "--c++=11"  # example, may be empty

import os, subprocess, tempfile, re


def extract_defines(compiler_bin, src_name):
    result = subprocess.run([compiler_bin, "-El", src_name], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    if result.returncode != 0:
        return None
    all_defines = result.stdout.splitlines()
    filtered_defines = filter(lambda s: s.split()[1] not in [b'__FILE__', b'__LINE__', b'__DATE__', b'__TIME__', ],
                              all_defines)
    str_defines = b'\n'.join(filtered_defines).decode("ascii")
    return str_defines


with open(output_filename, "wt") as yaml_file:
    open("__empty.c", "wt")
    open("__empty.cpp", "wt")
    try:
        print("compilers:", file=yaml_file)
        for suffix in tasking_platform_suffix:
            compiler_bin = tasking_install_folder + os.path.sep + "c" + suffix + os.path.sep + "bin" + os.path.sep + "cc" + suffix
            version = \
                subprocess.run([compiler_bin, "-V"], stderr=subprocess.STDOUT,
                               stdout=subprocess.PIPE).stdout.splitlines()[0].decode("ascii")
            print(f"Compiler: {version}")
            c_definitions = extract_defines(compiler_bin, "__empty.c")
            if c_definitions is None:
                print("Skipping yaml for C")
            else:
                print("Writing yaml for C")
                print(
                    f"""
  - description: "C, {version}"
    match-compiler-exe: "(.*/)?cc{suffix}(\\\\.exe)?"
    match-sources: ".*\\\\.c"
    match-language: C
    code-insight-target-name: arm
    include-dirs: ["${{compiler-exe-dir}}/../include"]
    defines-text: "
{c_definitions}
"  
""", file=yaml_file)
            cpp_definitions = extract_defines(compiler_bin, "__empty.cpp")
            if cpp_definitions is None:
                print("Skipping yaml for C++")
            else:
                print("Writing yaml for C++")
                print(
                    f"""
  - description: "CPP, {version}"
    match-compiler-exe: "(.*/)?cc{suffix}(\\\\.exe)?"
    match-sources: ".*\\\\.cpp"
    match-language: CPP
    code-insight-target-name: arm
    include-dirs: ["${{compiler-exe-dir}}/../include", "${{compiler-exe-dir}}/../include.cxx"]
    defines-text: "
{cpp_definitions}
"  
""", file=yaml_file)
    finally:
        os.unlink("__empty.c")
        os.unlink("__empty.cpp")
