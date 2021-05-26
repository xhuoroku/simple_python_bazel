# simple_python_bazel
a simple python project build with bazel
```
$ bazel  run  -s //src/main/python/simple:py2only
$ bazel  run  -s //src/main/python/simple:py3only
```
----------------------------------------------------

 $ bazel build //src/main/python/simple:py2foo.par
DEBUG: /private/var/tmp/_bazel_xhuo/940ca2483e20c08db33b36c0738427a0/external/rules_python/python/legacy_pip_import/pip.bzl:143:10: DEPRECATED: the pip_import rule has been replaced with pip_install, please see rules_python 0.1 release notes
DEBUG: Rule 'subpar' indicated that a canonical reproducible form can be obtained by modifying arguments commit = "c702c484e9dbffedd91999b17aab0cbb3ae61b4c", shallow_since = "1497291257 -0700" and dropping ["tag"]
DEBUG: Repository subpar instantiated at:
  /Users/xhuo/Documents/bazel_workspace/simple_python_bazel/WORKSPACE:55:15: in <toplevel>
Repository rule git_repository defined at:
  /private/var/tmp/_bazel_xhuo/940ca2483e20c08db33b36c0738427a0/external/bazel_tools/tools/build_defs/repo/git.bzl:199:33: in <toplevel>
ERROR: Traceback (most recent call last):
	File "/private/var/tmp/_bazel_xhuo/940ca2483e20c08db33b36c0738427a0/external/subpar/subpar.bzl", line 111, column 27, in <toplevel>
		"main": attr.label(
Error in label: label() got unexpected keyword argument 'single_file'
ERROR: Skipping '//src/main/python/simple:py2foo.par': error loading package 'src/main/python/simple': Extension file 'subpar.bzl' has errors
WARNING: Target pattern parsing failed.
ERROR: error loading package 'src/main/python/simple': Extension file 'subpar.bzl' has errors
INFO: Elapsed time: 3.064s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (1 packages loaded)
