cmake_minimum_required(VERSION 2.8.11)


set(CPACK_PACKAGE_NAME "kodos")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "* kodos is a regex debugger.")
set(CPACK_PACKAGE_VENDOR "Johannes Maier")
set(CPACK_PACKAGE_VERSION "2.4.9-2")
set(SYSTEM_ARCH "all")
set(CPACK_DEBIAN_PACKAGE_DEPENDS "python")
set(CPACK_GENERATOR "DEB")
set(PACKAGE_OS "linux")
execute_process(COMMAND ${CMAKE_CURRENT_LIST_DIR}/get-os.sh OUTPUT_VARIABLE CPACK_DEBIAN_REVISON)
string(STRIP ${CPACK_DEBIAN_REVISON} CPACK_DEBIAN_REVISON)

if (${CMAKE_SYSTEM_PROCESSOR} MATCHES "x86_64")
        set(CPACK_SYSTEM_NAME "${PACKAGE_OS}-amd64")
        set(SYSTEM_ARCH "amd64")
endif()
if (${CMAKE_SYSTEM_PROCESSOR} MATCHES "i386")
        set(CPACK_SYSTEM_NAME "${PACKAGE_OS}-i386")
        set(SYSTEM_ARCH "i386")
endif()
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "Johannes Maier <maier_jo@gmx.de>")

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../dist/kodos DESTINATION bin PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/kodos.desktop DESTINATION /usr/share/applications)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../images/kodos_icon.png DESTINATION /usr/share/pixmaps)


set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_DEBIAN_REVISON}_${SYSTEM_ARCH}")


include(CPack)


