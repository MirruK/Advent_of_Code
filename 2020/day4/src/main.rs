use std::any;

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

impl Credentials {
    fn validate(&self) -> bool {
        let values: [Option<String>; 7] = [
            self.byr.clone(),
            self.iyr.clone(),
            self.eyr.clone(),
            self.hgt.clone(),
            self.hcl.clone(),
            self.ecl.clone(),
            self.pid.clone(),
        ];
        return values.iter().all(|f| *f != None);
    }
}

fn deserialize_to(serialized: &str) -> Option<Credentials> {
    let mut creds: Vec<(&str, &str)> = vec![];
    for fields in serialized.split(" ") {
        let temp = fields.split(":").collect::<Vec<&str>>();
        creds.push((temp.get(0).unwrap(), temp.get(1).unwrap()));
    }
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

fn split_data() -> Vec<String> {
    let input = include_str!("./input.txt");
    let mut inp_iter = input.split("\n\n");
    let mut curr_line = inp_iter.next();
    let mut serialized_credentials = Vec::<String>::new();

    while curr_line != None {
        serialized_credentials.push(curr_line.unwrap().replace("\n", " "));
        curr_line = inp_iter.next();
    }

    serialized_credentials
}

fn main() {
    let data = split_data()
        .iter()
        .map(|s| deserialize_to(s))
        .collect::<Vec<Option<Credentials>>>();
    let valid_passports = data.iter().fold(0, |acc, curr| {
        if curr.as_ref().unwrap().validate() {
            acc + 1
        } else {
            acc
        }
    });
    println!("{:?}", valid_passports);
}
