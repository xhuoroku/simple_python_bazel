load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "dpu_rules_pyenv",
    sha256 = "d057168a757efa74e6345edd4776a1c0f38134c2d48eea4f3ef4783e1ea2cb0f",
    strip_prefix = "rules_pyenv-0.1.4",
    urls = ["https://github.com/digital-plumbers-union/rules_pyenv/archive/v0.1.4.tar.gz"],
)

load("@dpu_rules_pyenv//pyenv:defs.bzl", "pyenv_install")


pyenv_install(
    py2 = "2.7.18",
    py3 = "3.9.4",
)

register_toolchains("//:my_toolchain")


load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.2.0/rules_python-0.2.0.tar.gz",
    sha256 = "778197e26c5fbeb07ac2a2c5ae405b30f6cb7ad1f5510ea6fdac03bded96cc6f",
)

load("@rules_python//python/legacy_pip_import:pip.bzl", "pip_import", "pip_repositories")

pip_repositories()
pip_import(
   name = "py2deps",
   requirements = "//:python2_requirements.txt",
   python_interpreter_target="@pyenv//:py2/python",
)
load("@py2deps//:requirements.bzl", _python2_dep_install = "pip_install")
_python2_dep_install()



load("@rules_python//python:pip.bzl", "pip_parse")
# requirements_lock.txt.
pip_parse(
   name = "py3deps",
   requirements_lock = "//:python3_requirements_lock.txt",
   python_interpreter_target="@pyenv//:py3/python",
)

# Load the starlark macro which will define your dependencies.
load("@py3deps//:requirements.bzl", "install_deps")
# Call it to define repos for your requirements.
install_deps()

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
git_repository(
    name = "subpar",
    remote = "https://github.com/google/subpar",
    tag = "1.0.0",
)
