cmake_minimum_required(VERSION 3.16)

if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
    set(CMAKE_CUDA_ARCHITECTURES 75)
endif()

project(TRAACT_ALL)



add_subdirectory(traact_core)
add_subdirectory(traact_spatial)
add_subdirectory(traact_vision)
add_subdirectory(traact_pointcloud)
add_subdirectory(traact_gui)
add_subdirectory(traact_pcpd)
add_subdirectory(traact_component_aruco)
add_subdirectory(traact_component_basic)
add_subdirectory(traact_component_cereal)
add_subdirectory(traact_component_http)
add_subdirectory(traact_component_kinect_azure)
add_subdirectory(traact_component_zenoh)
add_subdirectory(traact_server)
add_subdirectory(test_apps)

