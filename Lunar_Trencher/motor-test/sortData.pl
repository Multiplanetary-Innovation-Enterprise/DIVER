#!usr/bin/perl

my $filename = $ARGV[0];

open (IN, '<', $filename) or die "Could not open file, $!";
open (OUT, '>', "sortedData.csv") or die "Could not open file, $!";

while (my $line = <IN>)
{
  if ($line =~ "Current")
  {
    my @words = split /\s+/, $line;
    print OUT "Current, $words[1], $words[2]\n";
  }
  if ($line =~ "RPM")
  {
    my @words = split /\s+/, $line;
    print OUT "RPM, $words[1], $words[2]\n";
  }
}
