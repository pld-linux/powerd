Summary:	Powerd is a UPS monitoring program to safely shutdown unattended
Summary(pl):	Powerd jest programem do monitorowania UPS'�w
Name:		powerd
Version:	2.0.2
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://ftp1.sourceforge.net/power/%{name}-%{version}.tar.gz
Source1:	%{name}.init
URL:		http://power.sourceforge.net/
Prereq:		rc-scripts
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	nut

%description
Powerd is an effective power daemon that can monitor a UPS and safely
shutdown the computer. It can also notify other powerd's on the
network that may not be able to monitor the serial line, so they may
also safely shutdown. It also has the capability of auto identifying
your particular UPS and cable configurations.

%description -l pl
Powerd jest efektywnym demonem, kt�ry potrafi monitorowa� UPS'a oraz
bezpiecznie zamkn�� komputer. Potrafi tak�e zakomunikowa� inny demonom
w sieci, kt�re mog� nie potrafi� monitorowa� serial line, wi�c mog�
by� one tak�e bezpiecznie zamkni�te. Demon ten potrafi automatycznie
identyfikowa� twojego UPS'a i konfiguracj� kabla.

%prep
%setup -q

%build
%configure
%{__make} CFLAGS="%{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_sbindir}%{_mandir}/man8}

%{__install} powerd detectups $RPM_BUILD_ROOT%{_sbindir}
%{__install} powerd.8 $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ups

gzip -9nf SUPPORTED Changelog README FAQ TODO

%post
NAME=ups; DESC="powerd ups daemon"; %chkconfig_add

%preun
NAME=ups; %chkconfig_del

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/*/*
