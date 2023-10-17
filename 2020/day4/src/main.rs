struct Credentials {
    byr: String, // (Birth Year)
    iyr: String, // (Issue Year)
    eyr: String, // (Expiration Year)
    hgt: String, // (Height)
    hcl: String, // (Hair Color)
    ecl: String, // (Eye Color)
    pid: String, // (Passport ID)
    cid: String, // (Country ID)
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
    None
    //return Credentials {};
}

fn main() {
    deserialize_to("abc:123 aaa:bbbb buu:1122baa");
    println!("Hello, world!");
}
