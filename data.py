"""
Name variations data and search functionality.
This module contains a comprehensive dataset of names and their variations from multiple cultures.
"""

# Comprehensive dataset of names and their variations
NAMES_DATA = [
    # Male names starting with A
    {'name': 'Aaron', 'variation_of': None},
    {'name': 'Aaronson', 'variation_of': 'Aaron'},
    {'name': 'Ron', 'variation_of': 'Aaron'},
    
    {'name': 'Abraham', 'variation_of': None},
    {'name': 'Abe', 'variation_of': 'Abraham'},
    {'name': 'Abram', 'variation_of': 'Abraham'},
    {'name': 'Bram', 'variation_of': 'Abraham'},
    
    {'name': 'Adam', 'variation_of': None},
    {'name': 'Ad', 'variation_of': 'Adam'},
    
    {'name': 'Adrian', 'variation_of': None},
    {'name': 'Ade', 'variation_of': 'Adrian'},
    
    {'name': 'Alan', 'variation_of': None},
    {'name': 'Al', 'variation_of': 'Alan'},
    {'name': 'Allan', 'variation_of': 'Alan'},
    {'name': 'Allen', 'variation_of': 'Alan'},
    
    {'name': 'Albert', 'variation_of': None},
    {'name': 'Al', 'variation_of': 'Albert'},
    {'name': 'Bert', 'variation_of': 'Albert'},
    {'name': 'Bertie', 'variation_of': 'Albert'},
    
    {'name': 'Alexander', 'variation_of': None},
    {'name': 'Alex', 'variation_of': 'Alexander'},
    {'name': 'Al', 'variation_of': 'Alexander'},
    {'name': 'Xander', 'variation_of': 'Alexander'},
    {'name': 'Alec', 'variation_of': 'Alexander'},
    {'name': 'Lex', 'variation_of': 'Alexander'},
    {'name': 'Sandy', 'variation_of': 'Alexander'},
    {'name': 'Sasha', 'variation_of': 'Alexander'},
    
    {'name': 'Anthony', 'variation_of': None},
    {'name': 'Tony', 'variation_of': 'Anthony'},
    {'name': 'Ant', 'variation_of': 'Anthony'},
    {'name': 'Antonio', 'variation_of': 'Anthony'},
    
    {'name': 'Andrew', 'variation_of': None},
    {'name': 'Andy', 'variation_of': 'Andrew'},
    {'name': 'Drew', 'variation_of': 'Andrew'},
    
    {'name': 'Arthur', 'variation_of': None},
    {'name': 'Art', 'variation_of': 'Arthur'},
    {'name': 'Artie', 'variation_of': 'Arthur'},
    
    {'name': 'Austin', 'variation_of': None},
    {'name': 'Aussie', 'variation_of': 'Austin'},
    
    # Male names starting with B
    {'name': 'Benjamin', 'variation_of': None},
    {'name': 'Ben', 'variation_of': 'Benjamin'},
    {'name': 'Benny', 'variation_of': 'Benjamin'},
    {'name': 'Benji', 'variation_of': 'Benjamin'},
    {'name': 'Bennie', 'variation_of': 'Benjamin'},
    
    {'name': 'Bernard', 'variation_of': None},
    {'name': 'Bernie', 'variation_of': 'Bernard'},
    {'name': 'Barney', 'variation_of': 'Bernard'},
    
    {'name': 'Bradley', 'variation_of': None},
    {'name': 'Brad', 'variation_of': 'Bradley'},
    
    {'name': 'Brandon', 'variation_of': None},
    {'name': 'Bran', 'variation_of': 'Brandon'},
    
    {'name': 'Brian', 'variation_of': None},
    {'name': 'Bryan', 'variation_of': 'Brian'},
    
    {'name': 'Robert', 'variation_of': None},
    {'name': 'Bob', 'variation_of': 'Robert'},
    {'name': 'Rob', 'variation_of': 'Robert'},
    {'name': 'Bobby', 'variation_of': 'Robert'},
    {'name': 'Robbie', 'variation_of': 'Robert'},
    {'name': 'Bert', 'variation_of': 'Robert'},
    {'name': 'Robby', 'variation_of': 'Robert'},
    
    # Male names starting with C
    {'name': 'Calvin', 'variation_of': None},
    {'name': 'Cal', 'variation_of': 'Calvin'},
    
    {'name': 'Cameron', 'variation_of': None},
    {'name': 'Cam', 'variation_of': 'Cameron'},
    
    {'name': 'Carlos', 'variation_of': None},
    {'name': 'Carl', 'variation_of': 'Carlos'},
    
    {'name': 'Charles', 'variation_of': None},
    {'name': 'Charlie', 'variation_of': 'Charles'},
    {'name': 'Chuck', 'variation_of': 'Charles'},
    {'name': 'Chaz', 'variation_of': 'Charles'},
    {'name': 'Chip', 'variation_of': 'Charles'},
    
    {'name': 'Christian', 'variation_of': None},
    {'name': 'Chris', 'variation_of': 'Christian'},
    
    {'name': 'Christopher', 'variation_of': None},
    {'name': 'Chris', 'variation_of': 'Christopher'},
    {'name': 'Christie', 'variation_of': 'Christopher'},
    {'name': 'Kit', 'variation_of': 'Christopher'},
    {'name': 'Topher', 'variation_of': 'Christopher'},
    
    {'name': 'Connor', 'variation_of': None},
    {'name': 'Con', 'variation_of': 'Connor'},
    {'name': 'Connie', 'variation_of': 'Connor'},
    
    # Male names starting with D
    {'name': 'Daniel', 'variation_of': None},
    {'name': 'Dan', 'variation_of': 'Daniel'},
    {'name': 'Danny', 'variation_of': 'Daniel'},
    {'name': 'Dani', 'variation_of': 'Daniel'},
    
    {'name': 'David', 'variation_of': None},
    {'name': 'Dave', 'variation_of': 'David'},
    {'name': 'Davey', 'variation_of': 'David'},
    {'name': 'Davy', 'variation_of': 'David'},
    
    {'name': 'Diego', 'variation_of': None},
    
    {'name': 'Dominic', 'variation_of': None},
    {'name': 'Dom', 'variation_of': 'Dominic'},
    {'name': 'Nick', 'variation_of': 'Dominic'},
    
    {'name': 'Douglas', 'variation_of': None},
    {'name': 'Doug', 'variation_of': 'Douglas'},
    {'name': 'Dougie', 'variation_of': 'Douglas'},
    
    # Male names starting with E
    {'name': 'Edward', 'variation_of': None},
    {'name': 'Ed', 'variation_of': 'Edward'},
    {'name': 'Eddie', 'variation_of': 'Edward'},
    {'name': 'Ted', 'variation_of': 'Edward'},
    {'name': 'Teddy', 'variation_of': 'Edward'},
    {'name': 'Ned', 'variation_of': 'Edward'},
    
    {'name': 'Edwin', 'variation_of': None},
    {'name': 'Ed', 'variation_of': 'Edwin'},
    {'name': 'Eddie', 'variation_of': 'Edwin'},
    
    {'name': 'Emmanuel', 'variation_of': None},
    {'name': 'Manny', 'variation_of': 'Emmanuel'},
    {'name': 'Manuel', 'variation_of': 'Emmanuel'},
    
    {'name': 'Eric', 'variation_of': None},
    {'name': 'Rick', 'variation_of': 'Eric'},
    {'name': 'Ricky', 'variation_of': 'Eric'},
    
    {'name': 'Ernest', 'variation_of': None},
    {'name': 'Ernie', 'variation_of': 'Ernest'},
    
    {'name': 'Eugene', 'variation_of': None},
    {'name': 'Gene', 'variation_of': 'Eugene'},
    
    {'name': 'Evan', 'variation_of': None},
    {'name': 'Ev', 'variation_of': 'Evan'},
    
    # Male names starting with F
    {'name': 'Felix', 'variation_of': None},
    
    {'name': 'Fernando', 'variation_of': None},
    {'name': 'Nando', 'variation_of': 'Fernando'},
    
    {'name': 'Francis', 'variation_of': None},
    {'name': 'Frank', 'variation_of': 'Francis'},
    {'name': 'Frankie', 'variation_of': 'Francis'},
    {'name': 'Fran', 'variation_of': 'Francis'},
    
    {'name': 'Francisco', 'variation_of': None},
    {'name': 'Frank', 'variation_of': 'Francisco'},
    {'name': 'Cisco', 'variation_of': 'Francisco'},
    {'name': 'Paco', 'variation_of': 'Francisco'},
    
    {'name': 'Frederick', 'variation_of': None},
    {'name': 'Fred', 'variation_of': 'Frederick'},
    {'name': 'Freddie', 'variation_of': 'Frederick'},
    {'name': 'Rick', 'variation_of': 'Frederick'},
    {'name': 'Fritz', 'variation_of': 'Frederick'},
    
    # Male names starting with G
    {'name': 'Gabriel', 'variation_of': None},
    {'name': 'Gabe', 'variation_of': 'Gabriel'},
    {'name': 'Gabby', 'variation_of': 'Gabriel'},
    
    {'name': 'Geoffrey', 'variation_of': None},
    {'name': 'Geoff', 'variation_of': 'Geoffrey'},
    {'name': 'Jeff', 'variation_of': 'Geoffrey'},
    
    {'name': 'George', 'variation_of': None},
    {'name': 'Georgie', 'variation_of': 'George'},
    
    {'name': 'Gerald', 'variation_of': None},
    {'name': 'Gerry', 'variation_of': 'Gerald'},
    {'name': 'Jerry', 'variation_of': 'Gerald'},
    
    {'name': 'Gregory', 'variation_of': None},
    {'name': 'Greg', 'variation_of': 'Gregory'},
    {'name': 'Greggy', 'variation_of': 'Gregory'},
    
    {'name': 'Guillermo', 'variation_of': None},
    {'name': 'Memo', 'variation_of': 'Guillermo'},
    {'name': 'Willy', 'variation_of': 'Guillermo'},
    
    # Male names starting with H
    {'name': 'Harold', 'variation_of': None},
    {'name': 'Harry', 'variation_of': 'Harold'},
    {'name': 'Hal', 'variation_of': 'Harold'},
    
    {'name': 'Harrison', 'variation_of': None},
    {'name': 'Harry', 'variation_of': 'Harrison'},
    
    {'name': 'Henry', 'variation_of': None},
    {'name': 'Hank', 'variation_of': 'Henry'},
    {'name': 'Harry', 'variation_of': 'Henry'},
    {'name': 'Hal', 'variation_of': 'Henry'},
    
    {'name': 'Howard', 'variation_of': None},
    {'name': 'Howie', 'variation_of': 'Howard'},
    
    # Male names starting with I
    {'name': 'Ian', 'variation_of': None},
    
    {'name': 'Isaac', 'variation_of': None},
    {'name': 'Ike', 'variation_of': 'Isaac'},
    {'name': 'Izzy', 'variation_of': 'Isaac'},
    
    # Male names starting with J
    {'name': 'Jacob', 'variation_of': None},
    {'name': 'Jake', 'variation_of': 'Jacob'},
    {'name': 'Jack', 'variation_of': 'Jacob'},
    {'name': 'Coby', 'variation_of': 'Jacob'},
    
    {'name': 'James', 'variation_of': None},
    {'name': 'Jim', 'variation_of': 'James'},
    {'name': 'Jimmy', 'variation_of': 'James'},
    {'name': 'Jamie', 'variation_of': 'James'},
    {'name': 'Jem', 'variation_of': 'James'},
    
    {'name': 'Jason', 'variation_of': None},
    {'name': 'Jay', 'variation_of': 'Jason'},
    
    {'name': 'Jeffrey', 'variation_of': None},
    {'name': 'Jeff', 'variation_of': 'Jeffrey'},
    {'name': 'Jeffie', 'variation_of': 'Jeffrey'},
    
    {'name': 'Jeremy', 'variation_of': None},
    {'name': 'Jerry', 'variation_of': 'Jeremy'},
    {'name': 'Jem', 'variation_of': 'Jeremy'},
    
    {'name': 'Jesse', 'variation_of': None},
    {'name': 'Jess', 'variation_of': 'Jesse'},
    
    {'name': 'Jesus', 'variation_of': None},
    {'name': 'Chuy', 'variation_of': 'Jesus'},
    
    {'name': 'John', 'variation_of': None},
    {'name': 'Johnny', 'variation_of': 'John'},
    {'name': 'Jack', 'variation_of': 'John'},
    {'name': 'Jackie', 'variation_of': 'John'},
    {'name': 'Johnnie', 'variation_of': 'John'},
    
    {'name': 'Jonathan', 'variation_of': None},
    {'name': 'Jon', 'variation_of': 'Jonathan'},
    {'name': 'Jonny', 'variation_of': 'Jonathan'},
    {'name': 'Johnny', 'variation_of': 'Jonathan'},
    
    {'name': 'Jordan', 'variation_of': None},
    {'name': 'Jordy', 'variation_of': 'Jordan'},
    
    {'name': 'Jose', 'variation_of': None},
    {'name': 'Joe', 'variation_of': 'Jose'},
    {'name': 'Pepe', 'variation_of': 'Jose'},
    
    {'name': 'Joseph', 'variation_of': None},
    {'name': 'Joe', 'variation_of': 'Joseph'},
    {'name': 'Joey', 'variation_of': 'Joseph'},
    {'name': 'Jo', 'variation_of': 'Joseph'},
    
    {'name': 'Joshua', 'variation_of': None},
    {'name': 'Josh', 'variation_of': 'Joshua'},
    
    {'name': 'Juan', 'variation_of': None},
    {'name': 'Juanito', 'variation_of': 'Juan'},
    
    {'name': 'Julian', 'variation_of': None},
    {'name': 'Jules', 'variation_of': 'Julian'},
    
    {'name': 'Justin', 'variation_of': None},
    {'name': 'Just', 'variation_of': 'Justin'},
    
    # Male names starting with K
    {'name': 'Kenneth', 'variation_of': None},
    {'name': 'Ken', 'variation_of': 'Kenneth'},
    {'name': 'Kenny', 'variation_of': 'Kenneth'},
    
    {'name': 'Kevin', 'variation_of': None},
    {'name': 'Kev', 'variation_of': 'Kevin'},
    
    # Male names starting with L
    {'name': 'Lawrence', 'variation_of': None},
    {'name': 'Larry', 'variation_of': 'Lawrence'},
    {'name': 'Lance', 'variation_of': 'Lawrence'},
    
    {'name': 'Leonardo', 'variation_of': None},
    {'name': 'Leo', 'variation_of': 'Leonardo'},
    {'name': 'Leon', 'variation_of': 'Leonardo'},
    
    {'name': 'Louis', 'variation_of': None},
    {'name': 'Lou', 'variation_of': 'Louis'},
    {'name': 'Louie', 'variation_of': 'Louis'},
    
    {'name': 'Lucas', 'variation_of': None},
    {'name': 'Luke', 'variation_of': 'Lucas'},
    
    # Male names starting with M
    {'name': 'Manuel', 'variation_of': None},
    {'name': 'Manny', 'variation_of': 'Manuel'},
    
    {'name': 'Marcus', 'variation_of': None},
    {'name': 'Mark', 'variation_of': 'Marcus'},
    {'name': 'Marc', 'variation_of': 'Marcus'},
    
    {'name': 'Martin', 'variation_of': None},
    {'name': 'Marty', 'variation_of': 'Martin'},
    
    {'name': 'Matthew', 'variation_of': None},
    {'name': 'Matt', 'variation_of': 'Matthew'},
    {'name': 'Matty', 'variation_of': 'Matthew'},
    
    {'name': 'Maurice', 'variation_of': None},
    {'name': 'Mo', 'variation_of': 'Maurice'},
    {'name': 'Maury', 'variation_of': 'Maurice'},
    
    {'name': 'Maxwell', 'variation_of': None},
    {'name': 'Max', 'variation_of': 'Maxwell'},
    
    {'name': 'Michael', 'variation_of': None},
    {'name': 'Mike', 'variation_of': 'Michael'},
    {'name': 'Mickey', 'variation_of': 'Michael'},
    {'name': 'Mick', 'variation_of': 'Michael'},
    {'name': 'Mikey', 'variation_of': 'Michael'},
    
    {'name': 'Miguel', 'variation_of': None},
    {'name': 'Mike', 'variation_of': 'Miguel'},
    
    # Male names starting with N
    {'name': 'Nathan', 'variation_of': None},
    {'name': 'Nate', 'variation_of': 'Nathan'},
    {'name': 'Nat', 'variation_of': 'Nathan'},
    
    {'name': 'Nathaniel', 'variation_of': None},
    {'name': 'Nate', 'variation_of': 'Nathaniel'},
    {'name': 'Nathan', 'variation_of': 'Nathaniel'},
    {'name': 'Nat', 'variation_of': 'Nathaniel'},
    
    {'name': 'Nicholas', 'variation_of': None},
    {'name': 'Nick', 'variation_of': 'Nicholas'},
    {'name': 'Nicky', 'variation_of': 'Nicholas'},
    {'name': 'Nico', 'variation_of': 'Nicholas'},
    
    {'name': 'Noah', 'variation_of': None},
    
    # Male names starting with O
    {'name': 'Oliver', 'variation_of': None},
    {'name': 'Ollie', 'variation_of': 'Oliver'},
    
    {'name': 'Oscar', 'variation_of': None},
    {'name': 'Oz', 'variation_of': 'Oscar'},
    
    # Male names starting with P
    {'name': 'Patrick', 'variation_of': None},
    {'name': 'Pat', 'variation_of': 'Patrick'},
    {'name': 'Patty', 'variation_of': 'Patrick'},
    {'name': 'Paddy', 'variation_of': 'Patrick'},
    {'name': 'Rick', 'variation_of': 'Patrick'},
    
    {'name': 'Paul', 'variation_of': None},
    {'name': 'Paulie', 'variation_of': 'Paul'},
    
    {'name': 'Peter', 'variation_of': None},
    {'name': 'Pete', 'variation_of': 'Peter'},
    {'name': 'Petey', 'variation_of': 'Peter'},
    
    {'name': 'Philip', 'variation_of': None},
    {'name': 'Phil', 'variation_of': 'Philip'},
    {'name': 'Flip', 'variation_of': 'Philip'},
    
    # Male names starting with R
    {'name': 'Rafael', 'variation_of': None},
    {'name': 'Rafa', 'variation_of': 'Rafael'},
    
    {'name': 'Raymond', 'variation_of': None},
    {'name': 'Ray', 'variation_of': 'Raymond'},
    {'name': 'Raymie', 'variation_of': 'Raymond'},
    
    {'name': 'Ricardo', 'variation_of': None},
    {'name': 'Rick', 'variation_of': 'Ricardo'},
    {'name': 'Ricky', 'variation_of': 'Ricardo'},
    
    {'name': 'Richard', 'variation_of': None},
    {'name': 'Rick', 'variation_of': 'Richard'},
    {'name': 'Dick', 'variation_of': 'Richard'},
    {'name': 'Richie', 'variation_of': 'Richard'},
    {'name': 'Ricky', 'variation_of': 'Richard'},
    {'name': 'Rich', 'variation_of': 'Richard'},
    
    {'name': 'Roberto', 'variation_of': None},
    {'name': 'Rob', 'variation_of': 'Roberto'},
    {'name': 'Bobby', 'variation_of': 'Roberto'},
    {'name': 'Berto', 'variation_of': 'Roberto'},
    
    {'name': 'Roger', 'variation_of': None},
    {'name': 'Rog', 'variation_of': 'Roger'},
    
    {'name': 'Ronald', 'variation_of': None},
    {'name': 'Ron', 'variation_of': 'Ronald'},
    {'name': 'Ronnie', 'variation_of': 'Ronald'},
    
    {'name': 'Ryan', 'variation_of': None},
    {'name': 'Ry', 'variation_of': 'Ryan'},
    
    # Male names starting with S
    {'name': 'Samuel', 'variation_of': None},
    {'name': 'Sam', 'variation_of': 'Samuel'},
    {'name': 'Sammy', 'variation_of': 'Samuel'},
    
    {'name': 'Sebastian', 'variation_of': None},
    {'name': 'Seb', 'variation_of': 'Sebastian'},
    {'name': 'Bastian', 'variation_of': 'Sebastian'},
    
    {'name': 'Sergio', 'variation_of': None},
    
    {'name': 'Stephen', 'variation_of': None},
    {'name': 'Steve', 'variation_of': 'Stephen'},
    {'name': 'Stevie', 'variation_of': 'Stephen'},
    {'name': 'Stefan', 'variation_of': 'Stephen'},
    
    {'name': 'Steven', 'variation_of': None},
    {'name': 'Steve', 'variation_of': 'Steven'},
    {'name': 'Stevie', 'variation_of': 'Steven'},
    
    # Male names starting with T
    {'name': 'Theodore', 'variation_of': None},
    {'name': 'Ted', 'variation_of': 'Theodore'},
    {'name': 'Teddy', 'variation_of': 'Theodore'},
    {'name': 'Theo', 'variation_of': 'Theodore'},
    
    {'name': 'Thomas', 'variation_of': None},
    {'name': 'Tom', 'variation_of': 'Thomas'},
    {'name': 'Tommy', 'variation_of': 'Thomas'},
    {'name': 'Thom', 'variation_of': 'Thomas'},
    
    {'name': 'Timothy', 'variation_of': None},
    {'name': 'Tim', 'variation_of': 'Timothy'},
    {'name': 'Timmy', 'variation_of': 'Timothy'},
    
    {'name': 'Tyler', 'variation_of': None},
    {'name': 'Ty', 'variation_of': 'Tyler'},
    
    # Male names starting with V
    {'name': 'Victor', 'variation_of': None},
    {'name': 'Vic', 'variation_of': 'Victor'},
    {'name': 'Vicky', 'variation_of': 'Victor'},
    
    {'name': 'Vincent', 'variation_of': None},
    {'name': 'Vince', 'variation_of': 'Vincent'},
    {'name': 'Vinny', 'variation_of': 'Vincent'},
    
    # Male names starting with W
    {'name': 'Walter', 'variation_of': None},
    {'name': 'Walt', 'variation_of': 'Walter'},
    {'name': 'Wally', 'variation_of': 'Walter'},
    
    {'name': 'William', 'variation_of': None},
    {'name': 'Will', 'variation_of': 'William'},
    {'name': 'Bill', 'variation_of': 'William'},
    {'name': 'Billy', 'variation_of': 'William'},
    {'name': 'Willie', 'variation_of': 'William'},
    {'name': 'Liam', 'variation_of': 'William'},
    {'name': 'Willy', 'variation_of': 'William'},
    
    # Male names starting with Z
    {'name': 'Zachary', 'variation_of': None},
    {'name': 'Zach', 'variation_of': 'Zachary'},
    {'name': 'Zack', 'variation_of': 'Zachary'},
    {'name': 'Zacky', 'variation_of': 'Zachary'},
    
    # Female names starting with A
    {'name': 'Abigail', 'variation_of': None},
    {'name': 'Abby', 'variation_of': 'Abigail'},
    {'name': 'Gail', 'variation_of': 'Abigail'},
    
    {'name': 'Ada', 'variation_of': None},
    {'name': 'Addie', 'variation_of': 'Ada'},
    
    {'name': 'Adelaide', 'variation_of': None},
    {'name': 'Addie', 'variation_of': 'Adelaide'},
    {'name': 'Della', 'variation_of': 'Adelaide'},
    
    {'name': 'Adriana', 'variation_of': None},
    {'name': 'Adri', 'variation_of': 'Adriana'},
    
    {'name': 'Agnes', 'variation_of': None},
    {'name': 'Aggie', 'variation_of': 'Agnes'},
    
    {'name': 'Alexandra', 'variation_of': None},
    {'name': 'Alex', 'variation_of': 'Alexandra'},
    {'name': 'Alexa', 'variation_of': 'Alexandra'},
    {'name': 'Lexie', 'variation_of': 'Alexandra'},
    {'name': 'Sandy', 'variation_of': 'Alexandra'},
    {'name': 'Sasha', 'variation_of': 'Alexandra'},
    {'name': 'Allie', 'variation_of': 'Alexandra'},
    
    {'name': 'Alice', 'variation_of': None},
    {'name': 'Allie', 'variation_of': 'Alice'},
    {'name': 'Ali', 'variation_of': 'Alice'},
    
    {'name': 'Alicia', 'variation_of': None},
    {'name': 'Ali', 'variation_of': 'Alicia'},
    {'name': 'Allie', 'variation_of': 'Alicia'},
    
    {'name': 'Amanda', 'variation_of': None},
    {'name': 'Mandy', 'variation_of': 'Amanda'},
    {'name': 'Amy', 'variation_of': 'Amanda'},
    
    {'name': 'Amy', 'variation_of': None},
    {'name': 'Ames', 'variation_of': 'Amy'},
    
    {'name': 'Andrea', 'variation_of': None},
    {'name': 'Andy', 'variation_of': 'Andrea'},
    {'name': 'Andie', 'variation_of': 'Andrea'},
    
    {'name': 'Angela', 'variation_of': None},
    {'name': 'Angie', 'variation_of': 'Angela'},
    {'name': 'Angel', 'variation_of': 'Angela'},
    
    {'name': 'Anna', 'variation_of': None},
    {'name': 'Annie', 'variation_of': 'Anna'},
    {'name': 'Ana', 'variation_of': 'Anna'},
    
    {'name': 'Anne', 'variation_of': None},
    {'name': 'Annie', 'variation_of': 'Anne'},
    {'name': 'Ann', 'variation_of': 'Anne'},
    
    {'name': 'Antonia', 'variation_of': None},
    {'name': 'Toni', 'variation_of': 'Antonia'},
    {'name': 'Tony', 'variation_of': 'Antonia'},
    
    {'name': 'Ashley', 'variation_of': None},
    {'name': 'Ash', 'variation_of': 'Ashley'},
    {'name': 'Ashe', 'variation_of': 'Ashley'},
    
    {'name': 'Audrey', 'variation_of': None},
    {'name': 'Audie', 'variation_of': 'Audrey'},
    
    # Female names starting with B
    {'name': 'Barbara', 'variation_of': None},
    {'name': 'Barb', 'variation_of': 'Barbara'},
    {'name': 'Barbie', 'variation_of': 'Barbara'},
    {'name': 'Babs', 'variation_of': 'Barbara'},
    
    {'name': 'Beatrice', 'variation_of': None},
    {'name': 'Bea', 'variation_of': 'Beatrice'},
    {'name': 'Beatie', 'variation_of': 'Beatrice'},
    
    {'name': 'Belinda', 'variation_of': None},
    {'name': 'Belle', 'variation_of': 'Belinda'},
    {'name': 'Linda', 'variation_of': 'Belinda'},
    
    {'name': 'Bernice', 'variation_of': None},
    {'name': 'Bernie', 'variation_of': 'Bernice'},
    
    {'name': 'Betty', 'variation_of': None},
    {'name': 'Bettie', 'variation_of': 'Betty'},
    
    {'name': 'Beverly', 'variation_of': None},
    {'name': 'Bev', 'variation_of': 'Beverly'},
    
    {'name': 'Bianca', 'variation_of': None},
    {'name': 'Bee', 'variation_of': 'Bianca'},
    
    {'name': 'Bridget', 'variation_of': None},
    {'name': 'Bridgie', 'variation_of': 'Bridget'},
    
    {'name': 'Brittany', 'variation_of': None},
    {'name': 'Brit', 'variation_of': 'Brittany'},
    {'name': 'Britt', 'variation_of': 'Brittany'},
    
    # Female names starting with C
    {'name': 'Camila', 'variation_of': None},
    {'name': 'Cami', 'variation_of': 'Camila'},
    
    {'name': 'Candace', 'variation_of': None},
    {'name': 'Candy', 'variation_of': 'Candace'},
    {'name': 'Candie', 'variation_of': 'Candace'},
    
    {'name': 'Carmen', 'variation_of': None},
    {'name': 'Carrie', 'variation_of': 'Carmen'},
    
    {'name': 'Caroline', 'variation_of': None},
    {'name': 'Carol', 'variation_of': 'Caroline'},
    {'name': 'Carrie', 'variation_of': 'Caroline'},
    {'name': 'Callie', 'variation_of': 'Caroline'},
    {'name': 'Carlyn', 'variation_of': 'Caroline'},
    
    {'name': 'Catherine', 'variation_of': None},
    {'name': 'Kate', 'variation_of': 'Catherine'},
    {'name': 'Katie', 'variation_of': 'Catherine'},
    {'name': 'Cathy', 'variation_of': 'Catherine'},
    {'name': 'Cat', 'variation_of': 'Catherine'},
    {'name': 'Kitty', 'variation_of': 'Catherine'},
    {'name': 'Cate', 'variation_of': 'Catherine'},
    
    {'name': 'Cecilia', 'variation_of': None},
    {'name': 'Ceci', 'variation_of': 'Cecilia'},
    {'name': 'Cece', 'variation_of': 'Cecilia'},
    
    {'name': 'Charlotte', 'variation_of': None},
    {'name': 'Charlie', 'variation_of': 'Charlotte'},
    {'name': 'Lottie', 'variation_of': 'Charlotte'},
    {'name': 'Char', 'variation_of': 'Charlotte'},
    
    {'name': 'Christina', 'variation_of': None},
    {'name': 'Chris', 'variation_of': 'Christina'},
    {'name': 'Christie', 'variation_of': 'Christina'},
    {'name': 'Tina', 'variation_of': 'Christina'},
    {'name': 'Chrissy', 'variation_of': 'Christina'},
    
    {'name': 'Christine', 'variation_of': None},
    {'name': 'Chris', 'variation_of': 'Christine'},
    {'name': 'Christie', 'variation_of': 'Christine'},
    {'name': 'Chrissy', 'variation_of': 'Christine'},
    
    {'name': 'Claire', 'variation_of': None},
    {'name': 'Clara', 'variation_of': 'Claire'},
    
    {'name': 'Claudia', 'variation_of': None},
    {'name': 'Claude', 'variation_of': 'Claudia'},
    
    {'name': 'Courtney', 'variation_of': None},
    {'name': 'Court', 'variation_of': 'Courtney'},
    
    {'name': 'Crystal', 'variation_of': None},
    {'name': 'Christy', 'variation_of': 'Crystal'},
    
    # Female names starting with D
    {'name': 'Danielle', 'variation_of': None},
    {'name': 'Dani', 'variation_of': 'Danielle'},
    {'name': 'Danny', 'variation_of': 'Danielle'},
    
    {'name': 'Deborah', 'variation_of': None},
    {'name': 'Debbie', 'variation_of': 'Deborah'},
    {'name': 'Deb', 'variation_of': 'Deborah'},
    {'name': 'Debby', 'variation_of': 'Deborah'},
    
    {'name': 'Denise', 'variation_of': None},
    {'name': 'Denny', 'variation_of': 'Denise'},
    
    {'name': 'Diana', 'variation_of': None},
    {'name': 'Di', 'variation_of': 'Diana'},
    {'name': 'Dee', 'variation_of': 'Diana'},
    
    {'name': 'Diane', 'variation_of': None},
    {'name': 'Di', 'variation_of': 'Diane'},
    {'name': 'Dee', 'variation_of': 'Diane'},
    
    {'name': 'Dolores', 'variation_of': None},
    {'name': 'Dolly', 'variation_of': 'Dolores'},
    {'name': 'Lola', 'variation_of': 'Dolores'},
    
    {'name': 'Donna', 'variation_of': None},
    {'name': 'Donnie', 'variation_of': 'Donna'},
    
    {'name': 'Dorothy', 'variation_of': None},
    {'name': 'Dot', 'variation_of': 'Dorothy'},
    {'name': 'Dotty', 'variation_of': 'Dorothy'},
    {'name': 'Dottie', 'variation_of': 'Dorothy'},
    
    # Female names starting with E
    {'name': 'Eleanor', 'variation_of': None},
    {'name': 'Ellie', 'variation_of': 'Eleanor'},
    {'name': 'Ella', 'variation_of': 'Eleanor'},
    {'name': 'Nell', 'variation_of': 'Eleanor'},
    {'name': 'Nellie', 'variation_of': 'Eleanor'},
    
    {'name': 'Elizabeth', 'variation_of': None},
    {'name': 'Liz', 'variation_of': 'Elizabeth'},
    {'name': 'Lizzie', 'variation_of': 'Elizabeth'},
    {'name': 'Beth', 'variation_of': 'Elizabeth'},
    {'name': 'Betty', 'variation_of': 'Elizabeth'},
    {'name': 'Eliza', 'variation_of': 'Elizabeth'},
    {'name': 'Lisa', 'variation_of': 'Elizabeth'},
    {'name': 'Libby', 'variation_of': 'Elizabeth'},
    {'name': 'Betsy', 'variation_of': 'Elizabeth'},
    {'name': 'Bess', 'variation_of': 'Elizabeth'},
    
    {'name': 'Emily', 'variation_of': None},
    {'name': 'Em', 'variation_of': 'Emily'},
    {'name': 'Emmy', 'variation_of': 'Emily'},
    {'name': 'Emmie', 'variation_of': 'Emily'},
    
    {'name': 'Emma', 'variation_of': None},
    {'name': 'Em', 'variation_of': 'Emma'},
    {'name': 'Emmy', 'variation_of': 'Emma'},
    
    {'name': 'Erica', 'variation_of': None},
    {'name': 'Rickie', 'variation_of': 'Erica'},
    
    {'name': 'Evelyn', 'variation_of': None},
    {'name': 'Eve', 'variation_of': 'Evelyn'},
    {'name': 'Evie', 'variation_of': 'Evelyn'},
    
    # Female names starting with F
    {'name': 'Faith', 'variation_of': None},
    
    {'name': 'Felicia', 'variation_of': None},
    {'name': 'Feli', 'variation_of': 'Felicia'},
    
    {'name': 'Florence', 'variation_of': None},
    {'name': 'Flo', 'variation_of': 'Florence'},
    {'name': 'Florrie', 'variation_of': 'Florence'},
    
    {'name': 'Frances', 'variation_of': None},
    {'name': 'Fran', 'variation_of': 'Frances'},
    {'name': 'Frannie', 'variation_of': 'Frances'},
    {'name': 'Fanny', 'variation_of': 'Frances'},
    
    # Female names starting with G
    {'name': 'Gabriela', 'variation_of': None},
    {'name': 'Gabi', 'variation_of': 'Gabriela'},
    {'name': 'Gabby', 'variation_of': 'Gabriela'},
    
    {'name': 'Gabrielle', 'variation_of': None},
    {'name': 'Gabi', 'variation_of': 'Gabrielle'},
    {'name': 'Gabby', 'variation_of': 'Gabrielle'},
    
    {'name': 'Georgia', 'variation_of': None},
    {'name': 'Georgie', 'variation_of': 'Georgia'},
    
    {'name': 'Gertrude', 'variation_of': None},
    {'name': 'Gertie', 'variation_of': 'Gertrude'},
    {'name': 'Trudy', 'variation_of': 'Gertrude'},
    
    {'name': 'Gloria', 'variation_of': None},
    {'name': 'Glory', 'variation_of': 'Gloria'},
    
    {'name': 'Grace', 'variation_of': None},
    {'name': 'Gracie', 'variation_of': 'Grace'},
    
    {'name': 'Guadalupe', 'variation_of': None},
    {'name': 'Lupe', 'variation_of': 'Guadalupe'},
    
    # Female names starting with H
    {'name': 'Hannah', 'variation_of': None},
    {'name': 'Anna', 'variation_of': 'Hannah'},
    
    {'name': 'Heather', 'variation_of': None},
    {'name': 'Heath', 'variation_of': 'Heather'},
    
    {'name': 'Helen', 'variation_of': None},
    {'name': 'Nell', 'variation_of': 'Helen'},
    {'name': 'Nellie', 'variation_of': 'Helen'},
    {'name': 'Lena', 'variation_of': 'Helen'},
    
    {'name': 'Hope', 'variation_of': None},
    
    # Female names starting with I
    {'name': 'Irene', 'variation_of': None},
    {'name': 'Renie', 'variation_of': 'Irene'},
    
    {'name': 'Isabella', 'variation_of': None},
    {'name': 'Bella', 'variation_of': 'Isabella'},
    {'name': 'Izzy', 'variation_of': 'Isabella'},
    {'name': 'Belle', 'variation_of': 'Isabella'},
    {'name': 'Isa', 'variation_of': 'Isabella'},
    
    # Female names starting with J
    {'name': 'Jacqueline', 'variation_of': None},
    {'name': 'Jackie', 'variation_of': 'Jacqueline'},
    {'name': 'Jack', 'variation_of': 'Jacqueline'},
    
    {'name': 'Janet', 'variation_of': None},
    {'name': 'Jan', 'variation_of': 'Janet'},
    
    {'name': 'Jasmine', 'variation_of': None},
    {'name': 'Jazz', 'variation_of': 'Jasmine'},
    
    {'name': 'Jean', 'variation_of': None},
    {'name': 'Jeanie', 'variation_of': 'Jean'},
    
    {'name': 'Jennifer', 'variation_of': None},
    {'name': 'Jen', 'variation_of': 'Jennifer'},
    {'name': 'Jenny', 'variation_of': 'Jennifer'},
    {'name': 'Jenn', 'variation_of': 'Jennifer'},
    
    {'name': 'Jessica', 'variation_of': None},
    {'name': 'Jess', 'variation_of': 'Jessica'},
    {'name': 'Jessie', 'variation_of': 'Jessica'},
    
    {'name': 'Jill', 'variation_of': None},
    {'name': 'Jilly', 'variation_of': 'Jill'},
    
    {'name': 'Joan', 'variation_of': None},
    {'name': 'Joanie', 'variation_of': 'Joan'},
    
    {'name': 'Joanna', 'variation_of': None},
    {'name': 'Jo', 'variation_of': 'Joanna'},
    {'name': 'Joey', 'variation_of': 'Joanna'},
    
    {'name': 'Josephine', 'variation_of': None},
    {'name': 'Jo', 'variation_of': 'Josephine'},
    {'name': 'Joey', 'variation_of': 'Josephine'},
    {'name': 'Josie', 'variation_of': 'Josephine'},
    
    {'name': 'Joy', 'variation_of': None},
    
    {'name': 'Joyce', 'variation_of': None},
    
    {'name': 'Judith', 'variation_of': None},
    {'name': 'Judy', 'variation_of': 'Judith'},
    {'name': 'Judi', 'variation_of': 'Judith'},
    
    {'name': 'Julia', 'variation_of': None},
    {'name': 'Julie', 'variation_of': 'Julia'},
    {'name': 'Jules', 'variation_of': 'Julia'},
    
    {'name': 'June', 'variation_of': None},
    {'name': 'Junie', 'variation_of': 'June'},
    
    # Female names starting with K
    {'name': 'Karen', 'variation_of': None},
    {'name': 'Kari', 'variation_of': 'Karen'},
    
    {'name': 'Katherine', 'variation_of': None},
    {'name': 'Kate', 'variation_of': 'Katherine'},
    {'name': 'Katie', 'variation_of': 'Katherine'},
    {'name': 'Kathy', 'variation_of': 'Katherine'},
    {'name': 'Kay', 'variation_of': 'Katherine'},
    {'name': 'Kit', 'variation_of': 'Katherine'},
    {'name': 'Kitty', 'variation_of': 'Katherine'},
    
    {'name': 'Kimberly', 'variation_of': None},
    {'name': 'Kim', 'variation_of': 'Kimberly'},
    {'name': 'Kimmy', 'variation_of': 'Kimberly'},
    
    {'name': 'Kristen', 'variation_of': None},
    {'name': 'Kris', 'variation_of': 'Kristen'},
    {'name': 'Kristy', 'variation_of': 'Kristen'},
    
    # Female names starting with L
    {'name': 'Laura', 'variation_of': None},
    {'name': 'Laurie', 'variation_of': 'Laura'},
    
    {'name': 'Lauren', 'variation_of': None},
    {'name': 'Laurie', 'variation_of': 'Lauren'},
    
    {'name': 'Leslie', 'variation_of': None},
    {'name': 'Les', 'variation_of': 'Leslie'},
    
    {'name': 'Linda', 'variation_of': None},
    {'name': 'Lindy', 'variation_of': 'Linda'},
    {'name': 'Lynn', 'variation_of': 'Linda'},
    
    {'name': 'Lisa', 'variation_of': None},
    {'name': 'Lee', 'variation_of': 'Lisa'},
    
    {'name': 'Lori', 'variation_of': None},
    {'name': 'Lor', 'variation_of': 'Lori'},
    
    {'name': 'Louise', 'variation_of': None},
    {'name': 'Lou', 'variation_of': 'Louise'},
    {'name': 'Louie', 'variation_of': 'Louise'},
    
    {'name': 'Lucia', 'variation_of': None},
    {'name': 'Lucy', 'variation_of': 'Lucia'},
    
    {'name': 'Lucy', 'variation_of': None},
    {'name': 'Lu', 'variation_of': 'Lucy'},
    
    # Female names starting with M
    {'name': 'Madison', 'variation_of': None},
    {'name': 'Maddie', 'variation_of': 'Madison'},
    {'name': 'Maddy', 'variation_of': 'Madison'},
    
    {'name': 'Margaret', 'variation_of': None},
    {'name': 'Maggie', 'variation_of': 'Margaret'},
    {'name': 'Meg', 'variation_of': 'Margaret'},
    {'name': 'Peggy', 'variation_of': 'Margaret'},
    {'name': 'Margie', 'variation_of': 'Margaret'},
    {'name': 'Marge', 'variation_of': 'Margaret'},
    {'name': 'Rita', 'variation_of': 'Margaret'},
    
    {'name': 'Maria', 'variation_of': None},
    {'name': 'Mari', 'variation_of': 'Maria'},
    
    {'name': 'Marie', 'variation_of': None},
    {'name': 'Mari', 'variation_of': 'Marie'},
    
    {'name': 'Martha', 'variation_of': None},
    {'name': 'Marty', 'variation_of': 'Martha'},
    {'name': 'Mattie', 'variation_of': 'Martha'},
    
    {'name': 'Mary', 'variation_of': None},
    {'name': 'Mare', 'variation_of': 'Mary'},
    {'name': 'Molly', 'variation_of': 'Mary'},
    
    {'name': 'Megan', 'variation_of': None},
    {'name': 'Meg', 'variation_of': 'Megan'},
    {'name': 'Meggie', 'variation_of': 'Megan'},
    
    {'name': 'Melissa', 'variation_of': None},
    {'name': 'Mel', 'variation_of': 'Melissa'},
    {'name': 'Missy', 'variation_of': 'Melissa'},
    
    {'name': 'Michelle', 'variation_of': None},
    {'name': 'Mish', 'variation_of': 'Michelle'},
    {'name': 'Mickey', 'variation_of': 'Michelle'},
    {'name': 'Shelly', 'variation_of': 'Michelle'},
    
    {'name': 'Monica', 'variation_of': None},
    {'name': 'Moni', 'variation_of': 'Monica'},
    
    # Female names starting with N
    {'name': 'Nancy', 'variation_of': None},
    {'name': 'Nan', 'variation_of': 'Nancy'},
    {'name': 'Nance', 'variation_of': 'Nancy'},
    
    {'name': 'Natalie', 'variation_of': None},
    {'name': 'Nat', 'variation_of': 'Natalie'},
    {'name': 'Nattie', 'variation_of': 'Natalie'},
    
    {'name': 'Nicole', 'variation_of': None},
    {'name': 'Nicky', 'variation_of': 'Nicole'},
    {'name': 'Nikki', 'variation_of': 'Nicole'},
    {'name': 'Cole', 'variation_of': 'Nicole'},
    
    # Female names starting with O
    {'name': 'Olivia', 'variation_of': None},
    {'name': 'Liv', 'variation_of': 'Olivia'},
    {'name': 'Livvy', 'variation_of': 'Olivia'},
    {'name': 'Ollie', 'variation_of': 'Olivia'},
    
    # Female names starting with P
    {'name': 'Pamela', 'variation_of': None},
    {'name': 'Pam', 'variation_of': 'Pamela'},
    {'name': 'Pammy', 'variation_of': 'Pamela'},
    
    {'name': 'Patricia', 'variation_of': None},
    {'name': 'Pat', 'variation_of': 'Patricia'},
    {'name': 'Patty', 'variation_of': 'Patricia'},
    {'name': 'Tricia', 'variation_of': 'Patricia'},
    {'name': 'Patsy', 'variation_of': 'Patricia'},
    
    {'name': 'Paula', 'variation_of': None},
    {'name': 'Paulie', 'variation_of': 'Paula'},
    
    {'name': 'Penelope', 'variation_of': None},
    {'name': 'Penny', 'variation_of': 'Penelope'},
    
    {'name': 'Priscilla', 'variation_of': None},
    {'name': 'Pris', 'variation_of': 'Priscilla'},
    {'name': 'Prissy', 'variation_of': 'Priscilla'},
    
    # Female names starting with R
    {'name': 'Rachel', 'variation_of': None},
    {'name': 'Rae', 'variation_of': 'Rachel'},
    {'name': 'Rach', 'variation_of': 'Rachel'},
    
    {'name': 'Rebecca', 'variation_of': None},
    {'name': 'Becky', 'variation_of': 'Rebecca'},
    {'name': 'Becca', 'variation_of': 'Rebecca'},
    {'name': 'Beck', 'variation_of': 'Rebecca'},
    
    {'name': 'Regina', 'variation_of': None},
    {'name': 'Gina', 'variation_of': 'Regina'},
    
    {'name': 'Robin', 'variation_of': None},
    {'name': 'Robbie', 'variation_of': 'Robin'},
    
    {'name': 'Rose', 'variation_of': None},
    {'name': 'Rosie', 'variation_of': 'Rose'},
    
    {'name': 'Ruth', 'variation_of': None},
    {'name': 'Ruthie', 'variation_of': 'Ruth'},
    
    # Female names starting with S
    {'name': 'Samantha', 'variation_of': None},
    {'name': 'Sam', 'variation_of': 'Samantha'},
    {'name': 'Sammy', 'variation_of': 'Samantha'},
    
    {'name': 'Sandra', 'variation_of': None},
    {'name': 'Sandy', 'variation_of': 'Sandra'},
    
    {'name': 'Sarah', 'variation_of': None},
    {'name': 'Sara', 'variation_of': 'Sarah'},
    {'name': 'Sally', 'variation_of': 'Sarah'},
    
    {'name': 'Sharon', 'variation_of': None},
    {'name': 'Shari', 'variation_of': 'Sharon'},
    
    {'name': 'Stephanie', 'variation_of': None},
    {'name': 'Steph', 'variation_of': 'Stephanie'},
    {'name': 'Steffi', 'variation_of': 'Stephanie'},
    {'name': 'Stephy', 'variation_of': 'Stephanie'},
    
    {'name': 'Susan', 'variation_of': None},
    {'name': 'Sue', 'variation_of': 'Susan'},
    {'name': 'Susie', 'variation_of': 'Susan'},
    {'name': 'Suzy', 'variation_of': 'Susan'},
    {'name': 'Suzie', 'variation_of': 'Susan'},
    
    {'name': 'Suzanne', 'variation_of': None},
    {'name': 'Suzy', 'variation_of': 'Suzanne'},
    {'name': 'Sue', 'variation_of': 'Suzanne'},
    
    {'name': 'Sylvia', 'variation_of': None},
    {'name': 'Syl', 'variation_of': 'Sylvia'},
    
    # Female names starting with T
    {'name': 'Tamara', 'variation_of': None},
    {'name': 'Tammy', 'variation_of': 'Tamara'},
    {'name': 'Tam', 'variation_of': 'Tamara'},
    
    {'name': 'Teresa', 'variation_of': None},
    {'name': 'Terry', 'variation_of': 'Teresa'},
    {'name': 'Teri', 'variation_of': 'Teresa'},
    {'name': 'Tess', 'variation_of': 'Teresa'},
    
    {'name': 'Theresa', 'variation_of': None},
    {'name': 'Terry', 'variation_of': 'Theresa'},
    {'name': 'Teri', 'variation_of': 'Theresa'},
    {'name': 'Tess', 'variation_of': 'Theresa'},
    
    {'name': 'Tiffany', 'variation_of': None},
    {'name': 'Tiff', 'variation_of': 'Tiffany'},
    
    {'name': 'Tracy', 'variation_of': None},
    {'name': 'Trace', 'variation_of': 'Tracy'},
    
    # Female names starting with V
    {'name': 'Valerie', 'variation_of': None},
    {'name': 'Val', 'variation_of': 'Valerie'},
    
    {'name': 'Vanessa', 'variation_of': None},
    {'name': 'Nessa', 'variation_of': 'Vanessa'},
    {'name': 'Van', 'variation_of': 'Vanessa'},
    
    {'name': 'Veronica', 'variation_of': None},
    {'name': 'Ronnie', 'variation_of': 'Veronica'},
    {'name': 'Roni', 'variation_of': 'Veronica'},
    
    {'name': 'Victoria', 'variation_of': None},
    {'name': 'Vicky', 'variation_of': 'Victoria'},
    {'name': 'Vic', 'variation_of': 'Victoria'},
    {'name': 'Tori', 'variation_of': 'Victoria'},
    
    {'name': 'Virginia', 'variation_of': None},
    {'name': 'Ginny', 'variation_of': 'Virginia'},
    {'name': 'Ginger', 'variation_of': 'Virginia'},
    
    # Female names starting with W
    {'name': 'Wendy', 'variation_of': None},
    {'name': 'Wen', 'variation_of': 'Wendy'},
    
    # Unisex/International names
    {'name': 'Angel', 'variation_of': None},
    {'name': 'Angelito', 'variation_of': 'Angel'},
    
    {'name': 'Casey', 'variation_of': None},
    {'name': 'Case', 'variation_of': 'Casey'},
    
    {'name': 'Drew', 'variation_of': None},
    
    {'name': 'Jaime', 'variation_of': None},
    {'name': 'Jamie', 'variation_of': 'Jaime'},
    
    {'name': 'Jordan', 'variation_of': None},
    {'name': 'Jordy', 'variation_of': 'Jordan'},
    
    {'name': 'Kelly', 'variation_of': None},
    
    {'name': 'Morgan', 'variation_of': None},
    
    {'name': 'Riley', 'variation_of': None},
    
    {'name': 'Taylor', 'variation_of': None},
    {'name': 'Tay', 'variation_of': 'Taylor'},
    
    # Asian Names - Chinese
    {'name': 'Wei', 'variation_of': None},
    {'name': 'Wayne', 'variation_of': 'Wei'},
    
    {'name': 'Li', 'variation_of': None},
    {'name': 'Lee', 'variation_of': 'Li'},
    
    {'name': 'Ming', 'variation_of': None},
    
    {'name': 'Jie', 'variation_of': None},
    {'name': 'Jay', 'variation_of': 'Jie'},
    
    {'name': 'Lei', 'variation_of': None},
    {'name': 'Ray', 'variation_of': 'Lei'},
    
    {'name': 'Ling', 'variation_of': None},
    {'name': 'Lynn', 'variation_of': 'Ling'},
    
    {'name': 'Xin', 'variation_of': None},
    {'name': 'Sean', 'variation_of': 'Xin'},
    
    {'name': 'Yu', 'variation_of': None},
    {'name': 'Jade', 'variation_of': 'Yu'},
    
    {'name': 'Chen', 'variation_of': None},
    {'name': 'Ken', 'variation_of': 'Chen'},
    
    {'name': 'Qiang', 'variation_of': None},
    {'name': 'John', 'variation_of': 'Qiang'},
    
    # Asian Names - Japanese
    {'name': 'Hiroshi', 'variation_of': None},
    {'name': 'Hiro', 'variation_of': 'Hiroshi'},
    
    {'name': 'Takeshi', 'variation_of': None},
    {'name': 'Take', 'variation_of': 'Takeshi'},
    
    {'name': 'Akira', 'variation_of': None},
    {'name': 'Aki', 'variation_of': 'Akira'},
    
    {'name': 'Kenji', 'variation_of': None},
    {'name': 'Ken', 'variation_of': 'Kenji'},
    
    {'name': 'Yuki', 'variation_of': None},
    
    {'name': 'Satoshi', 'variation_of': None},
    {'name': 'Sato', 'variation_of': 'Satoshi'},
    
    {'name': 'Kazuki', 'variation_of': None},
    {'name': 'Kaz', 'variation_of': 'Kazuki'},
    
    {'name': 'Haruto', 'variation_of': None},
    {'name': 'Harry', 'variation_of': 'Haruto'},
    
    {'name': 'Sakura', 'variation_of': None},
    {'name': 'Saki', 'variation_of': 'Sakura'},
    
    {'name': 'Yui', 'variation_of': None},
    
    {'name': 'Emi', 'variation_of': None},
    {'name': 'Emmy', 'variation_of': 'Emi'},
    
    {'name': 'Aiko', 'variation_of': None},
    {'name': 'Ai', 'variation_of': 'Aiko'},
    
    {'name': 'Miki', 'variation_of': None},
    {'name': 'Mickey', 'variation_of': 'Miki'},
    
    # Asian Names - Korean
    {'name': 'Jihoon', 'variation_of': None},
    {'name': 'Jimmy', 'variation_of': 'Jihoon'},
    
    {'name': 'Minho', 'variation_of': None},
    {'name': 'Min', 'variation_of': 'Minho'},
    
    {'name': 'Seunghyun', 'variation_of': None},
    {'name': 'Sean', 'variation_of': 'Seunghyun'},
    
    {'name': 'Jisoo', 'variation_of': None},
    {'name': 'Jessie', 'variation_of': 'Jisoo'},
    
    {'name': 'Hyunjin', 'variation_of': None},
    {'name': 'Jin', 'variation_of': 'Hyunjin'},
    
    {'name': 'Soyeon', 'variation_of': None},
    {'name': 'Sophie', 'variation_of': 'Soyeon'},
    
    {'name': 'Minji', 'variation_of': None},
    {'name': 'Minnie', 'variation_of': 'Minji'},
    
    # Asian Names - Indian/Hindi
    {'name': 'Arjun', 'variation_of': None},
    {'name': 'Arj', 'variation_of': 'Arjun'},
    
    {'name': 'Raj', 'variation_of': None},
    {'name': 'Rajesh', 'variation_of': 'Raj'},
    
    {'name': 'Vikram', 'variation_of': None},
    {'name': 'Vik', 'variation_of': 'Vikram'},
    
    {'name': 'Suresh', 'variation_of': None},
    {'name': 'Suri', 'variation_of': 'Suresh'},
    
    {'name': 'Anand', 'variation_of': None},
    {'name': 'Andy', 'variation_of': 'Anand'},
    
    {'name': 'Priya', 'variation_of': None},
    {'name': 'Pri', 'variation_of': 'Priya'},
    
    {'name': 'Aisha', 'variation_of': None},
    {'name': 'Ash', 'variation_of': 'Aisha'},
    
    {'name': 'Kavita', 'variation_of': None},
    {'name': 'Kavi', 'variation_of': 'Kavita'},
    
    {'name': 'Neha', 'variation_of': None},
    {'name': 'Neh', 'variation_of': 'Neha'},
    
    {'name': 'Rohit', 'variation_of': None},
    {'name': 'Ro', 'variation_of': 'Rohit'},
    
    {'name': 'Deepak', 'variation_of': None},
    {'name': 'Deep', 'variation_of': 'Deepak'},
    
    {'name': 'Manish', 'variation_of': None},
    {'name': 'Mani', 'variation_of': 'Manish'},
    
    # European Names - French
    {'name': 'Pierre', 'variation_of': None},
    {'name': 'Pete', 'variation_of': 'Pierre'},
    
    {'name': 'Jean', 'variation_of': None},
    {'name': 'Johnny', 'variation_of': 'Jean'},
    
    {'name': 'François', 'variation_of': None},
    {'name': 'Frank', 'variation_of': 'François'},
    
    {'name': 'Antoine', 'variation_of': None},
    {'name': 'Tony', 'variation_of': 'Antoine'},
    
    {'name': 'Nicolas', 'variation_of': None},
    {'name': 'Nick', 'variation_of': 'Nicolas'},
    
    {'name': 'Marie', 'variation_of': None},
    {'name': 'Mari', 'variation_of': 'Marie'},
    
    {'name': 'Isabelle', 'variation_of': None},
    {'name': 'Izzy', 'variation_of': 'Isabelle'},
    {'name': 'Belle', 'variation_of': 'Isabelle'},
    
    {'name': 'Sophie', 'variation_of': None},
    {'name': 'Soph', 'variation_of': 'Sophie'},
    
    {'name': 'Chloé', 'variation_of': None},
    {'name': 'Chloe', 'variation_of': 'Chloé'},
    
    {'name': 'Amélie', 'variation_of': None},
    {'name': 'Amy', 'variation_of': 'Amélie'},
    
    {'name': 'Camille', 'variation_of': None},
    {'name': 'Cami', 'variation_of': 'Camille'},
    
    # European Names - German
    {'name': 'Klaus', 'variation_of': None},
    {'name': 'Claus', 'variation_of': 'Klaus'},
    
    {'name': 'Wilhelm', 'variation_of': None},
    {'name': 'Will', 'variation_of': 'Wilhelm'},
    {'name': 'Willy', 'variation_of': 'Wilhelm'},
    
    {'name': 'Heinrich', 'variation_of': None},
    {'name': 'Henry', 'variation_of': 'Heinrich'},
    {'name': 'Heinz', 'variation_of': 'Heinrich'},
    
    {'name': 'Friedrich', 'variation_of': None},
    {'name': 'Fritz', 'variation_of': 'Friedrich'},
    {'name': 'Fred', 'variation_of': 'Friedrich'},
    
    {'name': 'Johann', 'variation_of': None},
    {'name': 'Hans', 'variation_of': 'Johann'},
    
    {'name': 'Gretchen', 'variation_of': None},
    {'name': 'Greta', 'variation_of': 'Gretchen'},
    
    {'name': 'Ingrid', 'variation_of': None},
    {'name': 'Inga', 'variation_of': 'Ingrid'},
    
    {'name': 'Ursula', 'variation_of': None},
    {'name': 'Urs', 'variation_of': 'Ursula'},
    
    # European Names - Italian
    {'name': 'Giuseppe', 'variation_of': None},
    {'name': 'Joe', 'variation_of': 'Giuseppe'},
    {'name': 'Beppe', 'variation_of': 'Giuseppe'},
    
    {'name': 'Giovanni', 'variation_of': None},
    {'name': 'Gio', 'variation_of': 'Giovanni'},
    {'name': 'Johnny', 'variation_of': 'Giovanni'},
    
    {'name': 'Antonio', 'variation_of': None},
    {'name': 'Tony', 'variation_of': 'Antonio'},
    {'name': 'Tonio', 'variation_of': 'Antonio'},
    
    {'name': 'Francesco', 'variation_of': None},
    {'name': 'Franco', 'variation_of': 'Francesco'},
    {'name': 'Frank', 'variation_of': 'Francesco'},
    
    {'name': 'Marco', 'variation_of': None},
    {'name': 'Mark', 'variation_of': 'Marco'},
    
    {'name': 'Giulia', 'variation_of': None},
    {'name': 'Julie', 'variation_of': 'Giulia'},
    
    {'name': 'Francesca', 'variation_of': None},
    {'name': 'Fran', 'variation_of': 'Francesca'},
    {'name': 'Frankie', 'variation_of': 'Francesca'},
    
    {'name': 'Chiara', 'variation_of': None},
    {'name': 'Clara', 'variation_of': 'Chiara'},
    
    {'name': 'Valentina', 'variation_of': None},
    {'name': 'Val', 'variation_of': 'Valentina'},
    {'name': 'Tina', 'variation_of': 'Valentina'},
    
    # European Names - Spanish
    {'name': 'Alejandro', 'variation_of': None},
    {'name': 'Alex', 'variation_of': 'Alejandro'},
    {'name': 'Alejo', 'variation_of': 'Alejandro'},
    
    {'name': 'Sebastián', 'variation_of': None},
    {'name': 'Seb', 'variation_of': 'Sebastián'},
    {'name': 'Sebas', 'variation_of': 'Sebastián'},
    
    {'name': 'Mateo', 'variation_of': None},
    {'name': 'Matt', 'variation_of': 'Mateo'},
    {'name': 'Mati', 'variation_of': 'Mateo'},
    
    {'name': 'Sofía', 'variation_of': None},
    {'name': 'Sofi', 'variation_of': 'Sofía'},
    {'name': 'Sophie', 'variation_of': 'Sofía'},
    
    {'name': 'Valentina', 'variation_of': None},
    {'name': 'Vale', 'variation_of': 'Valentina'},
    
    {'name': 'Camila', 'variation_of': None},
    {'name': 'Cami', 'variation_of': 'Camila'},
    
    {'name': 'Isabella', 'variation_of': None},
    {'name': 'Isa', 'variation_of': 'Isabella'},
    {'name': 'Bella', 'variation_of': 'Isabella'},
    
    # European Names - Scandinavian
    {'name': 'Erik', 'variation_of': None},
    {'name': 'Eric', 'variation_of': 'Erik'},
    
    {'name': 'Lars', 'variation_of': None},
    {'name': 'Larry', 'variation_of': 'Lars'},
    
    {'name': 'Nils', 'variation_of': None},
    {'name': 'Nick', 'variation_of': 'Nils'},
    
    {'name': 'Björn', 'variation_of': None},
    {'name': 'Bjorn', 'variation_of': 'Björn'},
    
    {'name': 'Magnus', 'variation_of': None},
    {'name': 'Max', 'variation_of': 'Magnus'},
    
    {'name': 'Astrid', 'variation_of': None},
    {'name': 'Asta', 'variation_of': 'Astrid'},
    
    {'name': 'Ingrid', 'variation_of': None},
    {'name': 'Inga', 'variation_of': 'Ingrid'},
    
    {'name': 'Sigrid', 'variation_of': None},
    {'name': 'Sig', 'variation_of': 'Sigrid'},
    
    {'name': 'Annika', 'variation_of': None},
    {'name': 'Anna', 'variation_of': 'Annika'},
    {'name': 'Annie', 'variation_of': 'Annika'},
    
    # European Names - Eastern European/Russian
    {'name': 'Vladimir', 'variation_of': None},
    {'name': 'Vlad', 'variation_of': 'Vladimir'},
    {'name': 'Volodya', 'variation_of': 'Vladimir'},
    
    {'name': 'Dmitri', 'variation_of': None},
    {'name': 'Dima', 'variation_of': 'Dmitri'},
    
    {'name': 'Aleksandr', 'variation_of': None},
    {'name': 'Sasha', 'variation_of': 'Aleksandr'},
    {'name': 'Alex', 'variation_of': 'Aleksandr'},
    
    {'name': 'Mikhail', 'variation_of': None},
    {'name': 'Misha', 'variation_of': 'Mikhail'},
    {'name': 'Mike', 'variation_of': 'Mikhail'},
    
    {'name': 'Nikolai', 'variation_of': None},
    {'name': 'Kolya', 'variation_of': 'Nikolai'},
    {'name': 'Nick', 'variation_of': 'Nikolai'},
    
    {'name': 'Anastasia', 'variation_of': None},
    {'name': 'Nastya', 'variation_of': 'Anastasia'},
    {'name': 'Anna', 'variation_of': 'Anastasia'},
    {'name': 'Stacy', 'variation_of': 'Anastasia'},
    
    {'name': 'Ekaterina', 'variation_of': None},
    {'name': 'Katya', 'variation_of': 'Ekaterina'},
    {'name': 'Kate', 'variation_of': 'Ekaterina'},
    
    {'name': 'Yelena', 'variation_of': None},
    {'name': 'Lena', 'variation_of': 'Yelena'},
    {'name': 'Helen', 'variation_of': 'Yelena'},
    
    {'name': 'Svetlana', 'variation_of': None},
    {'name': 'Sveta', 'variation_of': 'Svetlana'},
    
    # Middle Eastern Names - Arabic
    {'name': 'Muhammad', 'variation_of': None},
    {'name': 'Mohammed', 'variation_of': 'Muhammad'},
    {'name': 'Ahmad', 'variation_of': 'Muhammad'},
    
    {'name': 'Ali', 'variation_of': None},
    {'name': 'Allie', 'variation_of': 'Ali'},
    
    {'name': 'Omar', 'variation_of': None},
    {'name': 'Umar', 'variation_of': 'Omar'},
    
    {'name': 'Hassan', 'variation_of': None},
    {'name': 'Hasan', 'variation_of': 'Hassan'},
    
    {'name': 'Ahmed', 'variation_of': None},
    {'name': 'Ahmad', 'variation_of': 'Ahmed'},
    
    {'name': 'Fatima', 'variation_of': None},
    {'name': 'Fati', 'variation_of': 'Fatima'},
    
    {'name': 'Aisha', 'variation_of': None},
    {'name': 'Aysha', 'variation_of': 'Aisha'},
    
    {'name': 'Khadija', 'variation_of': None},
    {'name': 'Kadi', 'variation_of': 'Khadija'},
    
    {'name': 'Amina', 'variation_of': None},
    {'name': 'Mina', 'variation_of': 'Amina'},
    
    # Middle Eastern Names - Hebrew
    {'name': 'David', 'variation_of': None},
    {'name': 'Dov', 'variation_of': 'David'},
    
    {'name': 'Michael', 'variation_of': None},
    {'name': 'Micha', 'variation_of': 'Michael'},
    
    {'name': 'Benjamin', 'variation_of': None},
    {'name': 'Benny', 'variation_of': 'Benjamin'},
    
    {'name': 'Sarah', 'variation_of': None},
    {'name': 'Sara', 'variation_of': 'Sarah'},
    
    {'name': 'Rachel', 'variation_of': None},
    {'name': 'Rachelle', 'variation_of': 'Rachel'},
    
    {'name': 'Rebecca', 'variation_of': None},
    {'name': 'Rivka', 'variation_of': 'Rebecca'},
    
    {'name': 'Miriam', 'variation_of': None},
    {'name': 'Miri', 'variation_of': 'Miriam'},
    
    # African Names
    {'name': 'Kwame', 'variation_of': None},
    {'name': 'Kwamé', 'variation_of': 'Kwame'},
    
    {'name': 'Kofi', 'variation_of': None},
    {'name': 'Coffee', 'variation_of': 'Kofi'},
    
    {'name': 'Amara', 'variation_of': None},
    {'name': 'Mara', 'variation_of': 'Amara'},
    
    {'name': 'Zara', 'variation_of': None},
    {'name': 'Zahra', 'variation_of': 'Zara'},
    
    {'name': 'Jelani', 'variation_of': None},
    {'name': 'Jel', 'variation_of': 'Jelani'},
    
    {'name': 'Nia', 'variation_of': None},
    
    {'name': 'Kesi', 'variation_of': None},
    {'name': 'Kess', 'variation_of': 'Kesi'},
    
    {'name': 'Amina', 'variation_of': None},
    {'name': 'Aminah', 'variation_of': 'Amina'},
    
    # Celtic/Irish Names
    {'name': 'Seán', 'variation_of': None},
    {'name': 'Sean', 'variation_of': 'Seán'},
    {'name': 'Shane', 'variation_of': 'Seán'},
    
    {'name': 'Pádraig', 'variation_of': None},
    {'name': 'Patrick', 'variation_of': 'Pádraig'},
    {'name': 'Paddy', 'variation_of': 'Pádraig'},
    
    {'name': 'Cian', 'variation_of': None},
    {'name': 'Kian', 'variation_of': 'Cian'},
    
    {'name': 'Siobhan', 'variation_of': None},
    {'name': 'Shevaun', 'variation_of': 'Siobhan'},
    {'name': 'Joan', 'variation_of': 'Siobhan'},
    
    {'name': 'Niamh', 'variation_of': None},
    {'name': 'Neve', 'variation_of': 'Niamh'},
    
    {'name': 'Aoife', 'variation_of': None},
    {'name': 'Eva', 'variation_of': 'Aoife'},
    
    {'name': 'Saoirse', 'variation_of': None},
    {'name': 'Sersha', 'variation_of': 'Saoirse'},
    
    # Portuguese/Brazilian Names
    {'name': 'João', 'variation_of': None},
    {'name': 'John', 'variation_of': 'João'},
    {'name': 'Johnny', 'variation_of': 'João'},
    
    {'name': 'Carlos', 'variation_of': None},
    {'name': 'Carlinhos', 'variation_of': 'Carlos'},
    
    {'name': 'Luís', 'variation_of': None},
    {'name': 'Luis', 'variation_of': 'Luís'},
    {'name': 'Luiz', 'variation_of': 'Luís'},
    
    {'name': 'Ana', 'variation_of': None},
    {'name': 'Aninha', 'variation_of': 'Ana'},
    
    {'name': 'Maria', 'variation_of': None},
    {'name': 'Mariazinha', 'variation_of': 'Maria'},
    
    {'name': 'Fernanda', 'variation_of': None},
    {'name': 'Nanda', 'variation_of': 'Fernanda'},
    
    # Turkish Names
    {'name': 'Mehmet', 'variation_of': None},
    {'name': 'Metin', 'variation_of': 'Mehmet'},
    
    {'name': 'Mustafa', 'variation_of': None},
    {'name': 'Mus', 'variation_of': 'Mustafa'},
    
    {'name': 'Ayşe', 'variation_of': None},
    {'name': 'Aysha', 'variation_of': 'Ayşe'},
    
    {'name': 'Fatma', 'variation_of': None},
    {'name': 'Fati', 'variation_of': 'Fatma'},
    
    # Persian Names
    {'name': 'Darius', 'variation_of': None},
    {'name': 'Dario', 'variation_of': 'Darius'},
    
    {'name': 'Cyrus', 'variation_of': None},
    {'name': 'Cy', 'variation_of': 'Cyrus'},
    
    {'name': 'Yasmin', 'variation_of': None},
    {'name': 'Jasmine', 'variation_of': 'Yasmin'},
    
    {'name': 'Reza', 'variation_of': None},
    {'name': 'Rex', 'variation_of': 'Reza'},
    
    # Thai Names
    {'name': 'Somchai', 'variation_of': None},
    {'name': 'Som', 'variation_of': 'Somchai'},
    
    {'name': 'Niran', 'variation_of': None},
    {'name': 'Nira', 'variation_of': 'Niran'},
    
    {'name': 'Siriporn', 'variation_of': None},
    {'name': 'Siri', 'variation_of': 'Siriporn'},
    
    # Vietnamese Names
    {'name': 'Nguyen', 'variation_of': None},
    {'name': 'Win', 'variation_of': 'Nguyen'},
    
    {'name': 'Linh', 'variation_of': None},
    {'name': 'Lynn', 'variation_of': 'Linh'},
    
    {'name': 'Minh', 'variation_of': None},
    {'name': 'Min', 'variation_of': 'Minh'},
    
    # Filipino Names
    {'name': 'Jose', 'variation_of': None},
    {'name': 'Joey', 'variation_of': 'Jose'},
    
    {'name': 'Maria', 'variation_of': None},
    {'name': 'Ria', 'variation_of': 'Maria'},
    
    {'name': 'Antonio', 'variation_of': None},
    {'name': 'Toni', 'variation_of': 'Antonio'},
    
    {'name': 'Esperanza', 'variation_of': None},
    {'name': 'Espe', 'variation_of': 'Esperanza'},
    {'name': 'Hope', 'variation_of': 'Esperanza'},
    
    # Additional English/American Names
    {'name': 'Abigail', 'variation_of': None},
    {'name': 'Abbie', 'variation_of': 'Abigail'},
    
    {'name': 'Adam', 'variation_of': None},
    {'name': 'Addie', 'variation_of': 'Adam'},
    
    {'name': 'Adrian', 'variation_of': None},
    {'name': 'Addie', 'variation_of': 'Adrian'},
    
    {'name': 'Aiden', 'variation_of': None},
    {'name': 'Aidan', 'variation_of': 'Aiden'},
    
    {'name': 'Allison', 'variation_of': None},
    {'name': 'Allie', 'variation_of': 'Allison'},
    {'name': 'Ally', 'variation_of': 'Allison'},
    
    {'name': 'Amber', 'variation_of': None},
    {'name': 'Amby', 'variation_of': 'Amber'},
    
    {'name': 'Andre', 'variation_of': None},
    {'name': 'Dre', 'variation_of': 'Andre'},
    
    {'name': 'Angela', 'variation_of': None},
    {'name': 'Angie', 'variation_of': 'Angela'},
    
    {'name': 'Austin', 'variation_of': None},
    {'name': 'Austie', 'variation_of': 'Austin'},
    
    {'name': 'Barry', 'variation_of': None},
    {'name': 'Bear', 'variation_of': 'Barry'},
    
    {'name': 'Blake', 'variation_of': None},
    
    {'name': 'Brady', 'variation_of': None},
    
    {'name': 'Brittany', 'variation_of': None},
    {'name': 'Britt', 'variation_of': 'Brittany'},
    
    {'name': 'Brooke', 'variation_of': None},
    
    {'name': 'Caleb', 'variation_of': None},
    {'name': 'Cal', 'variation_of': 'Caleb'},
    
    {'name': 'Chloe', 'variation_of': None},
    {'name': 'Chlo', 'variation_of': 'Chloe'},
    
    {'name': 'Cole', 'variation_of': None},
    
    {'name': 'Cynthia', 'variation_of': None},
    {'name': 'Cindy', 'variation_of': 'Cynthia'},
    
    {'name': 'Devin', 'variation_of': None},
    {'name': 'Dev', 'variation_of': 'Devin'},
    
    {'name': 'Dylan', 'variation_of': None},
    
    {'name': 'Ethan', 'variation_of': None},
    {'name': 'Eth', 'variation_of': 'Ethan'},
    
    {'name': 'Garrett', 'variation_of': None},
    {'name': 'Gary', 'variation_of': 'Garrett'},
    
    {'name': 'Hunter', 'variation_of': None},
    
    {'name': 'Isabella', 'variation_of': None},
    {'name': 'Izzy', 'variation_of': 'Isabella'},
    {'name': 'Bella', 'variation_of': 'Isabella'},
    
    {'name': 'Jackson', 'variation_of': None},
    {'name': 'Jack', 'variation_of': 'Jackson'},
    {'name': 'Jax', 'variation_of': 'Jackson'},
    
    {'name': 'Jasmine', 'variation_of': None},
    {'name': 'Jazz', 'variation_of': 'Jasmine'},
    {'name': 'Jas', 'variation_of': 'Jasmine'},
    
    {'name': 'Jenna', 'variation_of': None},
    {'name': 'Jen', 'variation_of': 'Jenna'},
    
    {'name': 'Kayla', 'variation_of': None},
    {'name': 'Kay', 'variation_of': 'Kayla'},
    
    {'name': 'Kyle', 'variation_of': None},
    
    {'name': 'Logan', 'variation_of': None},
    
    {'name': 'Madison', 'variation_of': None},
    {'name': 'Maddie', 'variation_of': 'Madison'},
    {'name': 'Madi', 'variation_of': 'Madison'},
    
    {'name': 'Mason', 'variation_of': None},
    {'name': 'Mase', 'variation_of': 'Mason'},
    
    {'name': 'Noah', 'variation_of': None},
    
    {'name': 'Olivia', 'variation_of': None},
    {'name': 'Liv', 'variation_of': 'Olivia'},
    {'name': 'Livvy', 'variation_of': 'Olivia'},
    {'name': 'Ollie', 'variation_of': 'Olivia'},
    
    {'name': 'Parker', 'variation_of': None},
    {'name': 'Park', 'variation_of': 'Parker'},
    
    {'name': 'Preston', 'variation_of': None},
    {'name': 'Pres', 'variation_of': 'Preston'},
    
    {'name': 'Sean', 'variation_of': None},
    {'name': 'Shawn', 'variation_of': 'Sean'},
    
    {'name': 'Sydney', 'variation_of': None},
    {'name': 'Syd', 'variation_of': 'Sydney'},
    
    {'name': 'Tanner', 'variation_of': None},
    {'name': 'Tan', 'variation_of': 'Tanner'},
    
    {'name': 'Trevor', 'variation_of': None},
    {'name': 'Trev', 'variation_of': 'Trevor'},
    
    {'name': 'Zoe', 'variation_of': None},
    {'name': 'Zo', 'variation_of': 'Zoe'},
    
    # Biblical Names
    {'name': 'Elijah', 'variation_of': None},
    {'name': 'Eli', 'variation_of': 'Elijah'},
    {'name': 'Lijah', 'variation_of': 'Elijah'},
    
    {'name': 'Gabriel', 'variation_of': None},
    {'name': 'Gabe', 'variation_of': 'Gabriel'},
    {'name': 'Gabby', 'variation_of': 'Gabriel'},
    
    {'name': 'Isaiah', 'variation_of': None},
    {'name': 'Izzy', 'variation_of': 'Isaiah'},
    
    {'name': 'Jeremiah', 'variation_of': None},
    {'name': 'Jerry', 'variation_of': 'Jeremiah'},
    {'name': 'Jem', 'variation_of': 'Jeremiah'},
    
    {'name': 'Jonah', 'variation_of': None},
    {'name': 'Joe', 'variation_of': 'Jonah'},
    
    {'name': 'Micah', 'variation_of': None},
    {'name': 'Mike', 'variation_of': 'Micah'},
    
    {'name': 'Solomon', 'variation_of': None},
    {'name': 'Sol', 'variation_of': 'Solomon'},
    {'name': 'Solly', 'variation_of': 'Solomon'},
    
    {'name': 'Ezekiel', 'variation_of': None},
    {'name': 'Zeke', 'variation_of': 'Ezekiel'},
    {'name': 'Ezek', 'variation_of': 'Ezekiel'},
    
    {'name': 'Caleb', 'variation_of': None},
    {'name': 'Cal', 'variation_of': 'Caleb'},
    
    {'name': 'Abigail', 'variation_of': None},
    {'name': 'Abby', 'variation_of': 'Abigail'},
    
    {'name': 'Hannah', 'variation_of': None},
    {'name': 'Anna', 'variation_of': 'Hannah'},
    
    {'name': 'Leah', 'variation_of': None},
    {'name': 'Lee', 'variation_of': 'Leah'},
    
    {'name': 'Naomi', 'variation_of': None},
    {'name': 'Nomi', 'variation_of': 'Naomi'},
    
    {'name': 'Ruth', 'variation_of': None},
    {'name': 'Ruthie', 'variation_of': 'Ruth'},
    
    # Scottish Names
    {'name': 'Angus', 'variation_of': None},
    {'name': 'Gus', 'variation_of': 'Angus'},
    
    {'name': 'Bruce', 'variation_of': None},
    
    {'name': 'Duncan', 'variation_of': None},
    {'name': 'Dunc', 'variation_of': 'Duncan'},
    
    {'name': 'Fiona', 'variation_of': None},
    {'name': 'Fee', 'variation_of': 'Fiona'},
    
    {'name': 'Hamish', 'variation_of': None},
    {'name': 'Ham', 'variation_of': 'Hamish'},
    
    {'name': 'Iain', 'variation_of': None},
    {'name': 'Ian', 'variation_of': 'Iain'},
    
    {'name': 'Moira', 'variation_of': None},
    {'name': 'Moire', 'variation_of': 'Moira'},
    
    # Welsh Names
    {'name': 'Gareth', 'variation_of': None},
    {'name': 'Gar', 'variation_of': 'Gareth'},
    
    {'name': 'Gwyneth', 'variation_of': None},
    {'name': 'Gwyn', 'variation_of': 'Gwyneth'},
    
    {'name': 'Rhys', 'variation_of': None},
    {'name': 'Reese', 'variation_of': 'Rhys'},
    
    {'name': 'Bronwen', 'variation_of': None},
    {'name': 'Bron', 'variation_of': 'Bronwen'},
    
    # More African Names
    {'name': 'Kwabena', 'variation_of': None},
    {'name': 'Kwab', 'variation_of': 'Kwabena'},
    
    {'name': 'Akosua', 'variation_of': None},
    {'name': 'Ako', 'variation_of': 'Akosua'},
    
    {'name': 'Chiamaka', 'variation_of': None},
    {'name': 'Chi', 'variation_of': 'Chiamaka'},
    
    {'name': 'Folake', 'variation_of': None},
    {'name': 'Fola', 'variation_of': 'Folake'},
    
    {'name': 'Kemi', 'variation_of': None},
    
    {'name': 'Tunde', 'variation_of': None},
    {'name': 'Tun', 'variation_of': 'Tunde'},
    
    {'name': 'Yemi', 'variation_of': None},
    
    {'name': 'Zuberi', 'variation_of': None},
    {'name': 'Zub', 'variation_of': 'Zuberi'},
    
    # Native American Names
    {'name': 'Aiyana', 'variation_of': None},
    {'name': 'Aya', 'variation_of': 'Aiyana'},
    
    {'name': 'Cheyenne', 'variation_of': None},
    {'name': 'Chy', 'variation_of': 'Cheyenne'},
    
    {'name': 'Dakota', 'variation_of': None},
    {'name': 'Koda', 'variation_of': 'Dakota'},
    
    {'name': 'Kai', 'variation_of': None},
    
    {'name': 'Sequoia', 'variation_of': None},
    {'name': 'Seq', 'variation_of': 'Sequoia'},
    
    # Latin American Names
    {'name': 'Esperanza', 'variation_of': None},
    {'name': 'Espe', 'variation_of': 'Esperanza'},
    
    {'name': 'Guadalupe', 'variation_of': None},
    {'name': 'Lupe', 'variation_of': 'Guadalupe'},
    
    {'name': 'Joaquín', 'variation_of': None},
    {'name': 'Joaquin', 'variation_of': 'Joaquín'},
    
    {'name': 'Marisol', 'variation_of': None},
    {'name': 'Mari', 'variation_of': 'Marisol'},
    
    {'name': 'Octavio', 'variation_of': None},
    {'name': 'Tavo', 'variation_of': 'Octavio'},
    
    {'name': 'Pilar', 'variation_of': None},
    {'name': 'Pili', 'variation_of': 'Pilar'},
    
    {'name': 'Raúl', 'variation_of': None},
    {'name': 'Raul', 'variation_of': 'Raúl'},
    
    {'name': 'Soledad', 'variation_of': None},
    {'name': 'Sol', 'variation_of': 'Soledad'},
    {'name': 'Sole', 'variation_of': 'Soledad'},
    
    # More European Names - Dutch
    {'name': 'Hendrik', 'variation_of': None},
    {'name': 'Henk', 'variation_of': 'Hendrik'},
    
    {'name': 'Pieter', 'variation_of': None},
    {'name': 'Piet', 'variation_of': 'Pieter'},
    
    {'name': 'Willem', 'variation_of': None},
    {'name': 'Wim', 'variation_of': 'Willem'},
    
    {'name': 'Marieke', 'variation_of': None},
    {'name': 'Mare', 'variation_of': 'Marieke'},
    
    # More European Names - Polish
    {'name': 'Wojciech', 'variation_of': None},
    {'name': 'Wojtek', 'variation_of': 'Wojciech'},
    
    {'name': 'Stanisław', 'variation_of': None},
    {'name': 'Stan', 'variation_of': 'Stanisław'},
    
    {'name': 'Katarzyna', 'variation_of': None},
    {'name': 'Kasia', 'variation_of': 'Katarzyna'},
    
    {'name': 'Małgorzata', 'variation_of': None},
    {'name': 'Gosia', 'variation_of': 'Małgorzata'},
    
    # More European Names - Hungarian
    {'name': 'László', 'variation_of': None},
    {'name': 'Laci', 'variation_of': 'László'},
    
    {'name': 'Zoltán', 'variation_of': None},
    {'name': 'Zoli', 'variation_of': 'Zoltán'},
    
    {'name': 'Erzsébet', 'variation_of': None},
    {'name': 'Erzsi', 'variation_of': 'Erzsébet'},
    
    # More European Names - Czech
    {'name': 'Václav', 'variation_of': None},
    {'name': 'Vašek', 'variation_of': 'Václav'},
    
    {'name': 'Petr', 'variation_of': None},
    {'name': 'Péťa', 'variation_of': 'Petr'},
    
    {'name': 'Věra', 'variation_of': None},
    {'name': 'Věrka', 'variation_of': 'Věra'},
    
    # More Asian Names - Indonesian
    {'name': 'Budi', 'variation_of': None},
    {'name': 'Bud', 'variation_of': 'Budi'},
    
    {'name': 'Sari', 'variation_of': None},
    {'name': 'Sara', 'variation_of': 'Sari'},
    
    {'name': 'Indira', 'variation_of': None},
    {'name': 'Indi', 'variation_of': 'Indira'},
    
    # More Asian Names - Malaysian
    {'name': 'Ahmad', 'variation_of': None},
    {'name': 'Mad', 'variation_of': 'Ahmad'},
    
    {'name': 'Siti', 'variation_of': None},
    {'name': 'Sit', 'variation_of': 'Siti'},
    
    # Historical Names
    {'name': 'Augustus', 'variation_of': None},
    {'name': 'Gus', 'variation_of': 'Augustus'},
    {'name': 'Augie', 'variation_of': 'Augustus'},
    
    {'name': 'Beatrice', 'variation_of': None},
    {'name': 'Bea', 'variation_of': 'Beatrice'},
    {'name': 'Trixie', 'variation_of': 'Beatrice'},
    
    {'name': 'Cordelia', 'variation_of': None},
    {'name': 'Cordy', 'variation_of': 'Cordelia'},
    {'name': 'Delia', 'variation_of': 'Cordelia'},
    
    {'name': 'Edmund', 'variation_of': None},
    {'name': 'Ed', 'variation_of': 'Edmund'},
    {'name': 'Eddie', 'variation_of': 'Edmund'},
    
    {'name': 'Florence', 'variation_of': None},
    {'name': 'Flo', 'variation_of': 'Florence'},
    {'name': 'Flossie', 'variation_of': 'Florence'},
    
    {'name': 'Genevieve', 'variation_of': None},
    {'name': 'Genny', 'variation_of': 'Genevieve'},
    {'name': 'Vivi', 'variation_of': 'Genevieve'},
    
    {'name': 'Ignatius', 'variation_of': None},
    {'name': 'Iggy', 'variation_of': 'Ignatius'},
    
    {'name': 'Josephine', 'variation_of': None},
    {'name': 'Josie', 'variation_of': 'Josephine'},
    {'name': 'Fifi', 'variation_of': 'Josephine'},
    
    {'name': 'Leopold', 'variation_of': None},
    {'name': 'Leo', 'variation_of': 'Leopold'},
    
    {'name': 'Maximilian', 'variation_of': None},
    {'name': 'Max', 'variation_of': 'Maximilian'},
    {'name': 'Maxie', 'variation_of': 'Maximilian'},
    
    {'name': 'Octavia', 'variation_of': None},
    {'name': 'Tavy', 'variation_of': 'Octavia'},
    
    {'name': 'Percival', 'variation_of': None},
    {'name': 'Percy', 'variation_of': 'Percival'},
    
    {'name': 'Quintus', 'variation_of': None},
    {'name': 'Quin', 'variation_of': 'Quintus'},
    
    {'name': 'Rosalind', 'variation_of': None},
    {'name': 'Ros', 'variation_of': 'Rosalind'},
    {'name': 'Lindy', 'variation_of': 'Rosalind'},
    
    {'name': 'Sebastian', 'variation_of': None},
    {'name': 'Seb', 'variation_of': 'Sebastian'},
    {'name': 'Bastian', 'variation_of': 'Sebastian'},
    
    {'name': 'Theodora', 'variation_of': None},
    {'name': 'Thea', 'variation_of': 'Theodora'},
    {'name': 'Dora', 'variation_of': 'Theodora'},
    
    {'name': 'Valentine', 'variation_of': None},
    {'name': 'Val', 'variation_of': 'Valentine'},
    
    {'name': 'Winifred', 'variation_of': None},
    {'name': 'Winnie', 'variation_of': 'Winifred'},
    {'name': 'Fred', 'variation_of': 'Winifred'},
    
    # Literary Names
    {'name': 'Hermione', 'variation_of': None},
    {'name': 'Hermy', 'variation_of': 'Hermione'},
    
    {'name': 'Ophelia', 'variation_of': None},
    {'name': 'Phelia', 'variation_of': 'Ophelia'},
    
    {'name': 'Portia', 'variation_of': None},
    {'name': 'Port', 'variation_of': 'Portia'},
    
    {'name': 'Evangeline', 'variation_of': None},
    {'name': 'Eva', 'variation_of': 'Evangeline'},
    {'name': 'Angel', 'variation_of': 'Evangeline'},
    
    {'name': 'Lysander', 'variation_of': None},
    {'name': 'Ly', 'variation_of': 'Lysander'},
    
    # Modern Invented Names
    {'name': 'Braxton', 'variation_of': None},
    {'name': 'Brax', 'variation_of': 'Braxton'},
    
    {'name': 'Brayden', 'variation_of': None},
    {'name': 'Bray', 'variation_of': 'Brayden'},
    
    {'name': 'Jaxon', 'variation_of': None},
    {'name': 'Jax', 'variation_of': 'Jaxon'},
    
    {'name': 'Kayden', 'variation_of': None},
    {'name': 'Kay', 'variation_of': 'Kayden'},
    
    {'name': 'Nevaeh', 'variation_of': None},
    {'name': 'Nev', 'variation_of': 'Nevaeh'},
    
    # Nature Names
    {'name': 'River', 'variation_of': None},
    {'name': 'Riv', 'variation_of': 'River'},
    
    {'name': 'Sky', 'variation_of': None},
    {'name': 'Skye', 'variation_of': 'Sky'},
    
    {'name': 'Storm', 'variation_of': None},
    
    {'name': 'Autumn', 'variation_of': None},
    {'name': 'Auty', 'variation_of': 'Autumn'},
    
    {'name': 'Summer', 'variation_of': None},
    {'name': 'Summy', 'variation_of': 'Summer'},
    
    {'name': 'Winter', 'variation_of': None},
    {'name': 'Winnie', 'variation_of': 'Winter'},
    
    {'name': 'Forest', 'variation_of': None},
    {'name': 'Forrest', 'variation_of': 'Forest'},
    
    {'name': 'Ocean', 'variation_of': None},
    {'name': 'Ocie', 'variation_of': 'Ocean'},
    
    # Virtue Names
    {'name': 'Charity', 'variation_of': None},
    {'name': 'Cherry', 'variation_of': 'Charity'},
    
    {'name': 'Prudence', 'variation_of': None},
    {'name': 'Pru', 'variation_of': 'Prudence'},
    
    {'name': 'Temperance', 'variation_of': None},
    {'name': 'Tempy', 'variation_of': 'Temperance'},
    
    {'name': 'Justice', 'variation_of': None},
    {'name': 'Just', 'variation_of': 'Justice'},
    
    {'name': 'Honor', 'variation_of': None},
    {'name': 'Honey', 'variation_of': 'Honor'},
    
    # Color Names
    {'name': 'Violet', 'variation_of': None},
    {'name': 'Vi', 'variation_of': 'Violet'},
    
    {'name': 'Scarlett', 'variation_of': None},
    {'name': 'Scar', 'variation_of': 'Scarlett'},
    
    {'name': 'Azure', 'variation_of': None},
    {'name': 'Azzie', 'variation_of': 'Azure'},
    
    {'name': 'Indigo', 'variation_of': None},
    {'name': 'Indie', 'variation_of': 'Indigo'},
    
    # Gemstone Names
    {'name': 'Ruby', 'variation_of': None},
    {'name': 'Rube', 'variation_of': 'Ruby'},
    
    {'name': 'Pearl', 'variation_of': None},
    {'name': 'Pearly', 'variation_of': 'Pearl'},
    
    {'name': 'Opal', 'variation_of': None},
    {'name': 'Opie', 'variation_of': 'Opal'},
    
    {'name': 'Jade', 'variation_of': None},
    {'name': 'Jady', 'variation_of': 'Jade'},
    
    {'name': 'Crystal', 'variation_of': None},
    {'name': 'Chrys', 'variation_of': 'Crystal'},
    
    # Place Names
    {'name': 'Austin', 'variation_of': None},
    {'name': 'Aussie', 'variation_of': 'Austin'},
    
    {'name': 'Brooklyn', 'variation_of': None},
    {'name': 'Brook', 'variation_of': 'Brooklyn'},
    
    {'name': 'Dallas', 'variation_of': None},
    {'name': 'Dal', 'variation_of': 'Dallas'},
    
    {'name': 'Denver', 'variation_of': None},
    {'name': 'Den', 'variation_of': 'Denver'},
    
    {'name': 'Phoenix', 'variation_of': None},
    {'name': 'Nix', 'variation_of': 'Phoenix'},
    
    {'name': 'Savannah', 'variation_of': None},
    {'name': 'Sav', 'variation_of': 'Savannah'},
    
    {'name': 'Orlando', 'variation_of': None},
    {'name': 'Orly', 'variation_of': 'Orlando'},
    
    # Additional Traditional Names
    {'name': 'Barnabas', 'variation_of': None},
    {'name': 'Barney', 'variation_of': 'Barnabas'},
    
    {'name': 'Bartholomew', 'variation_of': None},
    {'name': 'Bart', 'variation_of': 'Bartholomew'},
    
    {'name': 'Cornelius', 'variation_of': None},
    {'name': 'Neil', 'variation_of': 'Cornelius'},
    {'name': 'Corny', 'variation_of': 'Cornelius'},
    
    {'name': 'Demetrius', 'variation_of': None},
    {'name': 'Demi', 'variation_of': 'Demetrius'},
    
    {'name': 'Erasmus', 'variation_of': None},
    {'name': 'Ras', 'variation_of': 'Erasmus'},
    
    {'name': 'Fabian', 'variation_of': None},
    {'name': 'Fabe', 'variation_of': 'Fabian'},
    
    {'name': 'Gideon', 'variation_of': None},
    {'name': 'Gid', 'variation_of': 'Gideon'},
    
    {'name': 'Horatio', 'variation_of': None},
    {'name': 'Ratio', 'variation_of': 'Horatio'},
    
    {'name': 'Isidore', 'variation_of': None},
    {'name': 'Izzy', 'variation_of': 'Isidore'},
    
    {'name': 'Jasper', 'variation_of': None},
    {'name': 'Jazz', 'variation_of': 'Jasper'},
    
    {'name': 'Leander', 'variation_of': None},
    {'name': 'Lee', 'variation_of': 'Leander'},
    
    {'name': 'Mortimer', 'variation_of': None},
    {'name': 'Mort', 'variation_of': 'Mortimer'},
    
    {'name': 'Nathanael', 'variation_of': None},
    {'name': 'Nate', 'variation_of': 'Nathanael'},
    
    {'name': 'Obadiah', 'variation_of': None},
    {'name': 'Obie', 'variation_of': 'Obadiah'},
    
    {'name': 'Phineas', 'variation_of': None},
    {'name': 'Finn', 'variation_of': 'Phineas'},
    
    {'name': 'Quentin', 'variation_of': None},
    {'name': 'Quin', 'variation_of': 'Quentin'},
    
    {'name': 'Reginald', 'variation_of': None},
    {'name': 'Reggie', 'variation_of': 'Reginald'},
    
    {'name': 'Silas', 'variation_of': None},
    {'name': 'Si', 'variation_of': 'Silas'},
    
    {'name': 'Thaddeus', 'variation_of': None},
    {'name': 'Thad', 'variation_of': 'Thaddeus'},
    
    {'name': 'Ulysses', 'variation_of': None},
    {'name': 'Uly', 'variation_of': 'Ulysses'},
    
    {'name': 'Virgil', 'variation_of': None},
    {'name': 'Virge', 'variation_of': 'Virgil'},
    
    {'name': 'Wilbur', 'variation_of': None},
    {'name': 'Wil', 'variation_of': 'Wilbur'},
    
    {'name': 'Xavier', 'variation_of': None},
    {'name': 'Xavi', 'variation_of': 'Xavier'},
    
    {'name': 'Yancey', 'variation_of': None},
    {'name': 'Yan', 'variation_of': 'Yancey'},
    
    {'name': 'Zebedee', 'variation_of': None},
    {'name': 'Zeb', 'variation_of': 'Zebedee'},
]

