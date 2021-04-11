cmake_minimum_required(VERSION 3.17)
project(cellphone C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_FLAGS "-Wall -Werror")

add_executable(cellphone main.c Phone.c Tower.c)