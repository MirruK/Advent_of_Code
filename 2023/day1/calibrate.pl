use 5.010;
use List::Util qw(sum);

my @matches = ();
my @nums    = ();

foreach my $line (<STDIN>) {
    push( @matches, ( $line =~ /[0-9]/g ) );
    push( @nums,    int( $matches[0] . $matches[-1] ) );
    @matches = ();
}

#print join( ", ", @nums );
print( sum(@nums) )
