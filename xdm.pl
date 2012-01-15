#!/usr/bin/perl -w
use strict;
use warnings;
use WWW::Mechanize;

my $mech = WWW::Mechanize->new( autocheck => 1 );
my $lzt_file;

open(lzt_file,">cache/perl.html");

# first, we should login
$mech->get('https://accounts.google.com/ServiceLogin');

$mech->submit_form(
    fields   => {
        Email => 'user@gmail.com', # your email, google account
        Passwd => 'passwd', # your password, please not be 'yyy'
    }
);

$mech->get('http://groups.google.com/group/xidian_linux/topics?gvc=1');
$mech->follow_link( n => 1);

print lzt_file ($mech->content);

close(lzt_file);
