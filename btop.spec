Name     : btop
Version  : 1.2.6
Release  : 1
URL      : https://github.com/aristocratos
Source0  : https://github.com/aristocratos/btop/archive/refs/tags/v%{version}.tar.gz
Summary  : Interactive process viewer
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : gcc
BuildRequires : sed

%description
Resource monitor that shows usage and stats for processor, memory, disks, network and processes. C++ version and continuation of bashtop and bpytop.


%prep
%setup -q

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}

%install
%make_install PREFIX=/usr

%files
%defattr(-,root,root,-)
/usr/bin/btop
/usr/share/btop
