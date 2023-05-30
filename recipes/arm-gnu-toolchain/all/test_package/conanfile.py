from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv"

    def build_requirements(self):
        self.tool_requires(self.tested_reference_str)

    def layout(self):
        cmake_layout(self)

    def build(self):
        if str(self.settings.compiler) == "gcc":
            cmake = CMake(self)
            cmake.configure()
            cmake.build()

    def test(self):
        # Executables generated by this toolchain will never work on a host
        # machine and thus can never be executed.
        pass
