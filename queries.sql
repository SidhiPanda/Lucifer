-- CREATE DATABASE Lucifer;

-- USE Lucifer;

CREATE TABLE Characters (
  Name VARCHAR(255),
  DOB DATE,
  Parent1 VARCHAR(255),
  Parent2 VARCHAR(255),
  BeingType VARCHAR(255),
  Rel_Status VARCHAR(255),
  Rel_Partner VARCHAR(255),
  Place_of_Origin VARCHAR(255),
  PRIMARY KEY(Name)
);

INSERT INTO Characters VALUES ("Lucifer Morningstar", NULL, "God", "Goddess", "Archangel", "Committed", "Chloe Decker", "Heaven"), ("Chloe Decker", 1981, "John Decker", "Penelope Decker", "Human", "Committed", "Lucifer Morningstar", "Los Angeles"), ("Amenadiel Canaan", NULL, "God", "Goddess", "Archangel", "Single", NULL, "Heaven"), ("Mazikeen", NULL, NULL, "Lilith", "Demon", "Married", "Eve", "Hell"), ("Aurora Morningstar", 2021, "Lucifer Morningstar", "Chloe Decker", "Nephilim", "Single", NULL, "Los Angeles"), ("Michael Demiurge", NULL, "God", "Goddess", "Archangel", "Single", NULL, "SilverCity"), ("Dan Espinoza", 1980, NULL, NULL, "Human", "Divorced", NULL, "Los Angeles"), ("Trixie Espinoza", 2007, "Dan Espinoza","Chloe Decker", "Human", "Single", NULL, "Los Angeles"), ("Linda Martin", 1978, NULL, NULL, "Human", "Single", NULL, "Los Angeles"), ("Ella Lopez", 1988, NULL, NULL, "Human", "Single", NULL, "Detroit"), ("Malcolm Graham", 1974, NULL, NULL, "Human", "Single", NULL, "Los Angeles"), ("Marcus Pierce", NULL, "Adam", "Eve", "Human", "Single", NULL, NULL), ("Charlotte Richards", 1978, NULL, NULL, "Human", "Divorced", NULL, "Los Angeles");

CREATE TABLE Cases (
  Case_Num INT,
  Victim VARCHAR(255),
  Accused VARCHAR(255),
  Type_of_Case VARCHAR(255),
  Status_of_Vicitm VARCHAR(255),
  Murder_Weapon VARCHAR(255),
  Rel_with_Luci VARCHAR(255),
  PRIMARY KEY(Case_Num),
  FOREIGN KEY (Victim) REFERENCES Characters(Name),
  FOREIGN KEY (Accused) REFERENCES Characters(Name)
);

CREATE TABLE Character_Age (
  Name VARCHAR(255),
  Age INT,
  PRIMARY KEY(Name),
  FOREIGN KEY (Name) REFERENCES Characters(Name)
);

CREATE TABLE Abilities (
  Name VARCHAR(255),
  Special_Ability VARCHAR(255),
  PRIMARY KEY(Name, Special_Ability),
  FOREIGN KEY (Name) REFERENCES Characters(Name)
);

CREATE TABLE Landmark_Properties (
  Name VARCHAR(255),
  Address VARCHAR(255),
  Valuation INT,
  PRIMARY KEY(Address)
);

CREATE TABLE Vehicles (
  Vehicle_No VARCHAR(255),
  Reg_No INT,
  Model VARCHAR(255),
  PRIMARY KEY(Vehicle_No, Reg_No)
);

CREATE TABLE Illegal_Substance (
  Common_Name VARCHAR(255),
  Scientific_Name VARCHAR(255),
  Price_per_Kilo INT,
  Dealer VARCHAR(255),
  PRIMARY KEY(Scientific_Name),
  FOREIGN KEY (Dealer) REFERENCES Characters(Name)
);

CREATE TABLE Dependant_Family (
  C_Name VARCHAR(255),
  D_Partner_Name VARCHAR(255),
  D_First_Child_Name VARCHAR(255),
  PRIMARY KEY(C_Name, D_Partner_Name),
  FOREIGN KEY (C_Name) REFERENCES Characters(Name)
);

CREATE TABLE Godly_Weapons (
  Owned_By VARCHAR(255),
  Level INT,
  Name VARCHAR(255),
  Location_Stored_At VARCHAR(255),
  PRIMARY KEY(Owned_By),
  FOREIGN KEY (Owned_By) REFERENCES Characters(Name),
  FOREIGN KEY (Location_Stored_At) REFERENCES Landmark_Properties(Address)
);

CREATE TABLE Subs_with_Case (
  Case_No INT,
  Illegal_Substance VARCHAR(255),
  PRIMARY KEY(Case_No, Illegal_Substance),
  FOREIGN KEY (Case_No) REFERENCES Cases(Case_Num),
  FOREIGN KEY (Illegal_Substance) REFERENCES Illegal_Substance(Scientific_Name)
);

CREATE TABLE Team (
  Case_No INT,
  Detective1 VARCHAR(255),
  Detective2 VARCHAR(255),
  PRIMARY KEY(Case_No, Detective1, Detective2),
  FOREIGN KEY (Case_No) REFERENCES Cases(Case_Num),
  FOREIGN KEY (Detective1) REFERENCES Characters(Name),
  FOREIGN KEY (Detective2) REFERENCES Characters(Name)
);

CREATE TABLE Ownership (
  Char_Name VARCHAR(255),
  Vehicle_No VARCHAR(255),
  Property_Add VARCHAR(255),
  PRIMARY KEY(Char_Name, Vehicle_No, Property_Add),
  FOREIGN KEY (Char_Name) REFERENCES Characters(Name),
  FOREIGN KEY (Vehicle_No) REFERENCES Vehicles(Vehicle_No),
  FOREIGN KEY (Property_Add) REFERENCES Landmark_Properties(Address)
);

CREATE TABLE Murder (
  Killer_Name VARCHAR(255),
  Casualty VARCHAR(255),
  Case_No INT,
  Godly_Weapon VARCHAR(255),
  PRIMARY KEY(Killer_Name, Casualty, Case_No, Godly_Weapon),
  FOREIGN KEY (Killer_Name) REFERENCES Characters(Name),
  FOREIGN KEY (Casualty) REFERENCES Characters(Name),
  FOREIGN KEY (Case_No) REFERENCES Cases(Case_Num),
  FOREIGN KEY (Godly_Weapon) REFERENCES Godly_Weapons(Owned_By)
);

CREATE TABLE Individual_Shares (
  Property_Add VARCHAR(255),
  Owned_By VARCHAR(255),
  Share INT,
  PRIMARY KEY(Property_Add, Owned_By),
  FOREIGN KEY (Property_Add) REFERENCES Landmark_Properties(Address),
  FOREIGN KEY (Owned_By) REFERENCES Characters(Name)
);

SHOW TABLES;