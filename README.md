# simple_python_bazel
a simple python project build with bazel
```
$ bazel  run  -s //src/main/python/simple:py2only
$ bazel  run  -s //src/main/python/simple:py3only
```
----------------------------------------------------

Moved away from pyenv, using system installed python interpreter instead

```
$ bazel build //src/main/python/simple:py2only --build_python_zip
 $ python bazel-out/darwin-py2-fastbuild/bin/src/main/python/simple/py2only.zip
Python 2 only!
yay done!
2.7.16 (default, Jun  5 2020, 22:59:21)
[GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc-
```
```
$ bazel build //src/main/python/simple:py3only --build_python_zip
$ /usr/bin/python3 bazel-bin/src/main/python/simple/py3only.zip
3.8.2 (default, Dec 21 2020, 15:06:04)
[Clang 12.0.0 (clang-1200.0.32.29)]
yay done!
```