def find_variations(name):
    """
    Find all variations of a given name.
    
    Args:
        name (str): The name to search for variations
        
    Returns:
        list: A list of all variations including the base name
    """
    if not name or not isinstance(name, str):
        return []
    
    name = name.strip()
    if not name:
        return []
    
    # Find the base name (the name that has variation_of as None)
    base_name = None
    
    # First, check if the input name itself is a base name
    for n in NAMES_DATA:
        if n['name'].lower() == name.lower() and n['variation_of'] is None:
            base_name = n['name']
            break
    
    # If not found as base name, find what it's a variation of
    if base_name is None:
        for n in NAMES_DATA:
            if n['name'].lower() == name.lower() and n['variation_of'] is not None:
                base_name = n['variation_of']
                break
    
    # If still not found, return empty list
    if base_name is None:
        return []
    
    # Gather all variations including the base name
    variations = []
    
    # Add the base name
    variations.append(base_name)
    
    # Add all variations of the base name
    for n in NAMES_DATA:
        if n['variation_of'] == base_name and n['name'] not in variations:
            variations.append(n['name'])
    
    # Remove duplicates and sort
    variations = list(set(variations))
    variations.sort()
    
    return variations

def get_all_base_names():
    """
    Get all base names (names that are not variations of other names).
    
    Returns:
        list: A list of all base names
    """
    base_names = []
    for name_data in NAMES_DATA:
        if name_data['variation_of'] is None:
            base_names.append(name_data['name'])
    
    return sorted(list(set(base_names)))

def search_names_containing(query):
    """
    Search for names that contain the given query string.
    
    Args:
        query (str): The search query
        
    Returns:
        list: A list of names containing the query
    """
    if not query or not isinstance(query, str):
        return []
    
    query = query.strip().lower()
    if not query:
        return []
    
    matching_names = []
    for name_data in NAMES_DATA:
        if query in name_data['name'].lower():
            matching_names.append(name_data['name'])
    
    return sorted(list(set(matching_names)))