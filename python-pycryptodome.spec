%define upstream_name pycryptodome

Name:           python-%{upstream_name}
Version:	3.8.2
Release:        2
Summary:        Cryptographic library for Python
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/pycryptodome
Source0:        https://github.com/Legrandin/pycryptodome/archive/v%{version}/%{upstream_name}-%{version}.tar.gz

%description
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
It supports Python 2.4 or newer, all Python 3 versions and PyPy.

%package -n     python2-%{upstream_name}
Summary:        Cryptographic library for Python
Group:          Development/Python
BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(setuptools)
Conflicts:      python2-pycrypto

%description -n python2-%{upstream_name}
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
It supports Python 2.4 or newer, all Python 3 versions and PyPy.

%package -n     python3-%{upstream_name}
Summary:        Cryptographic library for Python
Group:          Development/Python
BuildRequires:  pkgconfig(python)
BuildRequires:  python3egg(setuptools)
Conflicts:      python-pycrypto

%description -n python3-%{upstream_name}
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
It supports Python 2.4 or newer, all Python 3 versions and PyPy.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{upstream_name}
%{python2_sitearch}/Crypto
%{python2_sitearch}/pycryptodome-%{version}-py%{python2_version}.egg-info

%files -n python3-%{upstream_name}
%{python3_sitearch}/Crypto
%{python3_sitearch}/pycryptodome-%{version}-py%{python3_version}.egg-info
