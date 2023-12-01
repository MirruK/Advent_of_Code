use 5.010;
use List::Util qw(sum);
use Scalar::Util;

sub mapper {
    given ( $_[0] ) {
        when ("one")   { return "1"; }
        when ("two")   { return "2"; }
        when ("three") { return "3"; }
        when ("four")  { return "4"; }
        when ("five")  { return "5"; }
        when ("six")   { return "6"; }
        when ("seven") { return "7"; }
        when ("eight") { return "8"; }
        when ("nine")  { return "9"; }
        default        { return "0"; }
    }
}

my @matches = ();
my @nums    = ();

foreach my $line (<>) {
    push( @matches,
        ( $line =~ /(?=(\d|one|two|three|four|five|six|seven|eight|nine))/g ) );
    for ( my $i = 0 ; $i < ( 0 + @matches ) ; $i++ ) {
        if ( ( length $matches[$i] ) > 1 ) {
            $matches[$i] = mapper( $matches[$i] );
        }
    }
    push( @nums, int( $matches[0] . $matches[-1] ) );
    @matches = ();
}

print( sum(@nums) );
print("\n");
