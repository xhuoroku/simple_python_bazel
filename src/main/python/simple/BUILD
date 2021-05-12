load("@subpar//:subpar.bzl", "par_binary")
load("@py2deps//:requirements.bzl", py2_requirement="requirement")
load("@py3deps//:requirements.bzl", "requirement")


par_binary(
    name = 'py2foo',
    srcs = ['py2only.py'],
    deps = [py2_requirement("boto3"),
            py2_requirement("itsdangerous")],
    data = [],
)

py_binary(
    name='py2only',
    deps=[
      py2_requirement("boto3"),
      py2_requirement("itsdangerous"),
    ],
    srcs=['py2only.py'],
    python_version="PY2",
)

py_binary(
    name='py3only',
    deps=[py2_requirement("itsdangerous"),
#          requirement("apache-airflow")
    ],
    srcs=['py3only.py'],
    python_version="PY3",
)