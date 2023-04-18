# cython的基本使用
1. 安装cython

   ```shell
   pip install cython
   ```

2. 创建pyx文件编写代码逻辑

3. 创建setup.py并输入以下内容

   ```python
   from distutils.core import setup
   from Cython.Build import cythonize
   
   setup(ext_modules=cythonize('fib_cy.pyx'))
   
   ```

4. 命令行执行以下脚本

   ```shell
   python setup.py build_ext --inplace
   ```

5. 愉快地import并调用
