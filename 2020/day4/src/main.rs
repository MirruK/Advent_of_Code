use std::default;

#[derive(Debug)]
struct Credentials {
    byr: Option<String>, // (Birth Year)
    iyr: Option<String>, // (Issue Year)
    eyr: Option<String>, // (Expiration Year)
    hgt: Option<String>, // (Height)
    hcl: Option<String>, // (Hair Color)
    ecl: Option<String>, // (Eye Color)
    pid: Option<String>, // (Passport ID)
    cid: Option<String>, // (Country ID)
}

impl Default for Credentials {
    fn default() -> Self {
        Credentials {
            byr: None,
            iyr: None,
            eyr: None,
            hgt: None,
            hcl: None,
            ecl: None,
            pid: None,
            cid: None,
        }
    }
}

fn deserialize_to(serialized: &str) -> Option<Credentials> {
    //-> Credentials {
    let mut creds: Vec<(&str, &str)> = vec![];
    for fields in serialized.split(" ") {
        //println!("{:?}", fields.split(":").collect::<Vec<&str>>());
        let mut temp = fields.split(":").collect::<Vec<&str>>();
        creds.push((temp.get(0).unwrap(), temp.get(1).unwrap()));
    }
    println!("{:?}", creds);
    let mut deserialzed = Credentials::default();
    for cred in creds {
        match cred.0 {
            "byr" => deserialzed.byr = Some(String::from(cred.1)),
            "iyr" => deserialzed.iyr = Some(String::from(cred.1)),
            "eyr" => deserialzed.eyr = Some(String::from(cred.1)),
            "hgt" => deserialzed.hgt = Some(String::from(cred.1)),
            "hcl" => deserialzed.hcl = Some(String::from(cred.1)),
            "ecl" => deserialzed.ecl = Some(String::from(cred.1)),
            "pid" => deserialzed.pid = Some(String::from(cred.1)),
            "cid" => deserialzed.cid = Some(String::from(cred.1)),
            _ => println!("Found invalid Credentials key"),
        }
    }
    return Some(deserialzed);
}

fn split_data() -> Vec<&str> {
    let input = include_str!("./input.txt");
    let curr_line = Some(" ");
    let inp_iter = input.lines();
    let serialized_credentials = Vec::<&str>::default();
    // Check when line is "", when None return Vec of &str
    while curr_line != Some("") {
        curr_line = inp_iter.next();
        if curr_line == None {}
        //deserialize_to()
    }
}

fn main() {
    println!("{:?}", deserialize_to("byr:123 aaa:bbbb hcl:1122baa"));
}
