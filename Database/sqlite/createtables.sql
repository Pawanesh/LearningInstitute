CREATE TABLE IF NOT EXISTS Subject (
	ID integer PRIMARY KEY,
	Name text NOT NULL,
    DifficultyLevel integer NOT NULL
);
/**
 {
    "Subject" : [
         {
             1,
             "Art",
             "1 - Beginner"
         },
         {
             2,
             "Art",
             "2 - Intermediate"
         },
         {
             3,
             "Programming",
             "1 - Beginner"
         }
     ]
 }

Insert into Subject values(1, 'Art', 1);
Insert into Subject values(2, 'Art', 2);
**/


CREATE TABLE IF NOT EXISTS Lookup (
	ID integer NOT NULL,
    TypeCode integer NOT NULL,
    Value integer NOT NULL,
	Name text NOT NULL
);
/*
{
    "Lookup" : [
        {
            1,
            -1,
            1,
            "DifficultyLevel"
        },
        {
            2,
            -1,
            1,
            "Gender"
        },
        {
            3,
            1,
            1,
            "Beginner"
        },
        {
            4,
            1,
            2,
            "Intermediate"
        },
        {
            5,
            1,
            3,
            "Expert"
        },
        {
            6,
            2,
            1,
            "M"
        },
        {
            7,
            2,
            1,
            "F"
        }

    ]
}

Insert into Lookup values(1, -1, 1, 'DifficultyLevel');
Insert into Lookup values(2, -1, 1, 'Gender');
Insert into Lookup values(3, 1, 1, 'Beginner');
Insert into Lookup values(4, 1, 2, 'Intermediate');
Insert into Lookup values(5, 1, 3, 'Expert');
Insert into Lookup values(6, 2, 1, 'M');
Insert into Lookup values(7, 2, 2, 'F');

Insert into Lookup values(8, -1, 1, 'DayOfWeek');
Insert into Lookup values(9, 8, 1, 'Mon');
Insert into Lookup values(10, 8, 2, 'Tue');
Insert into Lookup values(11, 8, 3, 'Wed');
Insert into Lookup values(12, 8, 4, 'Thu');
Insert into Lookup values(13, 8, 5, 'Fri');
Insert into Lookup values(14, 8, 6, 'Sat');
Insert into Lookup values(15, 8, 6, 'Sun');
*/



CREATE TABLE IF NOT EXISTS User (
    ID integer PRIMARY KEY,
    Name text NOT NULL,
    UserName text NOT NULL,
    Password text NOT NULL,
    Gender text NOT NULL,
    Age integer NOT NULL,
    ParentName text NOT NULL,
    Address text NOT NULL,
    PhoneNumber text NOT NULL,
    EmailID text NOT NULL
);
/*
{
    "User": [
        {
            1,
            "Rishiv Gupta",
            "Rishiv",
            "Rishiv@123"
            "M",
            3,
            "Pawanesh Gupta",
            "1807 Continental Ave, Apt 215, IL 60563, US",
            "+1 312 292 6187",
            "pawaneshg@gmail.com"
        },
        {
            2,
            "Pawanesh Gupta",
            "Pawanesh",
            "Pawanesh@123"
            "M",
            3,
            "Pawanesh Gupta",
            "1807 Continental Ave, Apt 215, IL 60563, US",
            "+1 312 292 6187",
            "pawaneshg@gmail.com"
        }
        ,
        {
            3,
            "Roshani Gupta",
            "Roshani",
            "Roshani@123"
            "F",
            3,
            "Pawanesh Gupta",
            "1807 Continental Ave, Apt 215, IL 60563, US",
            "+1 312 292 6187",
            "roshani.kathil@gmail.com"
        }
    ]

Insert Into User Values(1, 'Rishiv Gupta', 'Rishiv', 'Rishiv@123',  1, 3, 'Pawanesh Gupta', '1807 Continental Ave, Apt 215, IL 60563, US', '+1 312 292 6187', 'pawaneshg@gmail.com');
Insert Into User Values(2, 'Roshani Gupta', 'Roshani', 'Roshani@123',  1, 3, 'Pawanesh Gupta', '1807 Continental Ave, Apt 215, IL 60563, US', '+1 312 292 6187', 'pawaneshg@gmail.com');
}
*/

CREATE TABLE IF NOT EXISTS Class (
	ID integer PRIMARY KEY,
    SubjectID integer NOT NULL,
    StartDate text NOT NULL,
    EndDate text NOT NULL,
    Time text NOT NULL,
    Day integer NOT NULL,
	Name text NOT NULL
);
/*
Insert INTO Class Values(1, 1, '2022-07-14', '', '4 PM', 2, 'Art beginner Tuesday 4 PM');
Insert INTO Class Values(2, 1, '2022-07-14', '', '4 PM', 4, 'Art beginner Thursday 4 PM');
*/

CREATE TABLE IF NOT EXISTS StudentEnrollment (
    ID integer PRIMARY KEY,
	UserID integer NOT NULL,
    ClassID integer NOT NULL,
    StartDate text NOT NULL,
    EndDate text NOT NULL
);
/*
Insert INTO StudentEnrollment Values (1, 1, 1, '2022-07-14', '');
*/

CREATE TABLE IF NOT EXISTS TeacherEnrollment (
    ID integer PRIMARY KEY,
	UserID integer NOT NULL,
    SubjectID integer NOT NULL,
    StartDate text NOT NULL,
    EndDate text NOT NULL
);
/*
Insert INTO TeacherEnrollment Values (1, 2, 1, '2022-07-14', '');
*/

CREATE TABLE IF NOT EXISTS Attendance (
    ID integer PRIMARY KEY,
	UserID integer NOT NULL,
    ClassID integer NOT NULL,
    Date text NOT NULL
);
/*
Insert INTO Attendance Values (1, 1, 1, '2022-07-14');
*/