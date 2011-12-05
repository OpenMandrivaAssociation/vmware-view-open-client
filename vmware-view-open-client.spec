%define	rev	297975
Name:		vmware-view-open-client
Version:	4.5.0
Release: 1
Summary:	VMware View Open Client lets you connect to remote Windows desktops managed by VMware View
Group:		System/X11 
License:	LGPL
Url:		http://code.google.com/p/vmware-view-open-client/
Source0:	http://vmware-view-open-client.googlecode.com/files/VMware-view-open-client-source-%{version}-%{rev}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	boost-devel
BuildRequires:	libgtk+2.0-devel
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	curl-devel

Patch0:		vmware-view-open-client-4.5.0.297975-curl-headers.patch
Patch1:		vmware-view-open-client-4.5.0.297975-linking.patch
Patch2:		format_not_werror.patch
Patch3:		gtk_format_not_string.patch

%description
VMware View Open Client lets you connect from a Linux or Mac OS X 
desktop to remote Windows desktops managed by VMware View.


%prep

%setup -q -n VMware-view-open-client-source-%{version}-%{rev}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%configure2_5x

%install
%makeinstall_std

%files
%{_bindir}/vmware-view
%{_bindir}/vmware-view-log-collector
%{_bindir}/vmware-view-tunnel
%{_datadir}/applications/vmware-view.desktop
%{_datadir}/locale/*
%{_datadir}/pixmaps/vmware-view.png
%{_docdir}/VMware-view-open-client/*
%{_mandir}/man1/vmware-*
