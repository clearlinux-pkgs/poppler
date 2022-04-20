#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : poppler
Version  : 22.04.0
Release  : 75
URL      : https://poppler.freedesktop.org/poppler-22.04.0.tar.xz
Source0  : https://poppler.freedesktop.org/poppler-22.04.0.tar.xz
Source1  : https://poppler.freedesktop.org/poppler-22.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0
Requires: poppler-bin = %{version}-%{release}
Requires: poppler-data = %{version}-%{release}
Requires: poppler-filemap = %{version}-%{release}
Requires: poppler-lib = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}
Requires: poppler-man = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : curl-dev
BuildRequires : freetype-dev
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : gtk-doc-data
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : openjpeg
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo-pdf)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(nss)
BuildRequires : python3
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras
BuildRequires : tiff-dev
BuildRequires : zlib-dev

%description
Poppler, a PDF rendering library
================================
This is Poppler, a library for rendering PDF files, and examining or
modifying their structure.  Poppler originally came from the XPDF

%package bin
Summary: bin components for the poppler package.
Group: Binaries
Requires: poppler-data = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}
Requires: poppler-filemap = %{version}-%{release}

%description bin
bin components for the poppler package.


%package data
Summary: data components for the poppler package.
Group: Data

%description data
data components for the poppler package.


%package dev
Summary: dev components for the poppler package.
Group: Development
Requires: poppler-lib = %{version}-%{release}
Requires: poppler-bin = %{version}-%{release}
Requires: poppler-data = %{version}-%{release}
Provides: poppler-devel = %{version}-%{release}
Requires: poppler = %{version}-%{release}

%description dev
dev components for the poppler package.


%package extras
Summary: extras components for the poppler package.
Group: Default

%description extras
extras components for the poppler package.


%package filemap
Summary: filemap components for the poppler package.
Group: Default

%description filemap
filemap components for the poppler package.


%package lib
Summary: lib components for the poppler package.
Group: Libraries
Requires: poppler-data = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}
Requires: poppler-filemap = %{version}-%{release}

%description lib
lib components for the poppler package.


%package license
Summary: license components for the poppler package.
Group: Default

%description license
license components for the poppler package.


%package man
Summary: man components for the poppler package.
Group: Default

%description man
man components for the poppler package.


%prep
%setup -q -n poppler-22.04.0
cd %{_builddir}/poppler-22.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650436235
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
%cmake .. -DENABLE_UNSTABLE_API_ABI_HEADERS=ON -DENABLE_UTILS=ON -DENABLE_LIBOPENJPEG=none
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DENABLE_UNSTABLE_API_ABI_HEADERS=ON -DENABLE_UTILS=ON -DENABLE_LIBOPENJPEG=none
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1650436235
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/poppler
cp %{_builddir}/poppler-22.04.0/COPYING %{buildroot}/usr/share/package-licenses/poppler/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/poppler-22.04.0/COPYING3 %{buildroot}/usr/share/package-licenses/poppler/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/poppler-22.04.0/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/poppler/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pdfattach
/usr/bin/pdfdetach
/usr/bin/pdffonts
/usr/bin/pdfimages
/usr/bin/pdfinfo
/usr/bin/pdfseparate
/usr/bin/pdfsig
/usr/bin/pdftocairo
/usr/bin/pdftohtml
/usr/bin/pdftoppm
/usr/bin/pdftops
/usr/bin/pdftotext
/usr/bin/pdfunite
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Poppler-0.18.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/poppler/CairoFontEngine.h
/usr/include/poppler/CairoOutputDev.h
/usr/include/poppler/CairoRescaleBox.h
/usr/include/poppler/cpp/poppler-destination.h
/usr/include/poppler/cpp/poppler-document.h
/usr/include/poppler/cpp/poppler-embedded-file.h
/usr/include/poppler/cpp/poppler-font-private.h
/usr/include/poppler/cpp/poppler-font.h
/usr/include/poppler/cpp/poppler-global.h
/usr/include/poppler/cpp/poppler-image.h
/usr/include/poppler/cpp/poppler-page-renderer.h
/usr/include/poppler/cpp/poppler-page-transition.h
/usr/include/poppler/cpp/poppler-page.h
/usr/include/poppler/cpp/poppler-rectangle.h
/usr/include/poppler/cpp/poppler-toc.h
/usr/include/poppler/cpp/poppler-version.h
/usr/include/poppler/cpp/poppler_cpp_export.h
/usr/include/poppler/glib/poppler-action.h
/usr/include/poppler/glib/poppler-annot.h
/usr/include/poppler/glib/poppler-attachment.h
/usr/include/poppler/glib/poppler-date.h
/usr/include/poppler/glib/poppler-document.h
/usr/include/poppler/glib/poppler-enums.h
/usr/include/poppler/glib/poppler-features.h
/usr/include/poppler/glib/poppler-form-field.h
/usr/include/poppler/glib/poppler-layer.h
/usr/include/poppler/glib/poppler-macros.h
/usr/include/poppler/glib/poppler-media.h
/usr/include/poppler/glib/poppler-movie.h
/usr/include/poppler/glib/poppler-page.h
/usr/include/poppler/glib/poppler-structure-element.h
/usr/include/poppler/glib/poppler.h
/usr/include/poppler/qt5/poppler-annotation.h
/usr/include/poppler/qt5/poppler-export.h
/usr/include/poppler/qt5/poppler-form.h
/usr/include/poppler/qt5/poppler-link.h
/usr/include/poppler/qt5/poppler-media.h
/usr/include/poppler/qt5/poppler-optcontent.h
/usr/include/poppler/qt5/poppler-page-transition.h
/usr/include/poppler/qt5/poppler-qt5.h
/usr/include/poppler/qt5/poppler-version.h
/usr/lib64/libpoppler-cpp.so
/usr/lib64/libpoppler-glib.so
/usr/lib64/libpoppler-qt5.so
/usr/lib64/pkgconfig/poppler-cpp.pc
/usr/lib64/pkgconfig/poppler-glib.pc
/usr/lib64/pkgconfig/poppler-qt5.pc

