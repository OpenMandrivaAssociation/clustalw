Summary:	General purpose multiple alignment program
Name:		clustalw
Version:	2.1
Release:	%mkrel 1
License:	Redistributable when non-commercial
URL:		http://www.clustal.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Source:		http://www.clustal.org/download/%{version}/clustalw-%{version}.tar.gz
Group:		Sciences/Biology

%description
Clustal W is a general purpose multiple alignment program for DNA or
proteins.

Users are free to redistribute ClustalW or ClustalX in it's unmodified
form as long as it is not for commercial gain.

Anyone wishing to redistribute Clustal commercially should contact Toby
Gibson at gibson@embl.de

%prep
%setup -q clustalw-%{version}

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE clustalw_help
%_bindir/*
