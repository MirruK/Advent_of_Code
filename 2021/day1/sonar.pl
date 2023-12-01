use 5.010;

my $last = -1;
my $total = -1;

while(<>){
	if ($last < $_) {
	$total = $total + 1;
	}
	$last = $_;
}

say $total;
