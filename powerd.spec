Summary:	Powerd is a UPS monitoring program to safely shutdown unattended
Name:		powerd
Version:	2.0.0
Release:	1
Source0:	http://ftp1.sourceforge.net/power/%{name}-%{version}.tar.gz
URL:		http://power.sourceforge.net
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Powerd is an effective power daemon that can monitor a UPS and safely
shutdown the computer. It can also notify other powerd's on the
network that may not be able to monitor the serial line, so they may
also safely shutdown. It also has the capability of auto identifying
your particular UPS and cable configurations.

%prep
%setup -q

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g}" 

%install
rm -rf $RPM_BUILD_ROOT
gzip -9nf README COPYING INSTALL TODO
tar   czf sample.conf.tar.gz powerd.conf*

install -d $RPM_BUILD_ROOT%{_sbindir} $RPM_BUILD_ROOT%{_mandir}/man8

install  powerd 	$RPM_BUILD_ROOT%{_sbindir}/
install  detectups 	$RPM_BUILD_ROOT%{_sbindir}/
install  powerd.8 	$RPM_BUILD_ROOT%{_mandir}/man8
			

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/*/*