%files extras
%defattr(-,root,root,-)
/usr/include/poppler/Annot.h
/usr/include/poppler/AnnotStampImageHelper.h
/usr/include/poppler/Array.h
/usr/include/poppler/BBoxOutputDev.h
/usr/include/poppler/CMap.h
/usr/include/poppler/CachedFile.h
/usr/include/poppler/Catalog.h
/usr/include/poppler/CertificateInfo.h
/usr/include/poppler/CharCodeToUnicode.h
/usr/include/poppler/CharTypes.h
/usr/include/poppler/CurlCachedFile.h
/usr/include/poppler/CurlPDFDocBuilder.h
/usr/include/poppler/DateInfo.h
/usr/include/poppler/Decrypt.h
/usr/include/poppler/Dict.h
/usr/include/poppler/Error.h
/usr/include/poppler/ErrorCodes.h
/usr/include/poppler/FDPDFDocBuilder.h
/usr/include/poppler/FILECacheLoader.h
/usr/include/poppler/FileSpec.h
/usr/include/poppler/FontEncodingTables.h
/usr/include/poppler/FontInfo.h
/usr/include/poppler/Form.h
/usr/include/poppler/Function.h
/usr/include/poppler/Gfx.h
/usr/include/poppler/GfxFont.h
/usr/include/poppler/GfxState.h
/usr/include/poppler/GfxState_helpers.h
/usr/include/poppler/GlobalParams.h
/usr/include/poppler/Hints.h
/usr/include/poppler/JArithmeticDecoder.h
/usr/include/poppler/JBIG2Stream.h
/usr/include/poppler/JPXStream.h
/usr/include/poppler/JSInfo.h
/usr/include/poppler/Lexer.h
/usr/include/poppler/Linearization.h
/usr/include/poppler/Link.h
/usr/include/poppler/LocalPDFDocBuilder.h
/usr/include/poppler/MarkedContentOutputDev.h
/usr/include/poppler/Movie.h
/usr/include/poppler/NameToCharCode.h
/usr/include/poppler/NameToUnicodeTable.h
/usr/include/poppler/Object.h
/usr/include/poppler/OptionalContent.h
/usr/include/poppler/Outline.h
/usr/include/poppler/OutputDev.h
/usr/include/poppler/PDFDoc.h
/usr/include/poppler/PDFDocBuilder.h
/usr/include/poppler/PDFDocEncoding.h
/usr/include/poppler/PDFDocFactory.h
/usr/include/poppler/PSOutputDev.h
/usr/include/poppler/PSTokenizer.h
/usr/include/poppler/Page.h
/usr/include/poppler/PageTransition.h
/usr/include/poppler/Parser.h
/usr/include/poppler/PopplerCache.h
/usr/include/poppler/PreScanOutputDev.h
/usr/include/poppler/ProfileData.h
/usr/include/poppler/Rendition.h
/usr/include/poppler/SecurityHandler.h
/usr/include/poppler/Sound.h
/usr/include/poppler/SplashOutputDev.h
/usr/include/poppler/Stream-CCITT.h
/usr/include/poppler/Stream.h
/usr/include/poppler/StructElement.h
/usr/include/poppler/StructTreeRoot.h
/usr/include/poppler/TextOutputDev.h
/usr/include/poppler/UTF.h
/usr/include/poppler/UnicodeCClassTables.h
/usr/include/poppler/UnicodeCompTables.h
/usr/include/poppler/UnicodeDecompTables.h
/usr/include/poppler/UnicodeMap.h
/usr/include/poppler/UnicodeMapFuncs.h
/usr/include/poppler/UnicodeMapTables.h
/usr/include/poppler/UnicodeTypeTable.h
/usr/include/poppler/ViewerPreferences.h
/usr/include/poppler/XRef.h
/usr/include/poppler/fofi/FoFiBase.h
/usr/include/poppler/fofi/FoFiEncodings.h
/usr/include/poppler/fofi/FoFiIdentifier.h
/usr/include/poppler/fofi/FoFiTrueType.h
/usr/include/poppler/fofi/FoFiType1.h
/usr/include/poppler/fofi/FoFiType1C.h
/usr/include/poppler/goo/GooCheckedOps.h
/usr/include/poppler/goo/GooLikely.h
/usr/include/poppler/goo/GooString.h
/usr/include/poppler/goo/GooTimer.h
/usr/include/poppler/goo/ImgWriter.h
/usr/include/poppler/goo/JpegWriter.h
/usr/include/poppler/goo/PNGWriter.h
/usr/include/poppler/goo/TiffWriter.h
/usr/include/poppler/goo/gdir.h
/usr/include/poppler/goo/gfile.h
/usr/include/poppler/goo/gmem.h
/usr/include/poppler/goo/grandom.h
/usr/include/poppler/goo/gstrtod.h
/usr/include/poppler/poppler-config.h
/usr/include/poppler/poppler_private_export.h
/usr/include/poppler/splash/Splash.h
/usr/include/poppler/splash/SplashBitmap.h
/usr/include/poppler/splash/SplashClip.h
/usr/include/poppler/splash/SplashErrorCodes.h
/usr/include/poppler/splash/SplashFTFont.h
/usr/include/poppler/splash/SplashFTFontEngine.h
/usr/include/poppler/splash/SplashFTFontFile.h
/usr/include/poppler/splash/SplashFont.h
/usr/include/poppler/splash/SplashFontEngine.h
/usr/include/poppler/splash/SplashFontFile.h
/usr/include/poppler/splash/SplashFontFileID.h
/usr/include/poppler/splash/SplashGlyphBitmap.h
/usr/include/poppler/splash/SplashMath.h
/usr/include/poppler/splash/SplashPath.h
/usr/include/poppler/splash/SplashPattern.h
/usr/include/poppler/splash/SplashScreen.h
/usr/include/poppler/splash/SplashState.h
/usr/include/poppler/splash/SplashTypes.h
/usr/include/poppler/splash/SplashXPath.h
/usr/include/poppler/splash/SplashXPathScanner.h
/usr/lib64/libpoppler-qt5.so.1
/usr/lib64/libpoppler-qt5.so.1.31.0
/usr/lib64/libpoppler.so
/usr/lib64/pkgconfig/poppler.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-poppler

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpoppler-cpp.so.0
/usr/lib64/libpoppler-cpp.so.0.9.0
/usr/lib64/libpoppler-glib.so.8
/usr/lib64/libpoppler-glib.so.8.23.0
/usr/lib64/libpoppler.so.120
/usr/lib64/libpoppler.so.120.0.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/poppler/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/poppler/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/poppler/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pdfattach.1
/usr/share/man/man1/pdfdetach.1
/usr/share/man/man1/pdffonts.1
/usr/share/man/man1/pdfimages.1
/usr/share/man/man1/pdfinfo.1
/usr/share/man/man1/pdfseparate.1
/usr/share/man/man1/pdfsig.1
/usr/share/man/man1/pdftocairo.1
/usr/share/man/man1/pdftohtml.1
/usr/share/man/man1/pdftoppm.1
/usr/share/man/man1/pdftops.1
/usr/share/man/man1/pdftotext.1
/usr/share/man/man1/pdfunite.1
