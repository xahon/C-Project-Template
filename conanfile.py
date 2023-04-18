import os
from conans import ConanFile


class Project(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package_multi"

    def requirements(self):
        self.requires("qt/6.4.2")

    def configure(self):
        self.options["qt"].shared = True

    def appendDotDll(self, lib):
        if self.settings.os == "Windows":
            return lib + ".dll"
        elif self.settings.os == "Linux":
            return lib + ".so"
        return lib + ".dylib"

    def imports(self):
        dest = os.getenv("CONAN_IMPORT_PATH", "bin")
        self.copy(self.appendDotDll("Qt6*"), dst=dest, src="bin")
        self.copy(self.appendDotDll("*"), dst=dest + "/platforms", src="res/archdatadir/plugins/platforms")
        self.copy(self.appendDotDll("*"), dst=dest + "/imageformats", src="res/archdatadir/plugins/imageformats")
        self.copy(self.appendDotDll("*"), dst=dest + "/iconengines", src="res/archdatadir/plugins/iconengines")
