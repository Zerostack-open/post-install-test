import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zs-postinstall-test",
    version="0.0.1Beta",
    scripts=['zspostinstall/zs-post-install'] ,
    author="Jonathan Arrance",
    author_email="jonathan@zerostack.com",
    description="The ZeroStack post install test will ensure your ZeroStack cluster is operational.",
    long_description=long_description,
    url="https://github.com/Zerostack-open/zs-post-install-test",
    packages=setuptools.find_packages(),
    install_requires=[
          'urllib3==1.24.1'
      ],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
