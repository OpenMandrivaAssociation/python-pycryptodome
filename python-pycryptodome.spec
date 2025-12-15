%define upstream_name pycryptodome

Name:           python-%{upstream_name}
Version:	3.23.0
Release:	1
Summary:        Cryptographic library for Python
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/pycryptodome
Source0:        https://github.com/Legrandin/pycryptodome/archive/v%{version}/%{upstream_name}-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(pip)
Provides:       python3-%{upstream_name}
%rename python-pycrypto

%description
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
It supports Python 2.4 or newer, all Python 3 versions and PyPy.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitearch}/Crypto
%{python_sitearch}/pycryptodome-%{version}.dist-info/
