##
# This script runs one or more TASKING compilers and gathers information
#  for CLion's Custom Compiler definitions file, see
#  https://blog.jetbrains.com/clion/2021/10/clion-2021-3-eap-custom-compiler/
#  https://www.jetbrains.com/help/clion/custom-compilers.html
#
#  The script is tested against TASKING VX-toolset v6.3r1 for Infineon TriCore
#    `output_filename`, `tasking_install_folder`, `tasking_platform_suffix`, `c_additional_compile_switches`, and
#    `cpp_additional_compile_switches` variables can be adjusted to fit another toolset variant
#
# # License
#
# Apache 2.0, https://github.com/JetBrains/clion-custom-defined-compiler-examples/blob/master/LICENSE
#
# # Disclaimer
#
# All the repository content is provided on an "AS IS" basis, without warranties or conditions of any kind.
#
# Please note that JetBrains does not provide the described compilers or required licenses. The use of third-party
# compilers in CLion is subject to the licensing policies of their vendors, while config files are open source.
# All trademarks, logos and brand names are the property of their respective owners. All company, product and service
# names used in this repository are for identification purposes only. Use of these names,trademarks and brands does not
# imply endorsement.
#
##
import os, subprocess, tempfile, re

output_filename = "custom-compiler-tasking-generated.yaml"
tasking_install_folder = "C:\\Program Files\\TASKING\\TriCore v6.3r1"
tasking_platform_suffix = ["51", "arm", "mcs", "tc"]  # 8051, ARM, MCS, TriCore

c_additional_compile_switches = "--iso=99"  # example, may be empty

cpp_additional_compile_switches = "--c++=11"  # example, may be empty

def extract_defines(compiler_bin, src_name):
    result = subprocess.run([compiler_bin, "-El", src_name], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    if result.returncode != 0:
        return None
    all_defines = result.stdout.decode("ascii").splitlines()
    filtered_defines = filter(lambda s: s.split()[1] not in ['__FILE__', '__LINE__', '__DATE__', '__TIME__' ],
                              all_defines)
    str_defines = '\n'.join(filtered_defines).replace("\"","\\\"")
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
                print(f'  - description: "C, {version}"',
                      f'    match-compiler-exe: "(.*/)?cc{suffix}(\\\\.exe)?"',
                      f'    match-sources: ".*\\\\.c"',
                      f'    match-language: C',
                      f'    code-insight-target-name: arm',
                      f'    include-dirs: ["${{compiler-exe-dir}}/../include"]',
                      f'    defines-text: "',
                      c_definitions,
                      '"',
                      file=yaml_file, sep="\n")
            cpp_definitions = extract_defines(compiler_bin, "__empty.cpp")
            if cpp_definitions is None:
                print("Skipping yaml for C++")
            else:
                print("Writing yaml for C++")
                print(f'  - description: "C++, {version}"',
                      f'    match-compiler-exe: "(.*/)?cc{suffix}(\\\\.exe)?"',
                      f'    match-sources: ".*\\\\.cpp"',
                      f'    match-language: CPP',
                      f'    code-insight-target-name: arm',
                      f'    include-dirs: ["${{compiler-exe-dir}}/../include", "${{compiler-exe-dir}}/../include.cxx"]',
                      f'    defines-text: "',
                      cpp_definitions,
                      '"',
                      file=yaml_file, sep="\n")
    finally:
        os.unlink("__empty.c")
        os.unlink("__empty.cpp")
