%define upstream_name pycryptodome

Name:           python-%{upstream_name}
Version:	3.14.1
Release:	2
Summary:        Cryptographic library for Python
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/pycryptodome
Source0:        https://github.com/Legrandin/pycryptodome/archive/v%{version}/%{upstream_name}-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Provides:       python3-%{upstream_name}
%rename python-pycrypto

%description
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
It supports Python 2.4 or newer, all Python 3 versions and PyPy.

%package -n     python2-%{upstream_name}
Summary:        Cryptographic library for Python
Group:          Development/Python
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2dist(setuptools)
%rename python2-pycrypto

%description -n python2-%{upstream_name}
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
It supports Python 2.4 or newer, all Python 3 versions and PyPy.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%py2_build
%py_build

%install
%py2_install
%py_install

%files
%{python_sitearch}/Crypto
%{python_sitearch}/pycryptodome-%{version}-py%{python_version}.egg-info

%files -n python2-%{upstream_name}
%{python2_sitearch}/Crypto
%{python2_sitearch}/pycryptodome-%{version}-py%{python2_version}.egg-info
