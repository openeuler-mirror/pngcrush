%global         _hardened_build 1
Summary:             Optimizer for PNG (Portable Network Graphics) files
Name:                pngcrush
Version:             1.8.13
Release:             1
License:             zlib
URL:                 http://pmt.sourceforge.net/%{name}/
Source0:             https://master.dl.sourceforge.net/project/pmt/pngcrunloadh/1.8.13/pngcrush-1.8.13-nolib.tar.xz
BuildRequires:       docbook-utils gcc libpng-devel pkgconfig zlib-devel
%description
pngcrush is a commandline optimizer for PNG (Portable Network Graphics) files.
Its main purpose is to reduce the size of the PNG IDAT datastream by trying
various compression levels and PNG filter methods. It also can be used to
remove unwanted ancillary chunks, or to add certain chunks including gAMA,
tRNS, iCCP, and textual chunks.

%prep
%setup -q -n %{name}-%{version}-nolib

%build
rm -f z*.h crc32.h deflate.h inf*.h trees.h png*.h # force using system headers
pngflags=$(pkg-config --cflags --libs libpng)
gcc %{optflags} $pngflags -lz -o %{name} %{name}.c

%install
%{__install} -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc ChangeLog.html
%license LICENSE
%{_bindir}/%{name}

%changelog
* Wed Oct 28 2020 jialei <jialei17@huawei.com> - 1.8.13-1
- package init
