Name:			pthread-stubs
Summary:		libpthread-stubs
Version:		0.3
Release:		6
Group:			Graphics
License:		MIT
URL:			http://xcb.freedesktop.org/dist/libpthread-stubs-0.3.tar.gz
Source:			%{name}-%{version}.tar.gz
Source1001:		%{name}.manifest

BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  libtool

%global TZ_SYS_RO_SHARE	%{?TZ_SYS_RO_SHARE:%TZ_SYS_RO_SHARE}%{!?TZ_SYS_RO_SHARE:/usr/share}

%description
This library provides weak aliases for pthread functions not provided in libc or otherwise available by default.

%prep
%setup -q

%build
cp %{SOURCE1001} .

./configure --prefix=/usr
make %{?jobs:-j%jobs}

%install
%make_install

mkdir -p %{buildroot}%{_libdir}/pkgconfig

%clean
rm -rf %{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc
