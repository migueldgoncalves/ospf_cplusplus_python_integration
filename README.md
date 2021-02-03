# ospf_cplusplus_python_integration
Experiments on integration of Python extensions with C++ OSPF base implementation.

The base code is the Release 2.16 of the ospfd routing software created by John T. Moy, and described in the book [OSPF Complete Implementation](https://dl.acm.org/doi/book/10.5555/1481642).

Executed in Docker containers running Ubuntu 16.04 integrated with GNS3.

## See also

* <http://www.ospf.org> - Original source code by John T. Moy, and respective patches

* <https://github.com/pfa/ospfd-diffs> - Most of required changes to run base code in Ubuntu 16.04

* <https://github.com/migueldgoncalves/ospf_cplusplus_python_integration/releases/tag/Base_code_ubuntu_16> - Base code patched to run in Ubuntu 16, without Python code