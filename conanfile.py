# /usr/bin/python3
import os
from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.files import copy

class TraactPackage(ConanFile):
    python_requires = "traact_base/0.0.0@traact/latest"
    python_requires_extend = "traact_base.TraactPackageCmake"

    name = "test_apps"
    version = "0.0.0"
    description = ""
    url = ""
    license = "MIT"
    author = "Frieder Pankratz#"
    
    settings = "os", "compiler", "build_type", "arch"
    compiler = "cppstd"

    options = {
        "shared": [True, False],
        "with_tests": [True, False],
        "trace_logs_in_release": [True, False],
        "with_cuda": [True, False],
        "with_bodytracking": [True, False]
    }

    default_options = {
        "shared": True,
        "with_tests": True,
        "trace_logs_in_release": True,
        "with_cuda": True,
        "with_bodytracking": True,
        "opencv/*:with_jpeg": "libjpeg-turbo",
        "opencv/*:with_quirc": False,
        "libtiff/*:jpeg": "libjpeg-turbo"

    }

    exports_sources = "CMakeLists.txt", "src/*"

    def requirements(self):
        self.requires("traact_base/0.0.0@traact/latest")
        self.requires("traact_core/0.0.0@traact/latest")
        self.requires("traact_spatial/0.0.0@traact/latest")
        self.requires("traact_vision/0.0.0@traact/latest")
        self.requires("traact_gui/0.0.0@traact/latest")
        self.requires("traact_component_basic/0.0.0@traact/latest")
        self.requires("traact_component_kinect_azure/0.0.0@traact/latest")
        self.requires("traact_component_cereal/0.0.0@traact/latest")
        self.requires("traact_component_aruco/0.0.0@traact/latest")
        self.requires("traact_component_pcpd_shm/0.0.0@traact/latest")
        self.requires("traact_component_pointcloud/0.0.0@traact/latest")
        self.requires("traact_component_http/0.0.0@traact/latest")
        self.requires("yaml-cpp/0.7.0")

        self.requires("cpp-httplib/0.14.0", transitive_libs=True)
        self.requires("opencv/4.8.0@camposs/stable", override=True)
        self.requires("aruco/3.1.15@camposs/stable")
        self.requires("apriltag/3.1.4")

        self.requires("cereal/1.3.2", transitive_headers=True, transitive_libs=True)
        self.requires("cppfs/1.3.0@camposs/stable")
        self.requires("kinect-azure-sensor-sdk/1.4.1-r3@camposs/stable", run=True)
        self.requires("kinect-azure-bodytracking-sdk/1.1.0@vendor/stable", run=True)
        self.requires("pcpd_shm_client/0.0.2@artekmed/stable")
        self.requires("capnproto/0.10.3")
        self.requires("gtest/1.14.0", override=True)
        self.requires("open3d/0.17.0@camposs/stable", transitive_headers=True, transitive_libs=True)
        self.requires("approvaltests.cpp/10.12.2", transitive_headers=True, transitive_libs=True)

        self.requires("nlohmann_json/[>=3.11.2]", transitive_headers=True)
        self.requires("spdlog/1.11.0", transitive_headers=True, transitive_libs=True)
        #self.requires("fmt/10.0.0")
        self.requires("fmt/9.1.0", override=True)
        self.requires("rttr/0.9.7-dev@camposs/stable", transitive_headers=True, transitive_libs=True)
        self.requires("taskflow/3.4.0")
        self.requires("tclap/[>=1.2.4]")
        self.requires("re2/20230801")
        self.requires("cuda_dev_config/[>=2.0]@camposs/stable")
        self.requires("glfw/3.3.8")
        self.requires("glew/2.2.0")
        self.requires("imgui/cci.20230105+1.89.2.docking", override=True)
        self.requires("ghc-filesystem/1.5.8")
        self.requires("imguizmo/1.83")
        self.requires("implot/0.16")
        self.requires("stb/cci.20220909")
        self.requires("nodesoup/cci.20200905")
        self.requires("glm/0.9.9.8")
        self.requires("eigen/[>=3.4.0]", transitive_headers=True)
        self.requires("ceres-solver/2.1.0", transitive_headers=True, transitive_libs=True)
        self.requires("libwebp/1.3.1", override=True)

    def configure(self):
        self.options['traact_core'].shared = self.options.shared
        self.options['traact_facade'].shared = self.options.shared
        self.options['traact_spatial'].shared = self.options.shared
        self.options['traact_vision'].shared = self.options.shared

        self.options['pcpd_shm_client'].with_python = False
        self.options['pcpd_shm_client'].with_visualization = False
        self.options['pcpd_shm_client'].with_apps = False
        self.options['capnproto'].shared = True
        self.options['iceoryx/*'].with_introspection = True
        self.options['opencv'].shared = self.options.shared
        self.options['opencv'].with_cuda = self.options.with_cuda
        # self.options['opencv'].with_tbb = True
        if self.settings.os == "Linux":
            self.options['opencv/*'].with_gtk = True

    def _extend_generate(self):
        for dep in self.dependencies.values():
            if dep.ref.name == "imgui":
                copy(self, "imgui_impl_opengl3*", os.path.join(dep.package_folder, "res/bindings"), os.path.join(self.build_folder, "traact_gui/imgui_bindings"))
                copy(self, "imgui_impl_glfw*", os.path.join(dep.package_folder, "res/bindings"), os.path.join(self.build_folder, "traact_gui/imgui_bindings"))