use 5.010;

my $sum = 0;
my $temp = 0;
my $lastSum = 10000000;
my $total = 0;
my @arr = ();
my $i = 0;


while(<>){
    $temp = int($_);
    $sum += $temp;
    if ($i <= 2) {
        $lastSum = $sum;
    }
    push(@arr,$temp);
    if($i > 2) {
        $sum -= shift @arr;
        if($lastSum < $sum){
            $total += 1;
        }else{
        }
        $lastSum = $sum;
    }    
    $i++;
}

say $total;