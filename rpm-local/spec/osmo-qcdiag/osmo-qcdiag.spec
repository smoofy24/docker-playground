#
# spec file for package osmo-qcdiag
#
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           osmo-qcdiag
Version:        0.0.0.git1485275799.cb5d847
Release:        0
Summary:        Osmocom tools for Qualcomm DIAG
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            http://cgit.osmocom.org/osmo-qcdiag/
Source:         %{name}-%{version}.tar.xz
Patch2:         0003-Fix-Makefile.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libosmocore)
BuildRequires:  pkgconfig(libosmogsm)
BuildRequires:  pkgconfig(qmi-glib)

%description
Utility to configure Qualcomm DIAG, read, decode and display the
DIAG messages. It can enable logging and format/print the log
messages generated by the various subsystems of the baseband.

%prep
%setup -q
%patch2 -p1

%build
export CPPFLAGS="%{optflags}"
make -C src/ %{?_smp_mflags}

%install
install -Dm 0755 src/osmo-qcdiag-log %{buildroot}/%{_bindir}/osmo-qcdiag-log
install -Dm 0755 src/color_rxlev.pl %{buildroot}/%{_bindir}/color_rxlev.pl

%files
%license COPYING
%doc README HISTORY TODO
%doc doc
%{_bindir}/osmo-qcdiag-log
%{_bindir}/color_rxlev.pl

%changelog
