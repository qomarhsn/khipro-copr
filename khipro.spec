Name:           khipro
Version:        33.1.0
Release:        1%{?dist}
Summary:        Khipro Bangla Input Method for m17n

License:        MIT
URL:            https://github.com/rank-coder/khipro-m17n
Source0:        %{url}/archive/refs/tags/v%{version}/khipro-m17n-%{version}.tar.gz

BuildArch:      noarch

%description
Khipro is a shift-free phonetic input method for the Bangla language.
This m17n (multilingualization) version enables Khipro input on Linux
systems. The key feature of Khipro is its shift-free design, allowing
users to type Bangla text efficiently without using the Shift key.

%prep
%autosetup -n khipro-m17n-%{version}

%build
# No build required, just installing pre-built files

%install
mkdir -p %{buildroot}%{_datadir}/m17n
mkdir -p %{buildroot}%{_datadir}/m17n/icons
install -p -m 0644 bn-khipro.mim %{buildroot}%{_datadir}/m17n/
install -p -m 0644 bn-khipro.png %{buildroot}%{_datadir}/m17n/icons/

%files
%{_datadir}/m17n/bn-khipro.mim
%{_datadir}/m17n/icons/bn-khipro.png

%changelog
* Mon Jan 06 2026 qomarhsn <mail@qomarhsn.com> - 33.1.0-1
- Initial package for khipro-m17n v33.1.0
