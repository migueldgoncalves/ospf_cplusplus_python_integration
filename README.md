# ospf_cplusplus_python_integration
Experiments on the integration of Python extensions with C++ OSPF base implementation.

The base code is the Release 2.16 of the ospfd routing software created by John T. Moy, and described in the book [OSPF Complete Implementation](https://dl.acm.org/doi/book/10.5555/1481642).

Executed in Docker containers running Ubuntu 16.04 integrated with GNS3.

## Installing and running

A [Dockerfile](https://github.com/migueldgoncalves/ospf_cplusplus_python_integration/blob/main/Dockerfile) is included in this repository, with the required packages to run the program. 

Before running the program, a configuration file `ospfd.conf` must be created or placed inside the /etc directory of the machine or Docker container running the program. A sample [configuration file](https://github.com/migueldgoncalves/ospf_cplusplus_python_integration/blob/main/ospfd.conf) is included in this repository.

It is necessary to provide the absolute path to the /python directory of the source code in the line 98 of the [ospfd_linux.C](https://github.com/migueldgoncalves/ospf_cplusplus_python_integration/blob/ac0582e3da201882b8fdfb3ce622a1275f095330/linux/ospfd_linux.C#L98) file. Currently, it is assumed that the path is /ospf/python.

After copying the content of this repository to the machine, it is necessary to open a terminal and go to the /linux directory of the source code. The program is compiled by running `make install`, and then executed by running `ospfd`. The command `ospfd` can be executed anywhere, and must be run as `root`.

**Note**: When running Docker containers inside GNS3 networks, an /etc directory can be seen inside the directories for each container, inside the respective GNS3 network directory in the host machine. This /etc directory is different from the Ubuntu /etc directory, and is inaccessible from inside the container.

## Python code

Two Python modules have been created along with C++ code interacting with them, producing some output. The Python code is stored in the /python directory of this repository, while the C++ code interacting with Python is stored in the file [ospfd_linux.C](https://github.com/migueldgoncalves/ospf_cplusplus_python_integration/blob/ac0582e3da201882b8fdfb3ce622a1275f095330/linux/ospfd_linux.C#L93). The [Makefile](https://github.com/migueldgoncalves/ospf_cplusplus_python_integration/blob/main/linux/Makefile) was also updated with Python-specific flags.

The experiments involve calling Python functions with different types of arguments and returns, and manipulating Python
objects of different types.

## See also

* <http://www.ospf.org> - Original source code by John T. Moy, and respective patches

* <https://github.com/pfa/ospfd-diffs> - Most of required changes to run the base code in Ubuntu 16.04

* <https://github.com/migueldgoncalves/ospf_cplusplus_python_integration/releases/tag/Base_code_ubuntu_16> - Base code patched to run in Ubuntu 16, without Python code