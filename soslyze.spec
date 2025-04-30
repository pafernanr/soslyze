Name: soslyze
Version: 0.0.0
Release: py3
Summary: Summarize SysMgmt/Subscription Management/Insights data from an extracted sosreport archive.

License: GPLv3
URL:            https://github.com/JanSenkyrik/soslyze
Source0: https://github.com/JanSenkyrik/%{name}-%{version}.tar.gz
Group: Applications/System
BuildArch: noarch

BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires: python3-jinja2

%description
SarCharts gets sysstat files from provided sarfilespaths and generates dynamic HTML Charts

%prep
%setup -qn %{name}-%{version}

%build

%install
rm -rf ${RPM_BUILD_ROOT}

mkdir -p ${RPM_BUILD_ROOT}/usr/lib/tools/soslyze/bin
install -D -m 755 soslyze/bin/__init__.py ${RPM_BUILD_ROOT}/usr/lib/tools/soslyze/bin/__init__.py
cp -rp soslyze ${RPM_BUILD_ROOT}/usr/lib/tools/

rm -rf ${RPM_BUILD_ROOT}/usr/lib/tools/%{name}/lib/__pycache__

%post
ln -s -f /usr/lib/tools/soslyze/bin/__init__.py /usr/bin/soslyze

%postun
if [ $1 -eq 0 ] ; then
    rm -f /usr/bin/%{name}
fi

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
/usr/lib/tools/soslyze
