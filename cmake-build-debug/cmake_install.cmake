<<<<<<< HEAD
<<<<<<< HEAD
# Install script for directory: /Users/imseung-u/Documents/GitHub/Group-16

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
=======
=======
>>>>>>> refs/remotes/origin/main
# Install script for directory: C:/Users/User/CLionProjects/Group-16

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/Group_16")
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> refs/remotes/origin/main
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
<<<<<<< HEAD
<<<<<<< HEAD
  set(CMAKE_OBJDUMP "/Library/Developer/CommandLineTools/usr/bin/objdump")
=======
  set(CMAKE_OBJDUMP "C:/Program Files/JetBrains/CLion 2024.2.3/bin/mingw/bin/objdump.exe")
>>>>>>> refs/remotes/origin/main
=======
  set(CMAKE_OBJDUMP "C:/Program Files/JetBrains/CLion 2024.2.3/bin/mingw/bin/objdump.exe")
>>>>>>> refs/remotes/origin/main
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
<<<<<<< HEAD
<<<<<<< HEAD
file(WRITE "/Users/imseung-u/Documents/GitHub/Group-16/cmake-build-debug/${CMAKE_INSTALL_MANIFEST}"
=======
file(WRITE "C:/Users/User/CLionProjects/Group-16/cmake-build-debug/${CMAKE_INSTALL_MANIFEST}"
>>>>>>> refs/remotes/origin/main
=======
file(WRITE "C:/Users/User/CLionProjects/Group-16/cmake-build-debug/${CMAKE_INSTALL_MANIFEST}"
>>>>>>> refs/remotes/origin/main
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
