from conans import ConanFile, CMake, CMakeToolchain


class TestPackageV1Conan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "VirtualBuildEnv"
    test_type = "explicit"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["CMAKE_TRY_COMPILE_TARGET_TYPE"] = "STATIC_LIBRARY"
        tc.blocks["arch_flags"].values = {
            "arch_flag": "-mthumb -mfloat-abi=hard -march=armv7e-m+fp -mtune=cortex-m4"
        }
        tc.variables[
            "CMAKE_EXE_LINKER_FLAGS_INIT"
        ] = "${{CMAKE_EXE_LINKER_FLAGS_INIT}} -specs=nano.specs -specs=nosys.specs"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        # Executables generated by this toolchain will never work on a host
        # machine and thus can never be executed.
        pass
