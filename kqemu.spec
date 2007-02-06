%define		_rc		Alpha
%define		_rel	0.2
Summary:	KQEMU - KDE GUI for QEMU
Name:		kqemu
Version:	0.3
Release:	0.%{_rc}.%{_rel}
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kqemu/%{name}-%{version}%{_rc}.tgz
# Source0-md5:	2df7544e071c34e92989b281b3145331
URL:		http://kqemu.sourceforge.net/
Requires:	kdewebdev-kommander
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	%{_prefix}/lib

%description
A KDE front-end for QEMU CPU emulator. QEMU is a FAST! processor
emulator using dynamic translation to achieve good emulation speed.

KQEMU makes it easier to launch QEmu directly or create scripts for
easy launching of QEMU environments.

%prep
%setup -qc
cat <<'EOF' > %{name}.sh
#!/bin/sh
exec %{_bindir}/kmdr-executor %{_libdir}/kqemu.kmdr
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
cp -a kqemu.kmdr $RPM_BUILD_ROOT%{_libdir}
install %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog ToDo
%attr(755,root,root) %{_bindir}/kqemu
%{_libdir}/kqemu.kmdr
