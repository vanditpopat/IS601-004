CREATE TABLE
    IS601_Accounts(
        id int auto_increment PRIMARY KEY,
        account_number VARCHAR(30),
        user_id int NOT NULL,
        account_type VARCHAR(50),
        balance DECIMAL NOT NULL default 0.00,
        creation_date DATE,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY (account_type, user_id)
    )
