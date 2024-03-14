-- script that creates the MySQL server user user_0d_
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILAGES ON user_0d_1.** TO user_0d_1@localhost;