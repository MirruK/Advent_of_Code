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

fn is_within_bounds(s: Option<&String>, lower: i32, upper: i32) -> bool {
    if s.as_deref() == None {
        return false;
    }
    return s.unwrap().parse::<i32>().unwrap_or_default() >= lower
        && s.unwrap().parse::<i32>().unwrap_or(1000000) <= upper;
}

fn is_height(s: Option<&String>) -> bool {
    if s.as_deref() == None {
        return false;
    }
    if s.unwrap().ends_with("cm") {
        return is_within_bounds(
            Some(
                &s.unwrap()
                    .strip_suffix("cm")
                    .map(|st| st.to_string())
                    .unwrap(),
            ),
            150,
            193,
        );
    }
    if s.unwrap().ends_with("in") {
        return is_within_bounds(
            Some(
                &s.unwrap()
                    .strip_suffix("in")
                    .map(|st| st.to_string())
                    .unwrap(),
            ),
            59,
            76,
        );
    }
    false
}

fn is_hair_color(s: Option<&String>) -> bool {
    if s.as_deref() == None {
        return false;
    }
    if !s.unwrap().starts_with("#") {
        return false;
    }
    if s.unwrap().len() < 7 || s.unwrap().len() > 7 {
        return false;
    }
    let mut chars = s.unwrap().chars();
    let _ = chars.next();
    for _ in 0..6 {
        if !chars.next().unwrap().is_ascii_hexdigit() {
            return false;
        }
    }
    true
}

fn is_eye_color(s: Option<&String>) -> bool {
    if s.is_none() {
        return false;
    }
    match s.clone().unwrap().as_str() {
        "amb" => true,
        "blu" => true,
        "brn" => true,
        "gry" => true,
        "grn" => true,
        "hzl" => true,
        "oth" => true,
        _ => false,
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

    fn validate_strict(&self) -> bool {
        let values: [bool; 7] = [
            is_within_bounds(self.byr.as_ref(), 1920, 2002),
            is_within_bounds(self.iyr.as_ref(), 2010, 2020),
            is_within_bounds(self.eyr.as_ref(), 2020, 2030),
            is_height(self.hgt.as_ref()),
            is_hair_color(self.hcl.as_ref()),
            is_eye_color(self.ecl.as_ref()),
            self.pid.as_ref().unwrap_or(&String::new()).len() == 9
                && match self.pid.as_ref().unwrap().parse::<i32>() {
                    Err(_) => false,
                    _ => true,
                },
        ];
        return values.iter().all(|f| *f);
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
    let valid_passports2 = data.iter().fold(0, |acc, curr| {
        if curr.as_ref().unwrap().validate_strict() {
            acc + 1
        } else {
            acc
        }
    });
    println!("{:?}", valid_passports);
    println!("{:?}", valid_passports2);
}
