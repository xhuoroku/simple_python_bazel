load("@py2deps//:requirements.bzl", py2_requirement="requirement")
load("@py3deps//:requirements.bzl", "requirement")

py_binary(
    name='py2only',
    deps=[
      ":simplelib",
      py2_requirement("boto3"),
      py2_requirement("itsdangerous"),
    ],
    srcs=['py2only.py'],
    python_version="PY2"
)

py_binary(
    name='py3only',
    deps=[py2_requirement("itsdangerous"),
#          requirement("apache-airflow")
    ],
    srcs=['py3only.py'],
    python_version="PY3",
)

py_library(
    name='simplelib',
    srcs=[
        'helper.py',
    ],
    deps=[
        py2_requirement("boto3")
    ],
    visibility = [ "//visibility:public" ],
)

py_test(
    name='py2test',
    deps=[
      '//src/main/python/simple:simplelib',
    ],
    srcs=['py2test.py']
)

py_binary(
    name='py2_simple',
    deps=[
      '//src/main/python/another_folder:another_lib'
    ],
    main='py2_simple.py',
    srcs=['py2_simple.py', 'helper.py'],
)
