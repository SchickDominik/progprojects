# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /mnt/data/Software/clion-2020.2/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /mnt/data/Software/clion-2020.2/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/helloworld.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/helloworld.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/helloworld.dir/flags.make

CMakeFiles/helloworld.dir/helloworld.cpp.o: CMakeFiles/helloworld.dir/flags.make
CMakeFiles/helloworld.dir/helloworld.cpp.o: ../helloworld.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/helloworld.dir/helloworld.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/helloworld.dir/helloworld.cpp.o -c "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/helloworld.cpp"

CMakeFiles/helloworld.dir/helloworld.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/helloworld.dir/helloworld.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/helloworld.cpp" > CMakeFiles/helloworld.dir/helloworld.cpp.i

CMakeFiles/helloworld.dir/helloworld.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/helloworld.dir/helloworld.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/helloworld.cpp" -o CMakeFiles/helloworld.dir/helloworld.cpp.s

# Object files for target helloworld
helloworld_OBJECTS = \
"CMakeFiles/helloworld.dir/helloworld.cpp.o"

# External object files for target helloworld
helloworld_EXTERNAL_OBJECTS =

helloworld: CMakeFiles/helloworld.dir/helloworld.cpp.o
helloworld: CMakeFiles/helloworld.dir/build.make
helloworld: CMakeFiles/helloworld.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable helloworld"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/helloworld.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/helloworld.dir/build: helloworld

.PHONY : CMakeFiles/helloworld.dir/build

CMakeFiles/helloworld.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/helloworld.dir/cmake_clean.cmake
.PHONY : CMakeFiles/helloworld.dir/clean

CMakeFiles/helloworld.dir/depend:
	cd "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld" "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld" "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/cmake-build-debug" "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/cmake-build-debug" "/home/fuchur/Documents/Hochschule/HS-AlbSig/progprojects/C|C++/helloworld/cmake-build-debug/CMakeFiles/helloworld.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/helloworld.dir/depend

