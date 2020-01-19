# TODO:
# - non-root user
# - init script
Summary:	3APA3A 3proxy tiny proxy server
Summary(pl.UTF-8):	Mały serwer proxy 3APA3A 3proxy
Name:		3proxy
Version:	0.8.13
Release:	1
License:	BSD or Apache v2.0 or LGPL v2.1+
Group:		Networking/Daemons
#Source0Download: https://github.com/z3APA3A/3proxy/releases/
Source0:	https://github.com/z3APA3A/3proxy/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d9420c56f05fb78bf9043dd8a30c6a1c
URL:		https://3proxy.ru/?l=EN
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3APA3A 3proxy tiny proxy server.

%description -l pl.UTF-8
Mały serwer proxy 3APA3A 3proxy.

%prep
%setup -q

%build
%{__make} -f Makefile.Linux \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fno-strict-aliasing -pthread -DGETHOSTBYNAME_R -D_THREAD_SAFE -D_REENTRANT -DNOODBC -DWITH_STD_MALLOC -DFD_SETSIZE=4096 -DWITH_POLL -c" \
	LN="%{__cc}" \
	DCFLAGS="-fPIC" \
	LDFLAGS="%{rpmldflags} %{rpmcflags} -pthread"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f Makefile.Linux install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	ETCDIR=$RPM_BUILD_ROOT%{_sysconfdir}/3proxy

# fix page
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man{3,5}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man5/3proxy.cfg.{3,5}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Release.notes authors copying doc/html
%lang(ru) %doc doc/ru
%dir %{_sysconfdir}/3proxy
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/3proxy/bandlimiters
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/3proxy/counters
# FIXME: 3proxy specific user?
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/3proxy/passwd
%attr(755,root,root) %{_bindir}/3proxy
%attr(755,root,root) %{_bindir}/dighosts
%attr(755,root,root) %{_bindir}/ftppr
%attr(755,root,root) %{_bindir}/mycrypt
%attr(755,root,root) %{_bindir}/pop3p
%attr(755,root,root) %{_bindir}/proxy
%attr(755,root,root) %{_bindir}/socks
%attr(755,root,root) %{_bindir}/tcppm
%attr(755,root,root) %{_bindir}/udppm
%{_mandir}/man5/3proxy.cfg.5*
%{_mandir}/man8/3proxy.8*
%{_mandir}/man8/ftppr.8*
%{_mandir}/man8/icqpr.8*
%{_mandir}/man8/pop3p.8*
%{_mandir}/man8/proxy.8*
%{_mandir}/man8/smtpp.8*
%{_mandir}/man8/socks.8*
%{_mandir}/man8/tcppm.8*
%{_mandir}/man8/udppm.8*
