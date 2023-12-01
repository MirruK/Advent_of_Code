use 5.010;

my $length = 0;
my $depth = 0;
my $aim = 0;

while(<>){
    my ($direction, $num) = split(/ /);
    given ($direction) {
        when("forward"){
            $length += $num;
            $depth += ($aim * $num);
        }
        when("down") {
            $aim += $num;
        }
        when("up") {
            $aim -= $num;
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