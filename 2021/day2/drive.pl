use 5.010;

my $length = 0;
my $depth = 0;
my $aim = 0;

while(<>){
    my ($direction, $num) = split(/ /);
    given ($direction) {
        when("forward"){
            $length += $num;
        }
        when("down") {
            $depth += $num;
        }
        when("up") {
            $depth -= $num;
        }
        default {
            say "WTF????";
        }
    }
}

say "Length: ";
say $length;
say "Depth: ";
say $depth;
say "Product: ";
say $length * $depth;