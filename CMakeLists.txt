cmake_minimum_required(VERSION 3.25)
project(scikit_build_core_minimal_shared_library_example C)

set(CMAKE_C_STANDARD 11)

add_library(library_example SHARED scikit_build_core_minimal_shared_library_example/library.c)

set(library_directory "${SKBUILD_PLATLIB_DIR}")

install(TARGETS library_example DESTINATION ${library_directory})
