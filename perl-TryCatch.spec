%define	module	TryCatch
%define	upstream_version 1.003000

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Easily build XS extensions that depend on XS extensions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/%{module}-%{upstream_version}.tar.xz

BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires:	perl(B::Hooks::OP::Check)
BuildRequires:	perl(B::Hooks::OP::PPAddr)
BuildRequires:	perl(Devel::Declare)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(Parse::Method::Signatures)
BuildRequires:	perl(Scope::Upper)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Variable::Magic)
BuildRequires:	perl(XSLoader)
BuildRequires:	perl-devel

%description
This module aims to provide a nicer syntax and method to catch errors in
Perl, similar to what is found in other languages (such as Java, Python or
C++). The standard method of using 'eval {}; if ($@) {}' is often prone to
subtle bugs, primarily that its far too easy to stomp on the error in error
handlers. And also eval/if isn't the nicest idiom.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3.0-2
+ Revision: 770620
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 607513
- import perl-TryCatch

