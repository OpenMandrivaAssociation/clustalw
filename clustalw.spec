Summary:	General purpose multiple alignment program
Name:		clustalw
Version:	2.1
Release:	5
License:	GPLv3 and LGPLv3
URL:		https://www.clustal.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Source:		http://www.clustal.org/download/%{version}/clustalw-%{version}.tar.gz
Group:		Sciences/Biology

%description
CLUSTAL W and CLUSTAL X Multiple Sequence Alignment Programs
                (version 2.1, 17th Nov 2010)                

Contact email address: clustalw@ucd.ie

For details and citation purposes see paper "Clustal W and Clustal X
version 2.0", Larkin M., et al. Bioinformatics 2007 23(21):2947-2948
http://bioinformatics.oxfordjournals.org/cgi/content/full/23/21/2947

Clustal X provides a window-based user interface to the ClustalW
multiple alignment program.                                     

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
%doc README COPYING COPYING.LESSER clustalw_help
%_bindir/*
